import pandas as pd
import json
import os

def transform_data():
    print("🔄 Début de la transformation...")
    
    # 1. Charger les données brutes
    raw_path = os.path.join('data', 'raw', 'crypto_data.json')
    
    if not os.path.exists(raw_path):
        print("❌ Erreur : Le fichier raw n'existe pas. Lancez d'abord extract.py")
        return None

    with open(raw_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Convertir en DataFrame Pandas
    df = pd.DataFrame(data)

    # 3. Sélectionner uniquement les colonnes intéressantes
    columns_to_keep = [
        'id', 'symbol', 'name', 'current_price', 
        'market_cap', 'total_volume', 'price_change_percentage_24h'
    ]
    df = df[columns_to_keep]

    # 4. Nettoyage et formatage
    # On s'assure que les noms sont en majuscules pour le style
    df['symbol'] = df['symbol'].str.upper()
    
    # On ajoute une colonne de timestamp pour savoir quand la donnée a été traitée
    df['processed_at'] = pd.Timestamp.now()

    # 5. Sauvegarder les données nettoyées en CSV
    processed_path = os.path.join('data', 'processed', 'crypto_cleaned.csv')
    df.to_csv(processed_path, index=False)
    
    print(f"✅ Transformation terminée ! {len(df)} lignes traitées.")
    print(f"📂 Fichier sauvegardé dans : {processed_path}")
    
    return df

if __name__ == "__main__":
    transform_data()