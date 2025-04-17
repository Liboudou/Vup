# __init__.py
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Initialiser des variables globales
BOT_TOKEN = os.getenv("BOT_TOKEN")
CATALOG_URL = os.getenv("CATALOG_URL")
