# Финальный проект курса: автотесты магазина (Page Object Model)

Итоговый тестовый проект курса Stepik
[«Автоматизация тестирования с помощью Selenium и Python»](https://stepik.org/course/575)
(урок [4.3 «Улучшаем дизайн тестов», финальное задание](https://stepik.org/lesson/201964/step/15)).

Тесты проверяют интернет-магазин [selenium1py.pythonanywhere.com](http://selenium1py.pythonanywhere.com/)
с помощью Python + Selenium + PyTest.

## Структура проекта

```
final_project/
├── conftest.py            # фикстура browser (Chrome)
├── pytest.ini             # маркеры и настройки запуска
├── requirements.txt       # зависимости
├── pages/                 # Page Object
│   ├── base_page.py       # базовый класс: ожидания, отрицательные проверки
│   ├── locators.py        # локаторы по страницам
│   ├── main_page.py       # главная страница
│   ├── login_page.py      # страница логина/регистрации
│   ├── product_page.py    # страница товара: добавление в корзину, промо
│   └── basket_page.py     # корзина
└── tests/                 # тесты
    ├── test_main_page.py          # логин-ссылка, пустая корзина с главной
    ├── test_product_page.py       # добавление в корзину, параметризация, негативные проверки
    └── test_user_product_page.py  # тесты для залогиненного пользователя (setup)
```

## Какие приёмы курса применены

| Приём | Где в коде | Шаг курса |
|---|---|---|
| Page Object Model | `pages/` — каждая страница своим классом | 4.1–4.2 |
| Наследование: `MainPage`, `LoginPage`, `ProductPage`, `BasketPage` наследуют `BasePage` | `pages/*.py` | 4.3, шаги 7–9 |
| Независимость от данных: `pytest.mark.parametrize` по 10 промо-ссылкам | `tests/test_product_page.py` | 4.3, шаг 3 |
| Независимость от контента: имя товара и цена берутся со страницы, не захардкожены | `ProductPage.should_be_product_name_in_success_message` | 4.3, шаг 4 |
| Отрицательные проверки: `is_not_element_present`, `is_element_disappeared` | `pages/base_page.py`, тесты `test_guest_cant_see_success_message_*` | 4.3, шаги 5–6 |
| Группировка тестов: класс `TestUserAddToBasketFromProductPage` + `setup`-фикстура (`autouse=True`) | `tests/test_user_product_page.py` | 4.3, шаги 11–13 |
| Известный баг: промо `offer6` помечен `xfail` | `tests/test_product_page.py` | 4.3, шаг 4 |

## Как запустить

```bash
pip install -r requirements.txt
pytest tests/                      # все тесты
pytest tests/ -m need_review       # только критичные тесты перед отправкой
pytest tests/test_product_page.py -k offer0   # один конкретный тест
```

Нужен установленный Google Chrome. Данные пользователя для регистрации
генерируются в `setup` (случайный email), тесты не зависят от состояния магазина
между запусками.

## Ссылки на задания курса

- 2.1–2.4 — задачи модуля 2: см. [`module2/`](../module2)
- 3.6 — параметризация и фикстуры PyTest: см. [`3_6_10/`](../3_6_10)
- 4.1–4.3 — Page Object, отрицательные проверки, наследование, setup: этот проект
