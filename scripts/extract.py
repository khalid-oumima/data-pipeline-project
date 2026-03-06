import requests
import json
import os

def extract_crypto_data():
    print("🚀 Début de l'extraction...")
    
    # URL de l'API (Top 10 cryptos par capitalisation)
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Vérifie si la requête a réussi
        data = response.json()

        # Chemin pour sauvegarder les données brutes
        raw_path = os.path.join('data', 'raw', 'crypto_data.json')
        
        with open(raw_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        print(f"✅ Extraction réussie ! Fichier sauvegardé dans : {raw_path}")
        return data

    except Exception as e:
        print(f"❌ Erreur lors de l'extraction : {e}")
        return None

if __name__ == "__main__":
    extract_crypto_data()