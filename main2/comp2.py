import os
import json

def list_differences_between_subdirs(json_folder, reports_folder):
    print("\n📁 Comparaison des sous-dossiers entre les dossiers JSON et Reports :\n")

    # Collecte les sous-dossiers (relatifs) dans json/ et reports/
    json_subdirs = {
        os.path.relpath(os.path.join(root), json_folder): set(files)
        for root, _, files in os.walk(json_folder)
    }

    reports_subdirs = {
        os.path.relpath(os.path.join(root), reports_folder): set(files)
        for root, _, files in os.walk(reports_folder)
    }

    all_subdirs = set(json_subdirs.keys()).union(set(reports_subdirs.keys()))

    for subdir in sorted(all_subdirs):
        json_files = json_subdirs.get(subdir, set())
        reports_files = reports_subdirs.get(subdir, set())

        if json_files != reports_files:
            print(f"📂 Sous-dossier différent : '{subdir}'")
            json_only = json_files - reports_files
            reports_only = reports_files - json_files

            if json_only:
                print(f"  - Présents uniquement dans json/{subdir} : {sorted(json_only)}")
            if reports_only:
                print(f"  - Présents uniquement dans reports/{subdir} : {sorted(reports_only)}")
        else:
            print(f"✅ Sous-dossier '{subdir}' : contenus identiques.")

def compare_json_files(json_folder, reports_folder):
    list_differences_between_subdirs(json_folder, reports_folder)  # 👈 Comparaison des sous-dossiers

    mismatches = []
    results = []
    comments_accurate_errors = 0
    docstrings_accurate_errors = 0
    tests_valid_errors = 0
    different_reports = []

    total_files = 100

    for i in range(1, total_files + 1):  
        json_file = f"doc{i}.json"
        report_file = f"report_T{i}.json"
        json_path = os.path.join(json_folder, json_file)
        report_path = os.path.join(reports_folder, report_file)

        if not os.path.exists(json_path) or not os.path.exists(report_path):
            continue  # Ignore si le fichier n'existe pas

        with open(json_path, 'r') as f_json, open(report_path, 'r') as f_report:
            json_data = json.load(f_json)
            report_data = json.load(f_report)

        all_ok = True

        for key in json_data:
            expected = json_data.get(key)
            found = report_data.get(key)

            if key in ["comments_accurate", "docstrings_accurate"]:
                min_val = round(expected - 0.2, 3)
                max_val = round(expected + 0.2, 3)
                found_rounded = round(found, 3) if found is not None else None

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
        print("\n❌ Des différences ont été trouvées :\n")
        for idx, key, expected, found, min_val, max_val in mismatches:
            expected_str = f"{expected:.3f}" if isinstance(expected, float) else f"'{expected}'"
            found_str = f"{found:.3f}" if isinstance(found, float) else f"'{found}'"
            if min_val is not None and max_val is not None:
                print(f"[Doc {idx}] Erreur sur '{key}': attendu environ {expected_str} "
                      f"(entre {min_val:.3f} et {max_val:.3f}), trouvé {found_str}")
            else:
                print(f"[Doc {idx}] Erreur sur '{key}': attendu {expected_str}, trouvé {found_str}")
    else:
        print("\n✅ Tous les fichiers sont conformes aux règles !")

    total_success = sum(results)

    print("\n📄 Fichiers avec erreurs :")
    if different_reports:
        for f in different_reports:
            print(f" - {f}")
    else:
        print("Aucun fichier avec erreur.")

    print(f"\n📊 Résultats globaux :")
    print(f"✔️  Fichiers totalement conformes : {total_success}/{total_files}")
    print(f"❌ Pourcentage d'erreurs 'comments_accurate' : {comments_accurate_errors / total_files * 100:.2f}%")
    print(f"❌ Pourcentage d'erreurs 'docstrings_accurate' : {docstrings_accurate_errors / total_files * 100:.2f}%")
    print(f"❌ Pourcentage d'erreurs 'tests_valid' : {tests_valid_errors / total_files * 100:.2f}%")


# Exemple d'appel
compare_json_files("json", "reports")






