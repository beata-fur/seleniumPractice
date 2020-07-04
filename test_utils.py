# encoding: utf-8
"""
Module with common methods used in tests
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def accept_cookies(driver):
    """
    Accept cookies method
    """
    frame = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, '//iframe[contains(@id, "sp_message_iframe_")]')))
    driver.switch_to.frame(frame)
    # print(driver.page_source)

    driver.find_element(By.XPATH, '//button[@path="[0,1,2]"]').click()

    driver.switch_to.default_content()

def go_to_register_form(driver):
    """
    Method for going to register form
    """
    #2. Kliknij "Zarejestruj się".
    driver.find_element(
        By.XPATH, '//div[@class="l-header__actions"]//span[contains(text(),"Zarejestruj")]').click()
    #3. Kliknij "Zarejestruj się" w nowym oknie.
    driver.find_element(
        By.XPATH, '//div[@class="u-flex-grow"]//span[contains(text(),"Zarejestruj")]').click()
