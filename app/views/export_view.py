import csv
from datetime import datetime
from pathlib import Path

from config import EXPORT_DIR


def exporter_csv(produits, nom=None, dossier=EXPORT_DIR):
    if nom is None:
        nom = f"produits_{datetime.now():%Y%m%d_%H%M%S}.csv"
    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / nom
    tries = sorted(
        produits,
        key=lambda p: (p.categorie, p.sous_categorie,
                       p.prix if p.prix is not None else float("inf")),
    )
    with open(chemin, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["categorie", "sous_categorie", "prix_xof", "titre", "asin", "url", "image_url"])
        for p in tries:
            prix = str(int(p.prix)) if p.prix is not None else ""
            writer.writerow([p.categorie, p.sous_categorie, prix, p.titre, p.asin, p.url, p.image_url])
    return chemin


def statistiques(produits):
    prix = [p.prix for p in produits if p.prix is not None]
    par_categorie = {}
    for p in produits:
        cle = f"{p.categorie} > {p.sous_categorie}"
        par_categorie[cle] = par_categorie.get(cle, 0) + 1
    return {
        "total": len(produits),
        "avec_prix": len(prix),
        "moyenne": sum(prix) / len(prix) if prix else None,
        "maximum": max(prix) if prix else None,
        "minimum": min(prix) if prix else None,
        "par_categorie": par_categorie,
    }