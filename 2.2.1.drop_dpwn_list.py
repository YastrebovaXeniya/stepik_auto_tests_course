from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
    return str(int(x) + int(y))

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.ID, 'num1').text
    x_element2 = browser.find_element(By.ID, 'num2').text
    y = calc(x_element1, x_element2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
finally:
    time.sleep(15)
    browser.quit()

# не забываем оставить пустую строку в конце файла