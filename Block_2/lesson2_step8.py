import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
first_name.send_keys('Boris')
last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
last_name.send_keys('Razor')
email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
email.send_keys('BoryaRazor@mail.ru')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "xuy.txt")
load_file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
load_file_button.send_keys(file_path)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
browser.quit()
