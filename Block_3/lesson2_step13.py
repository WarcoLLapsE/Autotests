from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class NewTestClass(unittest.TestCase):
    def template(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        self.input1 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        self.input1.send_keys('Jopka')
        self.input2 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        self.input2.send_keys('Pipka')
        self.input3 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        self.input3.send_keys('jopa@pipkina.by')
        self.button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()
        time.sleep(1)
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual(self.welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(5)
        self.browser.quit()

    def test_registration_1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.template()

    def test_registration_2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.template()


if __name__ == "__main__":
    unittest.main()