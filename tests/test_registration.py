import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize("email, username, password",
                         [("test1@yandex.ru", "test1", "QAZXSWED123"),
                          ("test2@google.ru", "test2", "Qsdfsdf456"),
                          ("test3@example.ru", "test23", "QAgsdfg789")],
                         ids=["Registration user 1", "Registration user 2", "Registration user 3"])
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, email: str,
                                 username: str, password: str):
    # Arrage
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # Act
    registration_page.fill_registartion_form(email, username, password)
    registration_page.click_registration_button()
    # Assert
    dashboard_page.check_dashboard_title_visible()
