import math
import time


from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
browser.switch_to.alert.accept()
find_x = browser.find_element(By.ID, 'input_value').text
answer_form = browser.find_element(By.ID, 'answer')
answer_form.send_keys(calc(find_x))
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
browser.quit()

