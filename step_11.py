from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)   
   
    
    browser.find_element(By.XPATH, "//div[1]/div[1]/input").send_keys('first')
    browser.find_element(By.XPATH, "//div[1]/div[2]/input").send_keys('last')
    browser.find_element(By.XPATH, "//div[1]/div[3]/input").send_keys('mail@mail.ru')
    browser.find_element(By.XPATH, "//div/form/div[2]/div[1]/input").send_keys('89001234567')
    browser.find_element(By.XPATH, "//div/form/div[2]/div[2]/input").send_keys('address') 


    browser.find_element(By.CSS_SELECTOR, "button.btn").click() 
 
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()