import time
from urllib.parse import quote_plus

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from app.scraper.driver import creer_driver
from app.scraper.parsing import SEL_CARTE, extraire_produits
from config import (AMAZON_URL, DELAI_ENTRE_PAGES, DELAI_LECTURE,
                    DEPARTEMENT, TIMEOUT, pause)


class CaptchaDetecte(Exception):
    pass


class AmazonScraper:
    def scraper(self, categorie, sous_categorie, mot_cle, nb_pages):
        driver = creer_driver()
        produits = []
        try:
            for page in range(1, nb_pages + 1):
                url = f"{AMAZON_URL}/s?k={quote_plus(mot_cle)}&i={DEPARTEMENT}&page={page}"
                print(f"[{sous_categorie}] page {page}/{nb_pages}...")
                driver.get(url)
                self._verifier_captcha(driver)
                try:
                    WebDriverWait(driver, TIMEOUT).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, SEL_CARTE))
                    )
                except TimeoutException:
                    print("Aucun résultat sur cette page, arrêt.")
                    break
                time.sleep(pause(DELAI_LECTURE))
                produits += extraire_produits(driver, categorie, sous_categorie)
                if page < nb_pages:
                    time.sleep(pause(DELAI_ENTRE_PAGES))
        except CaptchaDetecte:
            print("CAPTCHA détecté : arrêt. Les produits déjà récupérés sont conservés.")
        finally:
            driver.quit()
        return produits

    @staticmethod
    def _verifier_captcha(driver):
        if driver.find_elements(By.CSS_SELECTOR, "form[action*='validateCaptcha']"):
            raise CaptchaDetecte()