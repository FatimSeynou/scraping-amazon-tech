from dataclasses import dataclass, asdict


@dataclass
class Produit:
    asin: str                      # identifiant Amazon : sert de clé unique en base
    titre: str
    prix: float | None = None      # None si Amazon n'affiche pas de prix
    image_url: str = ""
    url: str = ""
    categorie: str = ""
    sous_categorie: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        prix = f"{self.prix:.2f}" if self.prix is not None else "N/A"
        return f"{self.titre[:50]}... | {prix}"