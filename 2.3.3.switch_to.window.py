from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    optoin1 = browser.find_element(By.CLASS_NAME, 'btn-primary').click()

    new_window = browser.window_handles[1] #ищем новую вкладку

    browser.switch_to.window(new_window) #переходим на новую вкладку

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer').send_keys(y)

    option2 = browser.find_element(By.CLASS_NAME, "btn-primary").click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла