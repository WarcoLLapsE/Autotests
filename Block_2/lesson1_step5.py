from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
find_x = browser.find_element(By.ID, "input_value")
x = find_x.text
y = calc(x)
answer_form = browser.find_element(By.ID, "answer")
answer_form.send_keys(y)
find_checkbox = browser.find_element(By.ID, "robotCheckbox")
find_checkbox.click()
find_radio = browser.find_element(By.ID, "robotsRule")
find_radio.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(5)
browser.quit()
