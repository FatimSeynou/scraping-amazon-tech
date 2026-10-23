from config import PAGES_MAX_AUTORISE, PAGES_PAR_DEFAUT


def afficher_menu_principal():
    print("\n=== SCRAPING AMAZON.COM - TECHNOLOGIE ===")
    print("[1] Lancer un scraping")
    print("[2] Afficher, statistiques et export CSV")
    print("[3] Quitter")
    return input("Ton choix : ").strip()


def choisir_dans_liste(titre, options):
    print(f"\n{titre}")
    for i, libelle in enumerate(options, 1):
        print(f"  [{i}] {libelle}")
    print("  [0] Retour")
    while True:
        rep = input("Ton choix : ").strip()
        if rep == "0":
            return None
        if rep.isdigit() and 1 <= int(rep) <= len(options):
            return int(rep) - 1
        print("Choix invalide.")


def demander_nombre_pages():
    while True:
        rep = input(f"Nombre de pages (1 à {PAGES_MAX_AUTORISE}, "
                    f"Entrée = {PAGES_PAR_DEFAUT}) : ").strip()
        if rep == "":
            return PAGES_PAR_DEFAUT
        if rep.isdigit() and 1 <= int(rep) <= PAGES_MAX_AUTORISE:
            return int(rep)
        print("Nombre de pages invalide.")


def afficher_succes(message):
    print("OK :", message)


def afficher_erreur(message):
    print("ERREUR :", message)


def afficher_produits(produits, limite=10):
    print(f"\n{len(produits)} produits (les {min(limite, len(produits))} premiers) :")
    for p in produits[:limite]:
        prix = f"{int(p.prix)} XOF" if p.prix is not None else "prix inconnu"
        print(f"- {p.titre[:60]} | {prix} | {p.sous_categorie}")


def afficher_statistiques(stats):
    print("\nStatistiques")
    print(f"Total : {stats['total']} (dont {stats['avec_prix']} avec prix)")
    for nom, cle in (("Prix moyen(XOF)", "moyenne"), ("Prix maximum(XOF)", "maximum"), ("Prix minimum(XOF)", "minimum")):
        valeur = stats[cle]
        print(f"{nom} : {valeur:.0f}" if valeur is not None else f"{nom} : aucune donnée")
    print("Produits par catégorie :")
    for nom, nombre in stats["par_categorie"].items():
        print(f"  {nom} : {nombre}")