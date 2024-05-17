from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
    def test_registration_page1(self):
        browser = self.browser
        browser.get(link1)

        self.input1 = browser.find_element(By.XPATH,'//input[contains(@placeholder, "first name")]').send_keys("Ivan")
        self.input2 = browser.find_element(By.XPATH,'//input[contains(@placeholder, "last name")]').send_keys("Petrov")
        self.input3 = browser.find_element(By.XPATH,'//input[contains(@placeholder, "email")]').send_keys("Smolensk@ru")

        self.button = browser.find_element(By.CLASS_NAME, "btn-default").click()

        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!","Error massage1")

        # успеваем скопировать код за 10 секунд
        time.sleep(3)
    def test_registration_page2(self):
        browser = self.browser
        browser.get(link2)

        self.input1 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "first name")]').send_keys("Ivan")
        self.input2 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "last name")]').send_keys("Petrov")
        self.input3 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "email")]').send_keys("Smolensk@ru")

        self.button = browser.find_element(By.CLASS_NAME, "btn-default").click()

        self.assertEqual("Congratulations! You have successfully registered!","Congratulations! You have successfully registered!", "Error massage2")

        # успеваем скопировать код за 10 секунд
        time.sleep(3)
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

# не забываем оставить пустую строку в конце файла
