from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Arrage - подготовка локаторов
    locators={"email": "registration-form-email-input",
              "username": "registration-form-username-input",
              "password": "registration-form-password-input",
              "registration_button": "registration-page-registration-button",
              "title_dashboard" : "dashboard-toolbar-title-text"
    }

    # Act - заполнение формы регистрации
    page.get_by_test_id(locators["email"]).locator("input").fill("user.name@gmail.com")
    page.get_by_test_id(locators["username"]).locator("input").fill("username")
    page.get_by_test_id(locators["password"]).locator("input").fill("password")
    page.get_by_test_id(locators["registration_button"]).click()

    # Assert - проверка наличия элемента
    expect(page.get_by_test_id(locators["title_dashboard"])).to_be_visible()

