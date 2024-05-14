from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Проверяем наличие обязательных полей
    required_fields = ['input.form-control.first', 'input.form-control.second', 'input.form-control.third']
    for field in required_fields:
        assert browser.find_element(By.CSS_SELECTOR, field), f"{field} is not found on the page"

    # Заполняем обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second')
    input2.send_keys("Popov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third')
    input3.send_keys("Email")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    # Проверяем успешную регистрацию
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text, "Registration failed"

finally:
    time.sleep(5)
    browser.quit()