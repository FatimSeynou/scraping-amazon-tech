from app.controllers.scraping_controller import ScrapingController
from app.views.console_view import (
    afficher_erreur,
    afficher_menu_principal,
    afficher_produits,
    afficher_statistiques,
    afficher_succes,
    choisir_dans_liste,
    demander_nombre_pages,
)
from app.views.export_view import exporter_csv, statistiques
from config import CATEGORIES


def choisir_sous_categorie():
    """Renvoie (categorie, sous_categorie, mot_cle) ou None si l'utilisateur annule."""
    noms_categories = list(CATEGORIES)
    i = choisir_dans_liste("Quelle catégorie veux-tu scraper ?", noms_categories)
    if i is None:
        return None
    categorie = noms_categories[i]
    sous = list(CATEGORIES[categorie])
    j = choisir_dans_liste(f"Quelle sous-catégorie de « {categorie} » ?", sous)
    if j is None:
        return None
    nom_sous = sous[j]
    return categorie, nom_sous, CATEGORIES[categorie][nom_sous]


def main():
    controleur = ScrapingController()
    try:
        while True:
            choix = afficher_menu_principal()
            if choix == "1":
                selection = choisir_sous_categorie()
                if selection is None:
                    continue
                nb_pages = demander_nombre_pages()
                categorie, sous, mot_cle = selection
                trouves, nouveaux = controleur.lancer(categorie, sous, mot_cle, nb_pages)
                afficher_succes(f"{trouves} produits trouvés, {nouveaux} nouveaux enregistrés.")
            elif choix == "2":
                produits = controleur.depot.tous()
                if not produits:
                    afficher_erreur("Aucun produit en base. Lance d'abord un scraping.")
                    continue
                afficher_produits(produits)
                afficher_statistiques(statistiques(produits))
                chemin = exporter_csv(produits)
                afficher_succes(f"CSV créé : {chemin}")
            elif choix == "3":
                break
            else:
                afficher_erreur("Choix invalide.")
    finally:
        controleur.fermer()


if __name__ == "__main__":
    main()