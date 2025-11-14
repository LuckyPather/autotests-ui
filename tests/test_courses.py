import pytest

from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state:Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    page = chromium_page_with_state
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
