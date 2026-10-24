# https://stepik.org/lesson/199980 — пишем первые тесты с помощью Page Object
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Страница логина/регистрации."""

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            f"URL не содержит 'login': {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Форма логина не представлена"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Форма регистрации не представлена"
