import pytest
import allure
from src.pages.login_page import LoginPage


@allure.feature("Авторизация на сайте SauceDemo")
@allure.story("Тесты авторизации")
class TestLogin:

    @allure.title("Успешный логин стандартного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, driver):
        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(driver).open()

        with allure.step("Выполнить логин с валидными данными"):
            inventory_page = login_page.login("standard_user", "secret_sauce")

        with allure.step("Проверить успешную авторизацию"):
            assert inventory_page.is_page_loaded()
            assert inventory_page.get_page_title() == "Products"
            inventory_page.check_current_url("https://www.saucedemo.com/inventory.html")

    @allure.title("Логин с неверным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_wrong_password(self, driver):
        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(driver).open()

        with allure.step("Выполнить логин с неверным паролем"):
            login_page.login("standard_user", "wrong_password")

        with allure.step("Проверить сообщение об ошибке"):
            assert login_page.is_error_displayed()
            error_text = login_page.get_error_message()
            assert "Username and password do not match" in error_text

    @allure.title("Логин заблокированного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_locked_out_user(self, driver):
        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(driver).open()

        with allure.step("Выполнить логин заблокированным пользователем"):
            login_page.login("locked_out_user", "secret_sauce")

        with allure.step("Проверить сообщение об ошибке блокировки"):
            assert login_page.is_error_displayed()
            error_text = login_page.get_error_message()
            assert "Sorry, this user has been locked out" in error_text

    @allure.title("Логин с пустыми полями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_fields(self, driver):
        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(driver).open()

        with allure.step("Нажать кнопку логина без ввода данных"):
            login_page.click_login()

        with allure.step("Проверить сообщение об ошибке"):
            assert login_page.is_error_displayed()
            error_text = login_page.get_error_message()
            assert "Username is required" in error_text

    @allure.title("Логин пользователя performance_glitch_user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_performance_glitch_user(self, driver):
        with allure.step("Открыть страницу логина"):
            login_page = LoginPage(driver).open()

        with allure.step("Выполнить логин пользователем performance_glitch_user"):
            inventory_page = login_page.login("performance_glitch_user", "secret_sauce")

        with allure.step("Проверить успешную авторизацию несмотря на возможные задержки"):
            assert inventory_page.is_page_loaded()
            assert inventory_page.get_page_title() == "Products"
            inventory_page.check_current_url("https://www.saucedemo.com/inventory.html")