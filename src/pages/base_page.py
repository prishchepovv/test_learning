from qa_framework.waits import wait_visible, wait_clickable

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait_visible(self, locator):
        return wait_visible(self.driver, locator)

    def click(self, locator):
        element = wait_clickable(self.driver, locator)
        element.click()