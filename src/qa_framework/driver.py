import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from qa_framework.config import BROWSER
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    if BROWSER.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")

        driver_path = ChromeDriverManager().install()

        # Фикс для WinError 193
        if not driver_path.endswith("chromedriver.exe"):
            driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")

        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        driver = webdriver.Firefox()

    return driver