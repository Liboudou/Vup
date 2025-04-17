# __init__.py
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Initialiser des variables globales
API_KEY = os.getenv("API_KEY")
DEBUG_MODE = os.getenv("DEBUG")
