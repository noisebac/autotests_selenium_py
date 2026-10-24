# https://stepik.org/lesson/228249/step/8
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    url = "http://suninjuly.github.io/file_input.html"
    browser.get(url)
    print(f"Страница открыта: {url}")
    time.sleep(1)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")
    print("Имя заполнено: Ivan")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")
    print("Фамилия заполнена: Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan.petrov@example.com")
    print("Email заполнен: ivan.petrov@example.com")

    file_name = "test_file.txt"
    file_path = os.path.join(os.getcwd(), file_name)
    
    with open(file_path, "w") as file:
        file.write("Это тестовый файл для загрузки")
    
    print(f"Создан файл: {file_path}")
    
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)
    print("Файл загружен")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
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
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Временный файл удален: {file_name}")
    
    time.sleep(3)
    browser.quit()
    print("Браузер закрыт")