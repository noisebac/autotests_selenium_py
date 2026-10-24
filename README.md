# autotests_selenium_py

Решения задач курса Stepik [«Автоматизация тестирования с помощью Selenium и Python»](https://stepik.org/course/575) на Python + Selenium.

## Структура

### `module2/` — задачи модуля 2 «Полезные методы Selenium»

| Файл | Урок |
|---|---|
| `test_2_1_5.py` | [2.1 Основные методы Selenium, шаг 5](https://stepik.org/lesson/165493/step/5) |
| `test_2_1_7.py` | [2.1 Основные методы Selenium, шаг 7](https://stepik.org/lesson/165493/step/7) |
| `test_2_2_3.py` | [2.2 Работа с файлами, списками и js-скриптами, шаг 3](https://stepik.org/lesson/228249/step/3) |
| `test_2_2_6.py` | [2.2 Работа с файлами, списками и js-скриптами, шаг 6](https://stepik.org/lesson/228249/step/6) |
| `test_2_2_8.py` | [2.2 Работа с файлами, списками и js-скриптами, шаг 8](https://stepik.org/lesson/228249/step/8) |
| `test_2_3_4.py` | [2.3 Работа с окнами, шаг 4](https://stepik.org/lesson/184253/step/4) |
| `test_2_3_6.py` | [2.3 Работа с окнами, шаг 6](https://stepik.org/lesson/184253/step/6) |
| `test_2_4_8.py` | [2.4 Настройка ожиданий, шаг 8](https://stepik.org/lesson/181384/step/8) |

Каждый файл в первой строке содержит ссылку на соответствующий шаг курса.

### `3_6_10/` — задача по PyTest (параметризация и фикстуры)

- `conftest.py` — фикстуры (запуск браузера, параметризация)
- `test_items.py` — тест с параметризацией

## Как запустить

```bash
pip install selenium
python module2/test_2_1_5.py
```

Задачи модуля 2 — самостоятельные скрипты: открывают страницу, выполняют шаги задания и печатают результат в консоль. Для работы нужен установленный Chrome и ChromeDriver.
