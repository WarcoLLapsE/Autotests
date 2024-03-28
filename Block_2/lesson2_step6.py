import math
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
find_x = browser.find_element(By.ID, "input_value").text
y = calc(int(find_x))
browser.execute_script("window.scrollBy(0, 100);")
browser.find_element(By.ID, "answer").send_keys(y)
find_checkbox = browser.find_element(By.ID, "robotCheckbox")
find_checkbox.click()
find_radio = browser.find_element(By.ID, "robotsRule")
find_radio.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
browser.quit()
