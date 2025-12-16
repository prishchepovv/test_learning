import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import pytest
from selenium import webdriver
from qa_framework.driver import create_driver
from qa_framework.config import BASE_URL
from pages.main_page import MainPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    return page