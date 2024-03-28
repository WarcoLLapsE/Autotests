from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
find_num1 = browser.find_element(By.ID, "num1").text
find_num2 = browser.find_element(By.ID, "num2").text
select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(int(find_num1) + int(find_num2)))
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
browser.quit()
