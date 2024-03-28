import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), '$100'))
button = browser.find_element(By.ID, "book")
button.click()
find_x = browser.find_element(By.ID, 'input_value').text
answer_form = browser.find_element(By.ID, 'answer')
answer_form.send_keys(calc(find_x))
button = browser.find_element(By.ID, "solve")
button.click()
time.sleep(10)


