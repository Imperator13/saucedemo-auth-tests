from selenium.webdriver.common.by import By
from .base_page import BasePage
from .inventory_page import InventoryPage
import allure


class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(self.url)
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username):
        username_field = self.find_clickable_element(self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)
        return self

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password):
        password_field = self.find_clickable_element(self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        return self

    @allure.step("Нажать кнопку логина")
    def click_login(self):
        login_button = self.find_clickable_element(self.LOGIN_BUTTON)
        login_button.click()
        return self

    @allure.step("Выполнить логин с именем пользователя: {username} и паролем: {password}")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        if "inventory" in self.driver.current_url:
            return InventoryPage(self.driver)
        return self

    @allure.step("Получить текст ошибки")
    def get_error_message(self):
        if self.is_element_present(self.ERROR_MESSAGE):
            error_element = self.find_visible_element(self.ERROR_MESSAGE)
            return error_element.text
        return None

    @allure.step("Проверить наличие ошибки")
    def is_error_displayed(self):
        return self.is_element_present(self.ERROR_MESSAGE)