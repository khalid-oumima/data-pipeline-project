import pandas as pd
from sqlalchemy import create_engine
import os

def load_data_to_sql():
    print("💾 Début du chargement en base de données...")
    
    # 1. Chemin du fichier nettoyé
    processed_path = os.path.join('data', 'processed', 'crypto_cleaned.csv')
    
    if not os.path.exists(processed_path):
        print("❌ Erreur : Le fichier nettoyé n'existe pas. Lancez transform.py d'abord.")
        return

    # 2. Lire le CSV
    df = pd.read_csv(processed_path)

    # 3. Créer la connexion à SQLite (le fichier crypto_db.db sera créé ici)
    db_path = os.path.join('database', 'crypto_db.db')
    engine = create_engine(f'sqlite:///{db_path}')

    # 4. Envoyer les données vers SQL
    # if_exists='replace' : on écrase la table à chaque fois pour ce test
    # index=False : on ne veut pas de colonne d'index Pandas dans SQL
    df.to_sql('cryptos', con=engine, if_exists='replace', index=False)

    print(f"✅ Chargement terminé ! Données insérées dans la table 'cryptos'.")
    print(f"📂 Base de données située ici : {db_path}")

if __name__ == "__main__":
    load_data_to_sql()