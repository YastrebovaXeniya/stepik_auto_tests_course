from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    browser.execute_script("window.scrollBy(0, 100);") #пролистываем страницу вниз

    input1 = browser.find_element(By.ID, 'answer').send_keys(y)

    option1 = browser.find_element(By.ID, 'robotCheckbox').click()

    option2 = browser.find_element(By.ID, 'robotsRule').click()

    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла