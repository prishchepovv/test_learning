from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from qa_framework.config import BROWSER

def create_driver():
    if BROWSER.lower() == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    return driver