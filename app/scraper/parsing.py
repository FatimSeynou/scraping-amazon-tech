import re
from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from app.models.produit import Produit
from config import AMAZON_URL

SEL_CARTE = "div[data-component-type='s-search-result']"
SEL_TITRE = "h2 span"
SEL_LIEN = "a[href*='/dp/']"
SEL_PRIX = "span.a-price span.a-offscreen"
SEL_IMAGE = "img.s-image"


def convertir_prix(texte):
    """'$499.99' -> 499.99 ; '$1,299.00' -> 1299.0 ; '$1,299' -> 1299.0 ; '' -> None"""
    nombre = re.sub(r"[^\d.,]", "", texte)
    if not nombre:
        return None
    # Si le texte finit par . suivi d'1 ou 2 chiffres, c'est la partie décimale
    decimales = re.search(r"\.(\d{1,2})$", nombre)
    if decimales:
        entier = nombre[:decimales.start()].replace(",", "")
        return float(f"{entier}.{decimales.group(1)}")
    return float(nombre.replace(",", "").replace(".", ""))


def _premier(carte, selecteur):
    trouves = carte.find_elements(By.CSS_SELECTOR, selecteur)
    return trouves[0] if trouves else None


def _texte(element):
    return (element.get_attribute("textContent") or "").strip() if element else ""


def extraire_produits(driver, categorie="", sous_categorie=""):
    produits = []
    for carte in driver.find_elements(By.CSS_SELECTOR, SEL_CARTE):
        asin = carte.get_attribute("data-asin")
        if not asin:
            continue
        titre = _texte(_premier(carte, SEL_TITRE))
        lien = _premier(carte, SEL_LIEN)
        href = lien.get_attribute("href") if lien else ""
        if not titre or not href:
            continue
        image = _premier(carte, SEL_IMAGE)
        produits.append(Produit(
            asin=asin,
            titre=titre,
            prix=convertir_prix(_texte(_premier(carte, SEL_PRIX))),
            image_url=(image.get_attribute("src") or "") if image else "",
            url=urljoin(AMAZON_URL, href),
            categorie=categorie,
            sous_categorie=sous_categorie,
        ))
    return produits