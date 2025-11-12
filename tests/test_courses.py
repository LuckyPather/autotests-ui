import pytest

from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    # Arrage
    # Сохраняю данные для входа без повторной логинизации
    with sync_playwright() as playwright:
        browser_chrome = playwright.chromium.launch(headless=False)
        context = browser_chrome.new_context()
        page = context.new_page()

        locators = {"email": "registration-form-email-input",
                    "username": "registration-form-username-input",
                    "password": "registration-form-password-input",
                    "registration_button": "registration-page-registration-button"
                    }

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Act
        page.get_by_test_id(locators["email"]).locator("input").fill("user.name@gmail.com")
        page.get_by_test_id(locators["username"]).locator("input").fill("username")
        page.get_by_test_id(locators["password"]).locator("input").fill("password")

        page.get_by_test_id(locators["registration_button"]).click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser_chrome = playwright.chromium.launch(headless=False)
        context = browser_chrome.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        elements = {"title": page.get_by_test_id("courses-list-toolbar-title-text"),
                    "icon_empty_result": page.get_by_test_id("courses-list-empty-view-icon"),
                    "title_result": page.get_by_test_id("courses-list-empty-view-title-text"),
                    "message_result": page.get_by_test_id("courses-list-empty-view-description-text")
                    }

        expect(elements["title"]).to_be_visible()
        expect(elements["title"]).to_have_text("Courses")

        expect(elements["icon_empty_result"]).to_be_visible()

        expect(elements["title_result"]).to_be_visible()
        expect(elements["title_result"]).to_have_text("There is no results")

        expect(elements["message_result"]).to_be_visible()
        expect(elements["message_result"]).to_have_text("Results from the load test pipeline will be displayed here")



