#https://stepik.org/lesson/237240/step/10
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Добавляет возможность указывать язык в командной строке."""
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help="Choose language: ru, en, fr, es, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для запуска браузера с указанным языком."""
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")

    # Настраиваем опции Chrome для нужного языка
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )

    # Создаем экземпляр браузера
    browser = webdriver.Chrome(options=options)

    # Возвращаем браузер в тест
    yield browser

    # Закрываем браузер после теста
    browser.quit()
