from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import HEADLESS, USER_AGENT


def creer_driver():
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--lang=en-US")
    options.add_argument(f"--user-agent={USER_AGENT}")
    return webdriver.Chrome(options=options)