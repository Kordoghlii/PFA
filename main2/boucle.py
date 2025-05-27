import os
from Agent import CodeAnalysisAgent  # Ton agent

# Chemin vers le dossier "test"
base_path = "Projets/test"
#Remmplacer Projets/test par le chemin de dossier où se trouvent les dossiers T1 à T100

# Initialisation de l'agent
agent = CodeAnalysisAgent()

# Parcours des dossiers T1 à T100
for i in range(1, 101):
    folder_name = f"T{i}"
    folder_path = os.path.join(base_path, folder_name)

    # Vérifie si le dossier existe
    if not os.path.isdir(folder_path):
        print(f"📁 {folder_name} introuvable.")
        continue

    print(f"🔍 Analyse de {folder_name} ...")

    # Analyse avec l'agent
    try:
        agent.analyze_project(folder_path)
        print(f"✅ Analyse terminée pour {folder_name}")
    except Exception as e:
        print(f"⚠️ Erreur pendant l’analyse de {folder_name} : {e}")
