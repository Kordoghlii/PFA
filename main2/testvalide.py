import ast
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional
load_dotenv()

class TestAnalyzer:
    def __init__(self, test_file_path):
        self.test_file_path = test_file_path
        self.report = []
        self.failed_tests = []
        print(f"\n--- Initialisation de l'analyse pour {test_file_path} ---")
        self.llm = self._init_llm()

    def _init_llm(self) -> Optional[ChatGoogleGenerativeAI]:
        """Initialise le LLM Gemini 2.0 Flash Lite."""
        print("Étape: Initialisation du LLM...")
        try:
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                print("AVERTISSEMENT: GOOGLE_API_KEY manquant")
                raise ValueError("GOOGLE_API_KEY manquant")
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash-lite",
                google_api_key=api_key,
                temperature=0.3
            )
            print("LLM initialisé (Gemini 2.0 Flash Lite)")
            return llm
        except Exception as e:
            print(f"ERREUR: Échec initialisation LLM: {e}")
            return None

    def parse_test_file(self):
        """Analyse statique du fichier de test avec AST."""
        print("\nÉtape: Analyse statique de la structure du fichier...")
        if not os.path.exists(self.test_file_path):
            print(f"ERREUR: Le fichier {self.test_file_path} n'existe pas")
            self.report.append(f"Erreur: Le fichier {self.test_file_path} n'existe pas")
            return None, {}

        try:
            with open(self.test_file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                tree = ast.parse(file_content, filename=self.test_file_path)
                print("Fichier parsé avec succès")
        except SyntaxError as e:
            print(f"ERREUR: Erreur de syntaxe dans {self.test_file_path}: {e}")
            self.report.append(f"Erreur de syntaxe dans {self.test_file_path}: {e}")
            self.failed_tests.append("SYNTAX_ERROR")
            return None, {}
        except Exception as e:
            print(f"ERREUR: Erreur lors de la lecture du fichier {self.test_file_path}: {e}")
            self.report.append(f"Erreur lors de la lecture du fichier {self.test_file_path}: {e}")
            self.failed_tests.append("FILE_READ_ERROR")
            return None, {}

        test_classes = []
        test_methods_code = {}
        print("Recherche des classes de test...")
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                inherits_testcase = any(
                    isinstance(base, ast.Name) and base.id == 'TestCase'
                    for base in node.bases
                ) or any(
                    isinstance(base, ast.Attribute) and base.attr == 'TestCase'
                    for base in node.bases
                )
                if inherits_testcase:
                    test_methods = []
                    for method in node.body:
                        if isinstance(method, ast.FunctionDef) and method.name.startswith('test_'):
                            test_methods.append(method.name)
                            # Extraire le code source de la méthode
                            method_code = ast.unparse(method)
                            test_methods_code[method.name] = method_code
                            print(f"  - Méthode trouvée: {method.name}")
                    test_classes.append({'name': node.name, 'methods': test_methods})
                    print(f"Classe de test trouvée: {node.name} avec {len(test_methods)} méthode(s)")

        if not test_classes:
            print(f"AVERTISSEMENT: Aucune classe de test valide trouvée dans {self.test_file_path}")
            self.report.append(f"Aucune classe de test valide trouvée dans {self.test_file_path}")
            self.failed_tests.append("NO_TEST_CLASSES")
        else:
            for cls in test_classes:
                self.report.append(f"Classe de test {cls['name']} trouvée avec {len(cls['methods'])} méthode(s) de test")
                if not cls['methods']:
                    print(f"AVERTISSEMENT: {cls['name']} n'a aucune méthode de test")
                    self.report.append(f"Avertissement: {cls['name']} n'a aucune méthode de test")
                    self.failed_tests.append(f"{cls['name']}_NO_METHODS")

        return tree, test_methods_code

    def check_assertions(self, tree):
        """Vérifie si les méthodes de test contiennent des assertions."""
        print("\nÉtape: Vérification des assertions...")
        if not tree:
            print("ERREUR: Impossible de vérifier les assertions (arbre AST non disponible)")
            return

        assertion_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                has_assert = False
                for n in ast.walk(node):
                    if isinstance(n, ast.Call):
                        if isinstance(n.func, ast.Attribute) and n.func.attr.startswith('assert'):
                            has_assert = True
                            assertion_found = True
                    elif isinstance(n, ast.Assert):
                        has_assert = True
                        assertion_found = True
                
                if has_assert:
                    print(f"{node.name}: Assertions trouvées")
                else:
                    print(f"AVERTISSEMENT: {node.name}: Aucune assertion trouvée")
                    self.report.append(f"Avertissement: La méthode {node.name} n'a pas d'assertion")
        
        if not assertion_found:
            print("AVERTISSEMENT: Aucune assertion trouvée dans les tests")
            self.report.append("Avertissement: Aucune assertion trouvée dans les tests")
        else:
            print("Des assertions ont été trouvées dans certains tests")

    def analyze_test_semantics(self, test_methods_code):
        """Analyse sémantique des méthodes de test avec le LLM."""
        print("\nÉtape: Analyse sémantique avec LLM...")
        if not self.llm:
            print("AVERTISSEMENT: LLM non disponible pour l'analyse sémantique")
            self.report.append("Avertissement: LLM non disponible pour l'analyse sémantique")
            return

        if not test_methods_code:
            print("AVERTISSEMENT: Aucune méthode de test à analyser")
            return
            
        print(f"Analyse de {len(test_methods_code)} méthodes de test...")
        for method_name, code in test_methods_code.items():
            print(f"  - Analyse de {method_name}...")
            prompt = f"""
Analyse le test unitaire suivant en Python. Vérifie si la syntaxe est correcte et si les assertions sont logiquement cohérentes.

Note importante: Un test est considéré VALIDE même s'il manque des assertions qui pourraient améliorer sa couverture. 
Un test n'est considéré NON VALIDE que s'il contient des erreurs de syntaxe ou de logique qui l'empêcheraient de fonctionner correctement.

Fournis une réponse claire avec :
Validité : "Valide" ou "Non valide", 1 si valide, 0 sinon
Explication : Pourquoi le test est correct ou incorrect

Code du test:
{code}
"""
            try:
                print(f"    Envoi de la requête au LLM...")
                response = self.llm.invoke(prompt)
                analysis = response.content if hasattr(response, 'content') else str(response)
                
                # Déterminer si le test est considéré valide par l'analyse LLM
                is_valid = True  # Par défaut, on considère le test valide
                
                # Vérification explicite de "Non valide" dans la réponse
                if "Non valide" in analysis or "non valide" in analysis.lower():
                    is_valid = False
                    self.failed_tests.append(method_name)
                    print(f"    {method_name}: Considéré non valide par le LLM")
                else:
                    print(f"    {method_name}: Considéré valide par le LLM")
                
                # Inclure un résumé concis dans le rapport
                summary = analysis.replace("\n", " ").strip()
                if len(summary) > 150:
                    summary = summary[:147] + "..."
                self.report.append(f"Analyse LLM pour {method_name}: {'Valide' if is_valid else 'Non valide'} - {summary}")
                
            except Exception as e:
                print(f"    ERREUR: Erreur lors de l'analyse LLM pour {method_name}: {e}")
                self.report.append(f"Erreur lors de l'analyse LLM pour {method_name}: {e}")

    def analyze(self):
        """Analyse complète du fichier de test."""
        print("\n==================================================")
        print(f"DÉBUT DE L'ANALYSE: {self.test_file_path}")
        print("==================================================")
        self.report.append(f"Analyse du fichier: {self.test_file_path}")

        # Étape 1: Analyse statique (structure et assertions)
        tree, test_methods_code = self.parse_test_file()
        self.check_assertions(tree)

        # Étape 2: Analyse sémantique avec le LLM
        if test_methods_code:
            self.analyze_test_semantics(test_methods_code)
        else:
            print("AVERTISSEMENT: Analyse sémantique ignorée (aucune méthode de test trouvée)")

        # Étape 3: Déterminer la validité
        print("\n==================================================")
        print("RÉSUMÉ DE L'ANALYSE")
        print("==================================================")
        
        # Vérification des incohérences détectées
        has_failed_tests = len(self.failed_tests) > 0
        
        # Score binaire : 0 si des incohérences sont trouvées, 1 sinon
        if has_failed_tests:
            score = 0
            print(f"Score: {score} (Tests non valides)")
            
            failed_set = set(self.failed_tests)
            if failed_set:
                failed_list = ", ".join(failed_set)
                print(f"Méthodes de test erronées: {failed_list}")
                self.report.append("Méthodes de test erronées: " + failed_list)
            
            self.report.append(f"Score: {score} (Tests non valides - incohérences détectées)")
        else:
            score = 1
            print(f"Score: {score} (Tests valides - pas d'incohérences détectées)")
            self.report.append(f"Score: {score} (Tests valides)")

        # Afficher le rapport complet dans le terminal
        print("\n==================================================")
        print("RAPPORT D'ANALYSE COMPLET")
        print("==================================================")
        for entry in self.report:
            print(f"- {entry}")
        
        print("\n==================================================")
        print("FIN DE L'ANALYSE")
        print("==================================================")

        return score


def select_and_analyze():
    """Ouvre une boîte de dialogue pour sélectionner le fichier et lance l'analyse."""
    root = tk.Tk()
    root.withdraw()

    test_file = filedialog.askopenfilename(
        title="Sélectionner le fichier de test unitaire",
        filetypes=[("Fichiers Python", "*.py"), ("Tous les fichiers", "*.*")]
    )

    if not test_file:
        messagebox.showwarning("Aucun fichier sélectionné", "Vous devez sélectionner un fichier de test pour continuer.")
        root.destroy()
        return

    analyzer = TestAnalyzer(test_file)
    analyzer.analyze()

    root.destroy()


if __name__ == "__main__":
    select_and_analyze()