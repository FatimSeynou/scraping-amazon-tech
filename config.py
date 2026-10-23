import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# --- Site cible -------------------------------------------------------------
AMAZON_URL = "https://www.amazon.com"
DEPARTEMENT = "electronics"  # rayon "Electronics" d'Amazon.com

# --- Catégories -> sous-catégories -> mot-clé envoyé à la recherche ---------
# Le menu de la console est construit automatiquement à partir de ce dictionnaire.
# Pour ajouter une sous-catégorie, il suffit d'ajouter une ligne ici.
CATEGORIES = {
    "Ordinateurs et tablettes": {
        "Ordinateurs portables": "laptop",
        "Ordinateurs de bureau": "desktop computer",
        "Tablettes": "tablet",
        "Écrans": "computer monitor",
    },
    "Téléphones et accessoires": {
        "Smartphones": "unlocked smartphone",
        "Coques": "phone case",
        "Chargeurs": "phone charger",
    },
    "Audio et vidéo": {
        "Casques audio": "headphones",
        "Enceintes Bluetooth": "bluetooth speaker",
        "Téléviseurs": "smart tv",
    },
    "Photo et jeux vidéo": {
        "Appareils photo": "digital camera",
        "Consoles de jeux": "game console",
        "Manettes": "game controller",
    },
}

# --- Réglages du scraping ---------------------------------------------------
HEADLESS = False          # False = tu vois Chrome (pratique pour tester), True = sans fenêtre
PAGES_PAR_DEFAUT = 1      # nombre de pages proposé par le menu
PAGES_MAX_AUTORISE = 3    # plafond : le menu refusera plus de 3 pages
TIMEOUT = 15              # secondes d'attente maximum pour qu'une page se charge

# --- Politesse envers le site : pauses aléatoires (min, max) en secondes ----
DELAI_ENTRE_PAGES = (3, 6)
DELAI_LECTURE = (1.5, 4)

# On s'annonce honnêtement (pas de faux navigateur).
USER_AGENT = "ProjetScrapingIIT/1.0 (projet etudiant)"

# --- Fichiers de sortie -----------------------------------------------------


DB_PATH = BASE_DIR / "data" / "produits.db"
EXPORT_DIR = BASE_DIR / "exports"


def pause(plage):
    """Retourne une durée aléatoire comprise dans la plage (min, max)."""
    return random.uniform(*plage)