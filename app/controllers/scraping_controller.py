from app.models.depot import Depot
from app.scraper.amazon_scraper import AmazonScraper
from config import DB_PATH


class ScrapingController:
    def __init__(self, chemin_db=DB_PATH):
        self.depot = Depot(chemin_db)

    def lancer(self, categorie, sous_categorie, mot_cle, nb_pages):
        """Scrape une sous-catégorie, enregistre en base, renvoie (trouvés, nouveaux)."""
        print(f"Scraping : {categorie} > {sous_categorie}")
        produits = AmazonScraper().scraper(categorie, sous_categorie, mot_cle, nb_pages)
        nouveaux = self.depot.ajouter_plusieurs(produits)
        return len(produits), nouveaux

    def fermer(self):
        self.depot.fermer()