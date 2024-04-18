import time
import math
from selenium.webdriver.common.by import By

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']


def calculate_answer(browser):
    final_answer = ''
    for url in links:
        browser.get(url)
        answer = math.log(int(time.time()))
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, '[class="submit-submission"]').click()
        answer_text = browser.find_element(By.CSS_SELECTOR, '[class="smart-hints__hint"]').text
        if answer_text != 'Correct!':
            final_answer += answer_text
    print(final_answer)

def test_stepic_authorization_with_links(browser):
    browser.get(links[0])
    browser.find_element(By.CSS_SELECTOR, "#ember453").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys('avolgin@niisokb.ru')
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys('P@ssw0rd')
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()
    calculate_answer(browser)