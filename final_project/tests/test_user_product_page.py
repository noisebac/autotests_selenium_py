# https://stepik.org/lesson/201964/step/12 — группировка тестов: setup
# https://stepik.org/lesson/201964/step/13 — задание: группировка тестов и setup
import time

import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestUserAddToBasketFromProductPage:
    """Тесты для залогиненного пользователя: регистрация выполняется один раз в setup."""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Setup: регистрируем нового пользователя и логинимся."""
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "Qwerty123"
        login_page.browser.find_element("#id_registration-email").send_keys(email)
        login_page.browser.find_element("#id_registration-password1").send_keys(password)
        login_page.browser.find_element("#id_registration-password2").send_keys(password)
        login_page.browser.find_element("#register_form button").click()
        # Проверяем, что регистрация прошла успешно
        assert login_page.is_element_present(".alert-success"), \
            "Сообщение об успешной регистрации не появилось"

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        """Залогиненный пользователь может добавить товар в корзину."""
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        page.should_be_product_name_in_success_message()
        page.should_be_basket_total()

    def test_user_cant_see_success_message(self, browser):
        """Залогиненный пользователь не видит сообщение об успехе до добавления."""
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
