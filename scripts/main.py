from extract import extract_crypto_data
from transform import transform_data
from load import load_data_to_sql

def run_pipeline():
    print("--- 🚀 LANCEMENT DU PIPELINE DATA ---")
    
    # Étape 1 : Extraction
    extract_crypto_data()
    
    # Étape 2 : Transformation
    transform_data()
    
    # Étape 3 : Chargement
    load_data_to_sql()
    
    print("--- ✅ PIPELINE TERMINÉ AVEC SUCCÈS ---")

if __name__ == "__main__":
    run_pipeline()