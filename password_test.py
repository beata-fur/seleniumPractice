# encoding: utf-8
'''
Scenariusz testowy:
Rejestracja na stronie https://www.vinted.pl/

Warunki wstepne:
Przeglądarka otwarta na stronie https://www.vinted.pl/

Przypadek testowy:
Błędne hasło (brak obecności cyfry)

Kroki:

1. Zaakceptuj zgodę cookies
2. Kliknij "Zarejestruj się".
3. Kliknij "Zarejestruj się" w nowym oknie.
4. Wprowadź prawidłowe imię i nazwisko.
5. Podaj prawidłową nazwę profilu.
6. Wpisz prawidłowy adres e-mail.
7. Wpisz nieprawidłowe hasło.
8. Kliknij "Rejestracja".

Oczekiwany rezultat:
1. Użytkownik dostaje błąd pod miejscem na wpisanie danych na czerwono:
"hasło musi zawierać co najmniej jedną cyfrę".
2. Po kliknięciu "Rejestracja" użytkownik widzi błąd w powiadomieniu
nad formularzem: "hasło musi zawierać co najmniej jedną cyfrę".
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_utils import accept_cookies
from test_utils import go_to_register_form
from test_constants import SIGN_FORM_NAME_INPUT, SIGN_FORM_LOGIN_INPUT, VALID_NAME, \
    VALID_USER_NICK, SIGN_FORM_EMAIL_INPUT, VALID_EMAIL, SIGN_FORM_PASSWORD_INPUT,\
    INVALID_PASSWORD, SIGN_FORM_REGISTER_BTN, SIGN_FORM_INPUT_ERROR_HINT, SIGN_FORM_ERROR_MSG

class VintedRegistration(unittest.TestCase):
    """
    Password test class
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.vinted.pl/")

    def test_wrong_password(self):
        """
        Test invalid password
        """
        driver = self.driver
        accept_cookies(driver)
        go_to_register_form(driver)

        name_field = driver.find_element_by_id(SIGN_FORM_NAME_INPUT)
        name_field.send_keys(VALID_NAME)

        user_nick_field = driver.find_element_by_id(SIGN_FORM_LOGIN_INPUT)
        user_nick_field.send_keys(VALID_USER_NICK)

        email_field = driver.find_element_by_id(SIGN_FORM_EMAIL_INPUT)
        email_field.send_keys(VALID_EMAIL)

        password_field = driver.find_element_by_id(SIGN_FORM_PASSWORD_INPUT)
        password_field.send_keys(INVALID_PASSWORD)

        registration_btt = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, SIGN_FORM_REGISTER_BTN)))

        ### TEST ###
        error = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, SIGN_FORM_INPUT_ERROR_HINT)))

        assert error.text == "hasło musi zawierać co najmniej jedną cyfrę"

        registration_btt.click()

        error_list = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, SIGN_FORM_ERROR_MSG)))
        items = error_list.find_elements_by_tag_name("li")

        assert len(items) == 1
        assert items[0].text == "hasło musi zawierać co najmniej jedną cyfrę"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
