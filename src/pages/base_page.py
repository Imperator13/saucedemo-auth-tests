from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить текущий URL")
    def check_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, \
            f"Ожидался URL: {expected_url}, но получен: {current_url}"
        return True