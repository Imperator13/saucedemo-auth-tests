import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")
    parser.addoption("--headless", action="store_true", default=False, help="Run in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    else:
        raise ValueError(f"Browser {browser} is not supported")

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        # Сделать скриншот при падении теста
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}.png")
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)