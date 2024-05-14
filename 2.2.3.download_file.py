from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname').send_keys("IVAN")

    input2 = browser.find_element(By.NAME, 'lastname').send_keys("IVANOV")

    input3 = browser.find_element(By.NAME, 'email').send_keys("Test@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'textov.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, 'file').send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn-primary").click()
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


