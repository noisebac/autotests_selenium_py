# https://stepik.org/lesson/228249/step/3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    url = "https://suninjuly.github.io/selects1.html"
    browser.get(url)
    print(f"Страница открыта: {url}")
    time.sleep(1)

    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    total = num1 + num2
    
    print(f"Найдены числа: {num1} и {num2}")
    print(f"Их сумма: {total}")

    select_element = browser.find_element(By.ID, "dropdown")
    select = Select(select_element)
    
    select.select_by_value(str(total))
    print(f"В списке выбран пункт со значением {total}")

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