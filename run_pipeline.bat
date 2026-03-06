@echo off
:: Accéder au dossier du projet
cd /d "C:\Users\oumim\data-pipeline-project"

:: Activer l'environnement virtuel
call venv\Scripts\activate

:: Exécuter le pipeline
python scripts/main.py

:: Optionnel : Laisser la fenêtre ouverte en cas d'erreur pour voir le log
:: pause