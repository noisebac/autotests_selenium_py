# https://stepik.org/lesson/184253/step/4
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    url = "http://suninjuly.github.io/alert_accept.html"
    browser.get(url)
    print(f"Страница открыта: {url}")
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print("Кнопка нажата")
    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm_text = confirm.text
    print(f"Текст confirm: {confirm_text}")
    confirm.accept()
    print("Confirm принят (нажато OK)")
    time.sleep(1)

    print(f"Перешли на новую страницу: {browser.current_url}")
    print(f"Заголовок страницы: {browser.title}")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Найдено значение x: {x}")

    y = calc(x)
    print(f"Результат вычислений (y): {y}")

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    print("Ответ введен в поле")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    print("Кнопка 'Submit' нажата")

    time.sleep(2)

    alert = browser.switch_to.alert
    alert_text = alert.text
    print("\n" + "=" * 50)
    print(f"РЕЗУЛЬТАТ (код из alert): {alert_text}")
    print("=" * 50)

    import re
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", alert_text)
    if numbers:
        final_answer = numbers[0]
        print(f"Числовой ответ для отправки: {final_answer}")

finally:
    time.sleep(3)
    browser.quit()
    print("Браузер закрыт")