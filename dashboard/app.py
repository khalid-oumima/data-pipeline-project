import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

# Configuration de la page
st.set_page_config(page_title="Crypto Data Pipeline Dashboard", layout="wide")

st.title("🚀 Crypto Dashboard (Automated Pipeline)")
st.markdown("Ce dashboard affiche les données extraites via l'API CoinGecko et stockées en base SQL.")

# 1. Connexion à la base de données
db_path = os.path.join('database', 'crypto_db.db')
engine = create_engine(f'sqlite:///{db_path}')

# 2. Chargement des données
@st.cache_data # Pour éviter de recharger la base à chaque clic
def load_data():
    query = "SELECT * FROM cryptos"
    return pd.read_sql(query, con=engine)

try:
    df = load_data()

    # --- SECTION 1 : Les KPIs ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        top_crypto = df.iloc[0]
        st.metric(label="Top Asset", value=top_crypto['name'], delta=f"{top_crypto['price_change_percentage_24h']:.2f}%")
    
    with col2:
        avg_price = df['current_price'].mean()
        st.metric(label="Prix Moyen (Top 10)", value=f"${avg_price:,.2f}")
        
    with col3:
        total_market_cap = df['market_cap'].sum()
        st.metric(label="Market Cap Totale (Top 10)", value=f"${total_market_cap/1e9:.1f}B")

    st.divider()

    # --- SECTION 2 : Graphiques ---
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("💰 Prix Actuel (USD)")
        st.bar_chart(data=df, x='name', y='current_price', color='#29b5e8')

    with right_column:
        st.subheader("📉 Variation sur 24h (%)")
        st.line_chart(data=df.set_index('name')['price_change_percentage_24h'])

    # --- SECTION 3 : Table de données ---
    st.subheader("📋 Données brutes de la base SQL")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Erreur lors du chargement des données : {e}")
    st.info("Assurez-vous d'avoir lancé 'python scripts/main.py' au moins une fois.")