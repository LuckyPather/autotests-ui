import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser_chrome = playwright.chromium.launch(headless=False)
    context = browser_chrome.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Arrage - подготовка локаторов
    locators = {"email": "registration-form-email-input",
                "username": "registration-form-username-input",
                "password": "registration-form-password-input",
                "registration_button": "registration-page-registration-button",
                "title_dashboard": "dashboard-toolbar-title-text"
                }

    page.get_by_test_id(locators["email"]).locator("input").fill("user.name@gmail.com")
    page.get_by_test_id(locators["username"]).locator("input").fill("username")
    page.get_by_test_id(locators["password"]).locator("input").fill("password")

    page.get_by_test_id(locators["registration_button"]).click()

    context.storage_state(
        path=r"C:\Users\redpr\OneDrive\Desktop\Курсы\Playwright\autotests-ui\tests\browser-state.json")

    context.close()
    browser_chrome.close()


@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser_chrome = playwright.chromium.launch(headless=False)
    context = browser_chrome.new_context(
        storage_state=r"C:\Users\redpr\OneDrive\Desktop\Курсы\Playwright\autotests-ui\tests\browser-state.json")
    page = context.new_page()

    yield page

    context.close()
    browser_chrome.close()
