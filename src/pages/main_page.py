from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):

    HEADER = (By.TAG_NAME, "h1")
    WANT_TO_TRANSPORT_BTN = (
        By.CSS_SELECTOR, "a[href*='/hochu-perevozit']"
    )

    def is_page_loaded(self):
        return self.wait_visible(self.HEADER)

    def get_header_text(self):
        return self.wait_visible(self.HEADER).text

    def click_want_to_transport(self):
        self.click(self.WANT_TO_TRANSPORT_BTN)