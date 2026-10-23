import sqlite3
from pathlib import Path

from app.models.produit import Produit

class Depot:
    def __init__(self, chemin):
        if str(chemin) != ":memory:":
            Path(chemin).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(chemin))
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                asin TEXT UNIQUE NOT NULL,
                titre TEXT NOT NULL,
                prix REAL,
                image_url TEXT,
                url TEXT,
                categorie TEXT,
                sous_categorie TEXT
            )"""
        )
        self.conn.commit()

    def ajouter(self, p: Produit) -> bool:
        """Insère le produit. Renvoie False si son ASIN existe déjà."""
        curseur = self.conn.execute(
            "INSERT OR IGNORE INTO produits "
            "(asin, titre, prix, image_url, url, categorie, sous_categorie) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (p.asin, p.titre, p.prix, p.image_url, p.url, p.categorie, p.sous_categorie),
        )
        self.conn.commit()
        return curseur.rowcount == 1

    def ajouter_plusieurs(self, produits) -> int:
        return sum(self.ajouter(p) for p in produits)

    def tous(self):
        lignes = self.conn.execute(
            "SELECT asin, titre, prix, image_url, url, categorie, sous_categorie "
            "FROM produits ORDER BY categorie, sous_categorie, prix"
        ).fetchall()
        return [Produit(*ligne) for ligne in lignes]

    def nombre(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM produits").fetchone()[0]

    def fermer(self):
        self.conn.close()