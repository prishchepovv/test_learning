import sys
import os
import allure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import pytest
from qa_framework.driver import create_driver
from qa_framework.config import BASE_URL
from pages.main_page import MainPage

@pytest.fixture(scope="session")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Только если тест упал
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )