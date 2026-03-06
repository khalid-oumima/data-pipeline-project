# 1. Utiliser une image Python légère
FROM python:3.11-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier tout le contenu du projet dans le conteneur
COPY . .

# 5. Exposer le port utilisé par Streamlit
EXPOSE 8501

# 6. Commande pour lancer le dashboard par défaut
CMD ["streamlit", "run", "dashboard/app.py", "--server.port=8501", "--server.address=0.0.0.0"]