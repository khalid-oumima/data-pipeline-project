# 🚀 Crypto Data Pipeline & Dashboard

Ce projet est un pipeline de données de bout en bout (ETL) automatisé. Il extrait les données du marché des cryptomonnaies, les transforme pour l'analyse, les stocke dans une base de données SQL et les visualise via un dashboard interactif.



## 🎯 Objectif
Démontrer la mise en place d'une architecture data moderne :
- **Extraction** : Consommation d'API REST.
- **Transformation** : Nettoyage et structuration avec Pandas.
- **Stockage** : Persistance des données en SQL.
- **Orchestration** : Automatisation des tâches.
- **Conteneurisation** : Déploiement via Docker.

## 🛠 Stack Technique
- **Langage** : Python 3.11+
- **Data** : Pandas, Requests, SQLAlchemy
- **Base de données** : SQLite (SQL)
- **Visualisation** : Streamlit
- **DevOps** : Docker

## 📁 Structure du Projet
- `scripts/` : Logique ETL (Extract, Transform, Load).
- `data/` : Stockage des fichiers bruts (JSON) et nettoyés (CSV).
- `database/` : Fichier de base de données SQLite.
- `dashboard/` : Interface utilisateur Streamlit.

## 🚀 Installation et Lancement

### 1. Via Python (Local)
1. Cloner le dépôt :
   ```bash
   git clone [https://github.com/TON_PSEUDO/crypto-data-pipeline.git](https://github.com/TON_PSEUDO/crypto-data-pipeline.git)
   cd crypto-data-pipeline

2. Créer l'environnement virtuel et installer les dépendances :
Bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

3. Lancer le pipeline complet :
Bash
python scripts/main.py

4. Lancer le Dashboard :
Bash
streamlit run dashboard/app.py

### 2. Via Docker (Recommandé)
Bash
docker build -t crypto-pipeline-app .
docker run -p 8501:8501 crypto-pipeline-app

Accédez ensuite au dashboard sur http://localhost:8501.

🤖 Automatisation

Le pipeline peut être automatisé via le planificateur de tâches Windows (en utilisant le script run_pipeline.bat) ou via une tâche Cron sous Linux pour des mises à jour régulières.

Projet réalisé par Khalid oumima - 2026.
