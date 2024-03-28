import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/find_link_text"
to_find = str(math.ceil(math.pow(math.pi, math.e)*10000))
browser = webdriver.Chrome()
browser.get(link)
explore = browser.find_element(By.LINK_TEXT, to_find)
explore.click()
input1 = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
input1.send_keys('Jopa')
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys('Petya')
input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
input3.send_keys('Petrograd')
input4 = browser.find_element(By.ID, 'country')
input4.send_keys('BOLIVIA')
button = browser.find_element(By.XPATH, '//button')
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла