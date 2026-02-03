from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class InventoryPage(BasePage):
    # Локаторы
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/inventory.html"

    @allure.step("Проверить, что страница инвентаря загружена")
    def is_page_loaded(self):
        self.check_current_url(self.url)
        assert self.is_element_present(self.PRODUCTS_TITLE), "Заголовок продуктов не найден"
        assert self.is_element_present(self.SHOPPING_CART), "Корзина не найдена"
        return True

    @allure.step("Получить заголовок страницы")
    def get_page_title(self):
        title_element = self.find_visible_element(self.PRODUCTS_TITLE)
        return title_element.text

    @allure.step("Выйти из системы")
    def logout(self):
        menu_button = self.find_clickable_element(self.MENU_BUTTON)
        menu_button.click()

        logout_link = self.find_clickable_element(self.LOGOUT_LINK)
        logout_link.click()

        from .login_page import LoginPage
        return LoginPage(self.driver)