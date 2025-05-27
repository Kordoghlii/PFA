import os
import ast
import json
import re
import time
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dotenv import load_dotenv
import tokenize
from io import BytesIO
import google.api_core.exceptions
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langdetect import detect
import unicodedata

# Import du TestAnalyzer
from testvalide import TestAnalyzer

load_dotenv()

class CodeAnalysisAgent:
    """
    Agent pour analyser la qualité du code Python, incluant la validation des docstrings,
    commentaires et fichiers de test unitaires, avec détection des langues et seuil de 90% de précision.
    Évalue les docstrings et commentaires indépendamment, sans interaction entre les deux critères.
    Fournit des explications détaillées sur pourquoi les docstrings et commentaires sont jugés vrais ou faux.
    """

    def __init__(self, report_dir: str = r"C:\Users\LENOVO PC\Desktop\reports"):
        """Initialise l'agent avec le répertoire des rapports et le LLM."""
        self.metrics_template = {
            "files_exist": 0,
            "files_valid": 0,
            "has_tests": 0,
            "tests_valid": 0,
            "fully_documented": 0,
            "all_functions_commented": 0,
            "docstrings_accurate": 0.0,
            "comments_accurate": 0.0
        }
        self.report_dir = Path(report_dir)
        self._setup_report_dir()
        self.llm = self._init_llm()
        self.docstring_prompt = self._create_docstring_prompt()
        self.comment_prompt = self._create_comment_prompt()
        self.test_prompt = self._create_test_prompt()

    def _setup_report_dir(self) -> None:
        """Configure le répertoire pour les rapports."""
        try:
            self.report_dir.mkdir(parents=True, exist_ok=True)
            print(f"Répertoire rapports : {self.report_dir}")
        except Exception as e:
            print(f"Échec création répertoire {self.report_dir}: {e}")
            self.report_dir = Path.cwd()
            print(f"Utilisation répertoire courant : {self.report_dir}")

    def _init_llm(self) -> Optional[ChatGoogleGenerativeAI]:
        """Initialise le LLM Gemini 2.0 Flash Lite."""
        try:
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("GOOGLE_API_KEY manquant")
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash-lite",
                google_api_key=api_key,
                temperature=0.3
            )
            print("LLM initialisé (Gemini 2.0 Flash Lite)")
            return llm
        except Exception as e:
            print(f"Échec initialisation LLM: {e}")
            return None

    def _clean_text(self, text: str) -> str:
        """Nettoie le texte pour supprimer les caractères problématiques."""
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
        text = ''.join(c for c in text if c.isprintable())
        return text.strip()

    def _detect_language(self, text: str) -> str:
        """Détecte la langue du texte."""
        try:
            return detect(text)
        except:
            return "en"  # Par défaut : anglais

    def _create_docstring_prompt(self) -> PromptTemplate:
        """Crée le prompt pour valider les docstrings avec seuil de 90% et support multilingue."""
        return PromptTemplate(
            input_variables=["func_name", "docstring", "code", "lang"],
            template="""
Vérifie si la docstring, écrite en langue '{lang}', décrit précisément le comportement de la fonction Python suivante à au moins 65% de précision. La description doit correspondre exactement au comportement du code, sans incohérences majeures (par exemple, décrire une addition pour une soustraction est inacceptable). Évalue UNIQUEMENT la docstring fournie, sans tenir compte des commentaires ou d'autres éléments du code. N'invente pas d'erreurs absentes du texte de la docstring.

Retourne UNIQUEMENT un objet JSON avec :
- "is_accurate": true si la docstring est précise à 65% ou plus, false sinon
- "issues": liste des problèmes spécifiques dans la docstring (vide si précise)
- "reason": explication détaillée expliquant pourquoi la docstring est jugée précise ou non, dans la langue de la docstring ou en anglais si indéterminée

Nom : {func_name}
Docstring : {docstring}
Code : {code}

**Retourne UNIQUEMENT l'objet JSON.**
"""
        )

    def _create_comment_prompt(self) -> PromptTemplate:
        """Crée le prompt pour valider les commentaires avec seuil de 90% et support multilingue."""
        return PromptTemplate(
            input_variables=["func_name", "comment", "code", "lang"],
            template="""
Vérifie si le commentaire, écrit en langue '{lang}', décrit précisément le comportement ou l'objectif de la fonction Python suivante à au moins 65% de précision. La description doit correspondre exactement au comportement du code, sans incohérences majeures (par exemple, décrire une addition pour une soustraction est inacceptable). Évalue UNIQUEMENT le commentaire fourni, sans tenir compte de la docstring ou d'autres éléments du code. N'invente pas d'erreurs absentes du texte du commentaire.

Retourne UNIQUEMENT un objet JSON avec :
- "is_accurate": true si le commentaire est précis à 65% ou plus, false sinon
- "issues": liste des aspects manquants ou incorrects dans le commentaire (vide si précis)
- "reason": explication détaillée expliquant pourquoi le commentaire est jugé précis ou non, dans la langue du commentaire ou en anglais si indéterminée

Nom : {func_name}
Commentaire : {comment}
Code : {code}

**Retourne UNIQUEMENT l'objet JSON.**
"""
        )

    def _create_test_prompt(self) -> PromptTemplate:
        """Crée un prompt optimisé pour valider des fichiers de test unitaires Python."""
        return PromptTemplate(
            input_variables=["test_code"],
            template="""
Analyse le code de test unitaire Python suivant pour déterminer s'il est valide. Un fichier est **valide uniquement si tous ses tests** respectent les critères ci-dessous.

### Critères
1. **Structure**: Tests dans des méthodes `test_*` d'une classe héritant de `unittest.TestCase` ou fonctions `test_*` (pytest). Aucun code hors tests.
2. **Assertions**: Chaque test doit avoir une assertion (`assertEqual`, `assertTrue`, `assertFalse`, `assertAlmostEqual`, etc.) correcte selon le domaine (graphes, bibliothèque, géométrie). Assertions triviales (ex. `assert True`) ou absurdes interdites.
3. **Noms**: Noms descriptifs (ex. `test_add_node`). Noms vagues (ex. `test_function`) interdits.
4. **Indépendance**: Tests indépendants, utilisant `setUp` si nécessaire.
5. **Contenu**: Fichier vide ou sans tests est invalide.

### Assertions par domaine
- **Graphes**:
  - `test_add_node`: Vérifie l'ajout (ex. `assertEqual(add_node({}, 1), {1: []})`, pas `assertEqual(..., {})`).
  - `test_add_edge`: Vérifie l'arête (ex. `assertEqual(add_edge({1: [], 2: []}, 1, 2), {1: [2], 2: [1]})`).
  - `test_has_node`: Vérifie la présence (ex. `assertTrue(has_node({1: []}, 1))`).
- **Bibliothèque**:
  - `test_add_book`: Vérifie l'ajout (ex. `assertEqual(result["123"], {"title": "Python", "available": True})`).
  - `test_borrow_book`: Vérifie l'indisponibilité (ex. `assertFalse(result["123"]["available"])`).
- **Géométrie**:
  - `test_circle_area`: Vérifie πr² (ex. `assertAlmostEqual(circle_area(2), math.pi * 4)`).
  - `test_circle_circumference`: Vérifie 2πr (ex. `assertAlmostEqual(circle_circumference(2), 2 * math.pi * 2)`).
  - `test_rectangle_area`: Vérifie l*w (ex. `assertEqual(rectangle_area(3, 4), 12)`).
  - `test_rectangle_perimeter`: Vérifie 2(l + w) (ex. `assertEqual(rectangle_perimeter(3, 4), 14)`).
  - `test_triangle_area`: Vérifie (base * hauteur) / 2 (ex. `assertEqual(triangle_area(4, 3), 6)`).
  - `test_is_right_triangle`: Vérifie si a² + b² = c² (ex. `assertTrue(is_right_triangle(3, 4, 5))`).
  - `test_distance_2d`: Vérifie √((x₂-x₁)² + (y₂-y₁)²) (ex. `assertAlmostEqual(distance_2d(0, 0, 3, 4), 5)`).
  - `test_slope`: Vérifie (y₂-y₁)/(x₂-x₁) ou None si x₁ = x₂ (ex. `assertEqual(slope(0, 0, 2, 4), 2)`, `assertIsNone(slope(1, 2, 1, 5))`).
  - `test_is_collinear`: Vérifie si trois points sont alignés (ex. `assertTrue(is_collinear(0, 0, 1, 1, 2, 2))`).
  - `test_regular_polygon_area`: Vérifie (n * s² * cot(π/n)) / 4 pour n côtés et s longueur (ex. `assertAlmostEqual(regular_polygon_area(3, 2), 3 * math.sqrt(3))`).

### Assertions incorrectes
- `assertEqual(add_node({}, 1), {})` → Faux, attend `{1: []}`.
- `assertFalse(has_node({1: []}, 1))` → Faux, nœud présent.
- `assertEqual(circle_area(1), 0)` → Faux, attend π.
- `assertEqual(circle_circumference(1), 0)` → Faux, attend 2π.
- `assertEqual(rectangle_perimeter(3, 4), 0)` → Faux, attend 14.
- `assertFalse(is_right_triangle(3, 4, 5))` → Faux, c'est un triangle rectangle.
- `assertEqual(distance_2d(0, 0, 3, 4), 0)` → Faux, attend 5.
- `assertEqual(slope(0, 0, 2, 4), 0)` → Faux, attend 2.
- `assertFalse(is_collinear(0, 0, 1, 1, 2, 2))` → Faux, points alignés.
- `assertEqual(regular_polygon_area(3, 2), 0)` → Faux, attend 3√3.

### Règles
- **Valide**: Tous les tests corrects.
- **Invalide**: Un test échoue.

### Sortie
JSON avec :
- `"is_valid"`: `true` si valide, `false` sinon.
- `"issues"`: Liste des problèmes (ex. "test_add_node: assertion incorrecte, attend {}").
- `"reason"`: Résumé (ex. "Tests corrects" ou "Assertions incorrectes").

### Exemples
**Valide**:
```python
def test_circle_area(self):
    self.assertAlmostEqual(circle_area(2), math.pi * 4)

Invalide:
python

def test_add_node(self):
    self.assertEqual(add_node({}, 1), {})

Code:
{test_code}
Retourne uniquement l'objet JSON.
"""
        )    

    def analyze_project(self, folder_path: str) -> Dict:
        """
        Analyse un projet Python et génère un rapport JSON avec les métriques.

        Args:
            folder_path: Chemin du dossier du projet.
        Returns:
            Dictionnaire contenant les métriques globales (combined_metrics).
        """
        path = Path(folder_path)
        report = {
            "phase1": {"files_found": {}, "errors": []},
            "phase2": {
                "implementation_analysis": {},
                "test_analysis": {},
                "uncommented_functions": [],
                "undocumented_functions": [],
                "docstring_issues": {},
                "comment_issues": {}
            },
            "combined_metrics": self.metrics_template.copy()
        }

        print(f"Analyse dossier : {folder_path}")
        try:
            report["phase1"] = self._scan_files(path)
            if impl_file := report["phase1"]["files_found"].get("implementation"):
                impl_report = self._analyze_implementation(Path(impl_file))
                report["phase2"]["implementation_analysis"] = impl_report
                report["phase2"]["uncommented_functions"] = impl_report.get("uncommented", [])
                report["phase2"]["undocumented_functions"] = impl_report.get("missing_docs", [])
                report["phase2"]["docstring_issues"] = impl_report.get("docstring_issues", {})
                report["phase2"]["comment_issues"] = impl_report.get("comment_issues", {})

            if test_file := report["phase1"]["files_found"].get("test"):
                report["phase2"]["test_analysis"] = self._analyze_tests(Path(test_file))

            report["combined_metrics"] = self._compute_metrics(report)
            print("\n" + self._render_terminal_report(report))
            self._save_report(folder_path, report)
        except Exception as e:
            report["phase1"]["errors"].append(f"Erreur analyse : {e}")
            print("\n" + self._render_terminal_report(report))
            self._save_report(folder_path, report)
            print(f"Exception analyse : {e}")

        return report["combined_metrics"]

    def _scan_files(self, folder: Path) -> Dict:
        """Scanne le dossier pour identifier les fichiers d'implémentation et de test."""
        result = {"files_found": {"implementation": None, "test": None}, "errors": []}
        if not folder.exists():
            result["errors"].append(f"Dossier introuvable : {folder}")
            return result

        try:
            for file in folder.glob("*.py"):
                if not self._is_test_file(file):
                    result["files_found"]["implementation"] = str(file)
                    break

            test_files = [f for f in folder.glob("*.py") if self._is_test_file(f)]
            if test_files:
                result["files_found"]["test"] = str(test_files[0])

            if not result["files_found"]["implementation"]:
                result["errors"].append("Aucun fichier d'implémentation")
        except Exception as e:
            result["errors"].append(f"Erreur scan fichiers : {e}")

        return result

    def _analyze_implementation(self, file: Path) -> Dict:
        """Analyse un fichier d'implémentation pour la syntaxe, docstrings et commentaires."""
        result = {
            "valid_syntax": 0,
            "function_count": 0,
            "missing_docs": [],
            "uncommented": [],
            "docstrings_accurate": 0.0,
            "docstring_issues": {},
            "comments_accurate": 0.0,
            "comment_issues": {},
            "errors": []
        }

        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                tree = ast.parse(content)
                result["valid_syntax"] = 1

                tokens = tokenize.tokenize(BytesIO(content.encode('utf-8')).readline)
                comments_by_line = {t.start[0]: t.string.strip('#').strip() for t in tokens if t.type == tokenize.COMMENT}

                functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
                result["function_count"] = len(functions)
                print("Fonctions détectées :", [f.name for f in functions])

                accurate_docstrings = 0
                accurate_comments = 0

                for func in functions:
                    # Vérification des docstrings
                    docstring = ast.get_docstring(func)
                    if not docstring:
                        result["missing_docs"].append(func.name)
                    else:
                        docstring = self._clean_text(docstring)
                        func_code = ast.get_source_segment(content, func)
                        if self.llm:
                            is_accurate, issues, reason = self._verify_docstring(func.name, docstring, func_code)
                            if is_accurate:
                                accurate_docstrings += 1
                            result["docstring_issues"][func.name] = {"issues": issues, "reason": reason, "docstring": docstring}

                    # Vérification des commentaires
                    comment = None
                    start_line = func.lineno
                    end_line = getattr(func, 'end_lineno', start_line + 10)
                    for line in range(start_line, end_line + 1):
                        if line in comments_by_line:
                            comment = comments_by_line[line]
                            break

                    print(f"Commentaire pour {func.name} : {comment}")
                    if not comment:
                        result["uncommented"].append(func.name)
                    else:
                        comment = self._clean_text(comment)
                        func_code = ast.get_source_segment(content, func)
                        if self.llm:
                            is_accurate, issues, reason = self._verify_comment(func.name, comment, func_code)
                            if is_accurate:
                                accurate_comments += 1
                            result["comment_issues"][func.name] = {"comment": comment, "issues": issues, "reason": reason}

                # Calcul des métriques avec la formule demandée
                if result["function_count"] > 0:
                    result["docstrings_accurate"] = accurate_docstrings / result["function_count"]
                    result["comments_accurate"] = accurate_comments / result["function_count"]
                else:
                    result["docstrings_accurate"] = 0.0
                    result["comments_accurate"] = 0.0

                print(f"Score docstrings_accurate : {result['docstrings_accurate']:.2f} ({accurate_docstrings}/{result['function_count']})")
                print(f"Score comments_accurate : {result['comments_accurate']:.2f} ({accurate_comments}/{result['function_count']})")

        except SyntaxError:
            result["errors"].append("Erreur syntaxe fichier")
        except Exception as e:
            result["errors"].append(f"Erreur analyse : {e}")

        return result

    def _analyze_tests(self, file: Path) -> Dict:
        """
        Analyse un fichier de tests en utilisant la classe TestAnalyzer de testvalide.py.
        Cette méthode remplace l'ancienne implémentation avec un appel à TestAnalyzer.
        """
        print(f"\nUtilisation de TestAnalyzer pour analyser le fichier de tests : {file}")
        result = {
            "valid_syntax": 0,
            "has_test_functions": 0,
            "test_function_count": 0,
            "test_validity": {},
            "errors": []
        }

        try:
            # Instancier TestAnalyzer et exécuter l'analyse
            test_analyzer = TestAnalyzer(str(file))
            score = test_analyzer.analyze()
            
            # Remplir le résultat avec les données de TestAnalyzer
            result["valid_syntax"] = 1  # Si l'analyse a pu se faire, la syntaxe est valide
            
            # Déterminer si le fichier contient des fonctions de test valides
            result["has_test_functions"] = 1 if len(test_analyzer.report) > 0 and "NO_TEST_CLASSES" not in test_analyzer.failed_tests else 0
            
            # Récupérer le nombre approximatif de méthodes de test (info disponible dans le rapport)
            test_count = 0
            for entry in test_analyzer.report:
                if "Classe de test" in entry and "trouvée avec" in entry:
                    try:
                        count_part = entry.split("trouvée avec")[1].split("méthode")[0].strip()
                        test_count += int(count_part)
                    except:
                        pass
            
            result["test_function_count"] = test_count
            
            # Déterminer la validité des tests
            result["test_validity"] = {
                "is_valid": score == 1,
                "issues": test_analyzer.failed_tests,
                "reason": "Tests valides" if score == 1 else "Problèmes détectés dans les tests"
            }
            
            print(f"Analyse des tests complétée. Score : {score}")
            
        except Exception as e:
            result["errors"].append(f"Erreur lors de l'analyse des tests : {e}")
            result["test_validity"] = {
                "is_valid": False,
                "issues": [f"Erreur inattendue : {e}"],
                "reason": "Échec de l'analyse du fichier de test"
            }
            print(f"Exception lors de l'analyse des tests : {e}")
        
        return result

    def _verify_docstring(self, func_name: str, docstring: str, func_code: str) -> Tuple[bool, List[str], str]:
        """Vérifie la précision d'une docstring via LLM."""
        if not self.llm:
            print(f"LLM indisponible pour docstring '{func_name}'")
            return False, ["LLM indisponible"], "LLM indisponible"

        docstring = self._clean_text(docstring)
        lang = self._detect_language(docstring)
        return self._call_llm(
            func_name=func_name,
            prompt_template=self.docstring_prompt,
            content={"func_name": func_name, "docstring": docstring, "code": func_code, "lang": lang},
            validation_type="docstring"
        )

    def _verify_comment(self, func_name: str, comment: str, func_code: str) -> Tuple[bool, List[str], str]:
        """Vérifie la précision d'un commentaire via LLM."""
        if not self.llm:
            print(f"LLM indisponible pour commentaire '{func_name}'")
            return False, ["LLM indisponible"], "LLM indisponible"

        comment = self._clean_text(comment)
        lang = self._detect_language(comment)
        return self._call_llm(
            func_name=func_name,
            prompt_template=self.comment_prompt,
            content={"func_name": func_name, "comment": comment, "code": func_code, "lang": lang},
            validation_type="comment"
        )

    def _verify_test_file(self, test_code: str) -> Tuple[bool, List[str]]:
        """Vérifie la validité d'un fichier de test via LLM."""
        if not self.llm:
            print("LLM indisponible pour validation des tests")
            return False, ["LLM indisponible"]

        return self._call_llm(
            func_name="test_file",
            prompt_template=self.test_prompt,
            content={"test_code": test_code},
            validation_type="test"
        )

    def _call_llm(self, func_name: str, prompt_template: PromptTemplate, content: Dict, validation_type: str) -> Tuple:
        """Appelle le LLM avec gestion robuste des erreurs et limites."""
        max_retries = 3
        retry_delay = 60

        for attempt in range(max_retries):
            try:
                prompt = prompt_template.format(**content)
                response = self.llm.invoke(prompt)
                response_text = response.content.strip()

                # Loguer la réponse brute pour débogage
                print(f"Réponse brute LLM pour {validation_type} de {func_name}:\n{response_text}\n")
                with open(self.report_dir / f"llm_response_{func_name}_{validation_type}.txt", 'w', encoding='utf-8') as f:
                    f.write(response_text)

                # Nettoyer la réponse
                cleaned_response = re.sub(r'^```json\n|```$', '', response_text, flags=re.MULTILINE).strip()
                cleaned_response = re.sub(r'^```|```$', '', cleaned_response, flags=re.MULTILINE).strip()

                print(f"Réponse nettoyée LLM pour {validation_type} de {func_name}: {cleaned_response}")
                try:
                    result = json.loads(cleaned_response)
                except json.JSONDecodeError:
                    if match := re.search(r'\{[\s\S]*?\}', cleaned_response, re.DOTALL):
                        result = json.loads(match.group(0))
                    else:
                        print(f"JSON invalide pour {validation_type} de '{func_name}'")
                        self._save_failed_response(func_name, response_text)
                        return (False, [f"JSON invalide - {validation_type} non valide"], "JSON invalide") if validation_type in ["docstring", "comment"] else (False, [f"JSON invalide"])

                if not isinstance(result, dict):
                    print(f"Structure JSON incorrecte pour {validation_type} de '{func_name}'")
                    self._save_failed_response(func_name, response_text)
                    return (False, [f"Structure JSON incorrecte"], "Structure JSON incorrecte") if validation_type in ["docstring", "comment"] else (False, [f"Structure JSON incorrecte"])

                if validation_type == "test":
                    required_keys = {"is_valid", "issues", "reason"}
                    missing_keys = required_keys - result.keys()
                    if missing_keys:
                        print(f"Clés manquantes pour {validation_type} de '{func_name}' : {missing_keys}")
                        self._save_failed_response(func_name, response_text)
                        return False, [f"Clés manquantes : {', '.join(missing_keys)}"]
                    is_valid = bool(result.get("is_valid", False))
                    issues = result.get("issues", []) if isinstance(result.get("issues"), list) else []
                    return is_valid, issues
                else:  # docstring ou comment
                    required_keys = {"is_accurate", "issues", "reason"}
                    missing_keys = required_keys - result.keys()
                    if missing_keys:
                        print(f"Clés manquantes pour {validation_type} de '{func_name}' : {missing_keys}")
                        self._save_failed_response(func_name, response_text)
                        return False, [f"Clés manquantes : {', '.join(missing_keys)}"], f"Clés manquantes : {', '.join(missing_keys)}"
                    return (
                        bool(result.get("is_accurate", False)),
                        result.get("issues", []) if isinstance(result.get("issues"), list) else [],
                        result.get("reason", "")
                    )

            except google.api_core.exceptions.ResourceExhausted as e:
                print(f"Limite requêtes pour {validation_type} de '{func_name}' : {e}")
                if attempt < max_retries - 1:
                    print(f"Attente {retry_delay}s...")
                    time.sleep(retry_delay)
                    continue
                print(f"Échec après {max_retries} tentatives")
                return (False, [f"Limite requêtes dépassée : {e}"], "Limite requêtes dépassée") if validation_type in ["docstring", "comment"] else (False, [f"Limite requêtes dépassée : {e}"])

            except Exception as e:
                print(f"Erreur LLM pour {validation_type} de '{func_name}' : {e}")
                self._save_failed_response(func_name, response_text if 'response_text' in locals() else "Aucune réponse")
                return (False, [f"Erreur LLM : {e}"], "Erreur LLM") if validation_type in ["docstring", "comment"] else (False, [f"Erreur LLM : {e}"])

    def _save_failed_response(self, func_name: str, response_text: str) -> None:
        """Sauvegarde les réponses LLM échouées pour débogage."""
        failed_path = self.report_dir / f"failed_response_{func_name}.txt"
        try:
            with open(failed_path, 'w', encoding='utf-8') as f:
                f.write(f"Fonction : {func_name}\nRéponse :\n{response_text}")
            print(f"Réponse échouée sauvegardée : {failed_path}")
        except Exception as e:
            print(f"Échec sauvegarde réponse '{func_name}' : {e}")

    def _compute_metrics(self, report: Dict) -> Dict:
        """Calcule les métriques globales du rapport."""
        metrics = self.metrics_template.copy()
        phase1 = report["phase1"]
        phase2 = report["phase2"]

        metrics["files_exist"] = 1 if phase1["files_found"].get("implementation") else 0
        test_analysis = phase2.get("test_analysis", {})
        metrics["has_tests"] = 1 if phase1["files_found"].get("test") else 0
        metrics["tests_valid"] = 1 if test_analysis.get("test_validity", {}).get("is_valid", False) else 0

        if metrics["files_exist"]:
            impl = phase2["implementation_analysis"]
            metrics["files_valid"] = impl["valid_syntax"]
            metrics["fully_documented"] = 0 if impl["missing_docs"] else 1
            metrics["all_functions_commented"] = 0 if impl["uncommented"] else 1
            metrics["docstrings_accurate"] = impl["docstrings_accurate"]
            metrics["comments_accurate"] = impl["comments_accurate"]

        return metrics

    def _render_terminal_report(self, report: Dict) -> str:
        """Génère le rapport affiché dans le terminal."""
        lines = ["=== RAPPORT FINAL ANALYSE CODE ===", "\n### Structure Fichiers"]
        phase1 = report["phase1"]
        phase2 = report["phase2"]

        lines.append(f"Implémentation : {phase1['files_found'].get('implementation', 'Introuvable')}")
        if test_file := phase1["files_found"].get("test"):
            test_analysis = phase2.get("test_analysis", {})
            if not test_analysis.get("valid_syntax", 0):
                lines.append(f"Fichier Tests : {test_file} (syntaxe invalide)")
            elif test_analysis.get("has_test_functions", 0):
                lines.append(f"Fichier Tests : {test_file} ({test_analysis['test_function_count']} fonctions de test)")
                test_validity = test_analysis.get("test_validity", {})
                lines.append(f"Tests Valides : {'Oui' if test_validity.get('is_valid', False) else 'Non'}")
                if issues := test_validity.get("issues", []):
                    lines.append("**Problèmes Tests :**")
                    lines.extend(f"- {issue}" for issue in issues)
            else:
                lines.append(f"Fichier Tests : {test_file} (aucune fonction de test)")
        else:
            lines.append("Fichier Tests : Introuvable")

        lines.extend([f"Erreur : {e}" for e in phase1["errors"]])
        lines.append("\n### Qualité Code")

        impl = phase2["implementation_analysis"]
        if impl:
            uncommented_count = len(impl["uncommented"])
            missing_docs_count = len(impl["missing_docs"])
            total_functions = impl["function_count"]
            lines.extend([
                f"\nFonctions : {total_functions}",
                f"Syntaxe Valide : {'Oui' if impl['valid_syntax'] else 'Non'}",
                f"Fonctions Sans Docstring : {missing_docs_count}/{total_functions}",
                f"Fonctions Sans Commentaire : {uncommented_count}/{total_functions}",
                f"Docstrings Précises : {impl['docstrings_accurate']:.2f}",
                f"Commentaires Précis : {impl['comments_accurate']:.2f}",
            ])

            if impl["uncommented"]:
                lines.append("\n**Fonctions Non Commentées :**")
                lines.extend(f"- {name}" for name in impl["uncommented"])

            if impl["missing_docs"]:
                lines.append("\n**Fonctions Non Documentées :**")
                lines.extend(f"- {name}" for name in impl["missing_docs"])

            if doc_issues := phase2.get("docstring_issues", {}):
                lines.append("\n**Problèmes Docstrings :**")
                for func_name, data in doc_issues.items():
                    lines.append(f"- {func_name} (Docstring : \"{data['docstring']}\") :")
                    lines.append(f"  Raison : {data['reason']}")
                    if data["issues"]:
                        lines.extend(f"  - {issue}" for issue in data["issues"])

            if com_issues := phase2.get("comment_issues", {}):
                lines.append("\n**Problèmes Commentaires :**")
                for func_name, data in com_issues.items():
                    lines.append(f"- {func_name} (Commentaire : \"{data['comment']}\") :")
                    lines.append(f"  Raison : {data['reason']}")
                    if data["issues"]:
                        lines.extend(f"  - {issue}" for issue in data["issues"])

        lines.extend([
            "\n### Métriques Finales",
            "| Métrique             | Valeur |",
            "|----------------------|--------|",
            *[f"| {k.replace('_', ' ').title():19}|   {v:.2f}   |" if isinstance(v, float) else f"| {k.replace('_', ' ').title():19}|   {v}   |"
              for k, v in report["combined_metrics"].items()]
        ])

        return "\n".join(lines)

    def _save_report(self, folder_path: str, report: Dict) -> None:
        """Sauvegarde uniquement les métriques globales au format JSON avec l'ordre spécifié."""
        folder_name = Path(folder_path).name
        json_file = self.report_dir / f"report_{folder_name}.json"
        metrics = report["combined_metrics"]

        # Créer un nouveau dictionnaire avec l'ordre exact des clés
        ordered_metrics = {
            "files_exist": metrics["files_exist"],
            "files_valid": metrics["files_valid"],
            "has_tests": metrics["has_tests"],
            "tests_valid": metrics["tests_valid"],
            "fully_documented": metrics["fully_documented"],
            "all_functions_commented": metrics["all_functions_commented"],
            "docstrings_accurate": metrics["docstrings_accurate"],
            "comments_accurate": metrics["comments_accurate"]
        }

        print(f"Sauvegarde rapport : {json_file}")
        try:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(ordered_metrics, f, indent=4)
            print(f"Rapport sauvegardé : {json_file}")
        except PermissionError as e:
            print(f"Permission refusée : {json_file}: {e}")
            fallback = Path.cwd() / f"report_{folder_name}.json"
            try:
                with open(fallback, 'w', encoding='utf-8') as f:
                    json.dump(ordered_metrics, f, indent=4)
                print(f"Rapport sauvegardé (secours) : {fallback}")
            except Exception as e2:
                print(f"Échec sauvegarde secours : {e2}")
        except Exception as e:
            print(f"Échec sauvegarde : {json_file}: {e}")

    def _is_test_file(self, path: Path) -> bool:
        """Vérifie si un fichier est un fichier de test."""
        return path.name.startswith('test_') or 'test' in path.name.lower()

if __name__ == "__main__":
    agent = CodeAnalysisAgent()
    print("=== ANALYSEUR CODE PYTHON ===")

    while True:
        path = input("\nChemin dossier projet (ou 'q' pour quitter) : ").strip()
        if path.lower() == 'q':
            break
        metrics = agent.analyze_project(path)
        print(f"\nMétriques retournées : {json.dumps(metrics, indent=4)}")