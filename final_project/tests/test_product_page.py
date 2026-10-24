# https://stepik.org/lesson/201964/step/2 — добавление в корзину со страницы товара
# https://stepik.org/lesson/201964/step/3 — независимость от данных
# https://stepik.org/lesson/201964/step/4 — независимость от контента, ищем баг
# https://stepik.org/lesson/201964/step/6 — отрицательные проверки
# https://stepik.org/lesson/201964/step/9 — наследование
# https://stepik.org/lesson/201964/step/12 — setup
import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage

# Независимость от данных: параметризация ссылок.
# offer0 — рабочая промо-ссылка, offer6 — известный сломанный промо (баг на сервере).
links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        marks=pytest.mark.xfail(reason="известный баг промо на сервере"),
    ),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
]


@pytest.mark.need_review
@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_cart(browser, link):
    """Гость может добавить товар в корзину с промо-страницы товара."""
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    # Имя и сумма берутся со страницы — проверка не зависит от контента
    page.should_be_product_name_in_success_message()
    page.should_be_basket_total()


@pytest.mark.need_review
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    """Сообщение об успехе отсутствует сразу после добавления (отрицательная проверка)."""
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message_before_adding_product_to_cart(browser):
    """Сообщение об успехе отсутствует, пока товар не добавили (отрицательная проверка)."""
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    """На странице товара есть ссылка на логин."""
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Гость может перейти на страницу логина со страницы товара (наследование BasePage)."""
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Корзина пуста, если гость открыл её со страницы товара."""
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.go_to_basket()
    from pages.basket_page import BasketPage
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_message()
