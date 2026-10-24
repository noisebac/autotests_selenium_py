# https://stepik.org/lesson/181384/step/8
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    print("Страница загружена")

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    print("Цена достигла $100! Бронируем...")

    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    print("Кнопка 'Book' нажата")
    time.sleep(1)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Найдено значение x: {x}")

    y = calc(x)
    print(f"Результат вычислений: {y}")

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    print("Ответ введен")

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    print("Кнопка 'Submit' нажата")

    time.sleep(2)

    alert = browser.switch_to.alert
    alert_text = alert.text
    print("\n" + "=" * 50)
    print(f"РЕЗУЛЬТАТ: {alert_text}")
    print("=" * 50)

    import re
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", alert_text)
    if numbers:
        final_answer = numbers[0]
        print(f"КОД ДЛЯ ОТПРАВКИ: {final_answer}")

finally:
    time.sleep(3)
    browser.quit()
    print("Браузер закрыт")