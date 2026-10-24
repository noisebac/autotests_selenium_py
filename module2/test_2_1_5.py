# https://stepik.org/lesson/165493/step/5
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    url = "https://suninjuly.github.io/math.html"
    browser.get(url)
    print(f"Страница открыта: {url}")
    time.sleep(1)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Найдено значение x: {x}")

    y = calc(x)
    print(f"Результат вычислений (y): {y}")

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    print("Ответ введен в поле.")

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    print("Чекбокс 'I'm the robot' отмечен.")

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    print("Радиокнопка 'Robots rule!' выбрана.")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print("Кнопка 'Submit' нажата.")

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
    else:
        print("Не удалось извлечь число из alert.")

finally:
    time.sleep(3)
    browser.quit()
    print("Браузер закрыт.")