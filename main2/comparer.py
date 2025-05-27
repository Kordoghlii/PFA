import os
import json

def compare_json_files(json_folder, reports_folder):
    mismatches = []
    results = []  # 1 si tout est OK pour un fichier, 0 sinon
    comments_accurate_errors = 0
    docstrings_accurate_errors = 0
    tests_valid_errors = 0
    different_reports = []  # Pour stocker les fichiers report_Ti avec des erreurs

    total_files = 100

    for i in range(1, total_files + 1):  
        json_file = f"doc{i}.json"
        report_file = f"report_T{i}.json"
        json_path = os.path.join(json_folder, json_file)
        report_path = os.path.join(reports_folder, report_file)

        with open(json_path, 'r') as f_json, open(report_path, 'r') as f_report:
            json_data = json.load(f_json)
            report_data = json.load(f_report)

        all_ok = True

        for key in json_data:
            expected = json_data.get(key)
            found = report_data.get(key)

            if key in ["comments_accurate", "docstrings_accurate"]:
                min_val = round(expected - 0.2, 3)      # % erreur
                max_val = round(expected + 0.2, 3)     # % erreur
                found_rounded = round(found, 3) if found is not None else None

                # Vérification si la valeur est en dehors de l'intervalle
                if found_rounded is None or (found_rounded < min_val or found_rounded > max_val):
                    mismatches.append((i, key, expected, found, min_val, max_val))
                    all_ok = False
                    if key == "comments_accurate":
                        comments_accurate_errors += 1
                    else:
                        docstrings_accurate_errors += 1
            else:
                if expected != found:
                    mismatches.append((i, key, expected, found, None, None))
                    all_ok = False
                    if key == "tests_valid":
                        tests_valid_errors += 1

        if not all_ok:
            different_reports.append(report_file)

        results.append(1 if all_ok else 0)

    # Affichage des erreurs détaillées
    if mismatches:
        print("❌ Des différences ont été trouvées :\n")
        for idx, key, expected, found, min_val, max_val in mismatches:
            expected_str = f"{expected:.3f}" if isinstance(expected, float) else f"'{expected}'"
            found_str = f"{found:.3f}" if isinstance(found, float) else f"'{found}'"
            if min_val is not None and max_val is not None:
                print(f"[Doc {idx}] Erreur sur '{key}': attendu environ {expected_str} "
                      f"(entre {min_val:.3f} et {max_val:.3f}), trouvé {found_str}")
            else:
                print(f"[Doc {idx}] Erreur sur '{key}': attendu {expected_str}, trouvé {found_str}")
    else:
        print("✅ Tous les fichiers sont conformes aux règles !")

    total_success = sum(results)

    print("\n📄 Fichiers avec erreurs :")
    if different_reports:
        for f in different_reports:
            print(f" - {f}")
    else:
        print("Aucun fichier avec erreur.")

    # Pourcentages d'erreur
    print(f"\n📊 Résultats globaux :")
    print(f"✔️  Fichiers totalement conformes : {total_success}/{total_files}")
    print(f"❌ Pourcentage d'erreurs 'comments_accurate' : {comments_accurate_errors / total_files * 100:.2f}%")
    print(f"❌ Pourcentage d'erreurs 'docstrings_accurate' : {docstrings_accurate_errors / total_files * 100:.2f}%")
    print(f"❌ Pourcentage d'erreurs 'tests_valid' : {tests_valid_errors / total_files * 100:.2f}%")

# Exemple d'appel
compare_json_files("json", "reports")
