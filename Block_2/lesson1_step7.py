from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
find_x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
y = calc(find_x)
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
