from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser_chrome = playwright.chromium.launch(headless=False)
    page = browser_chrome.new_page()

    # Arrage - подготовка локаторов, переход на страницу
    locators = {"email": "registration-form-email-input",
                "username": "registration-form-username-input",
                "password": "registration-form-password-input",
                "registration_button": "registration-page-registration-button"
                }

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Act
    expect(page.get_by_test_id(locators["registration_button"])).not_to_be_enabled()
    page.get_by_test_id(locators["email"]).locator("input").fill("user.name@gmail.com")
    page.get_by_test_id(locators["username"]).locator("input").fill("username")
    page.get_by_test_id(locators["password"]).locator("input").fill("password")

    # Assert
    expect(page.get_by_test_id(locators["registration_button"])).to_be_enabled()