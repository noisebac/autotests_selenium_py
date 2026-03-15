
#https://stepik.org/lesson/237240/step/10
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    """Тест проверяет, что на странице есть кнопка добавления в корзину."""
    # Открываем страницу
    browser.get(link)

    # Небольшая пауза для визуальной проверки языка интерфейса
    # (будет удалена после рецензирования)
    time.sleep(30)

    # Ищем кнопку добавления в корзину по уникальному селектору
    # Селектор взят из реальной верстки страницы
    add_to_basket_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )

    # Проверяем, что кнопка найдена и отображается
    assert add_to_basket_button.is_displayed(), \
        "Кнопка добавления в корзину не найдена на странице"