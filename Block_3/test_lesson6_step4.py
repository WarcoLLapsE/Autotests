from selenium.webdriver.common.by import By

link = 'https://stepik.org/lesson/236895/step/1'


def test_stepic_authorization(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#ember453").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys('ilpert2@yandex.ru')
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys('Parol121')
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()
