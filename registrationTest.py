'''
Scenariusz testowy:
Rejestracja na stronie https://www.vinted.pl/

Warunki wstepne:
Przeglądarka otwarta na stronie https://www.vinted.pl/

Przypadek testowy:
Błędne imię (obecnośc znaku '@')

Kroki:

1. Zaakceptuj zgodę cookies
2. Kliknij "Zarejestruj się".
3. Kliknij "Zarejestruj się" w nowym oknie.
4. Wprowadź błędne imię i prawidłowe nazwisko.
5. Podaj nazwę profilu.
6. Wpisz prawidłowy adres e-mail.
7. Wpisz prawidłowe hasło.
8. Kliknij "Rejestracja".

Oczekiwany rezultat:
1. Uzytkownik dostaje informację na czerwono "Proszę podaj swoje imię i nazwisko"
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class vintedRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.vinted.pl/")

    def testWrongName(self):
        driver = self.driver
        
        frame = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//iframe[contains(@id, "sp_message_iframe_")]')))
        driver.switch_to.frame(frame)
        # print(driver.page_source)

        driver.find_element(By.XPATH, '//button[@path="[0,1,2]"]').click()

        driver.switch_to.default_content()
        #2. Kliknij "Zarejestruj się".
        driver.find_element(By.XPATH,'//div[@class="l-header__actions"]//span[contains(text(),"Zarejestruj")]').click()
        #3. Kliknij "Zarejestruj się" w nowym oknie.
        driver.find_element(By.XPATH,'//div[@class="u-flex-grow"]//span[contains(text(),"Zarejestruj")]').click()
        #4. Wprowadź błędne imię i prawidłowe nazwisko.
        name_field = driver.find_element_by_id('user_real_name')
        name_field.send_keys("Beat@ Kowalska")
        #5. Podaj nazwę profilu.
        user_nick_field = driver.find_element_by_id('user_login')
        user_nick_field.send_keys("bea796344620")
        #6. Wpisz prawidłowy adres e-mail.
        email_field = driver.find_element_by_id('user_email')
        email_field.send_keys("horicana-2123@yopmail.com")
        #7. Wpisz prawidłowe hasło.
        password_field = driver.find_element_by_id('user_password')
        password_field.send_keys("t3gdMWFAtZ")
        #8. Kliknij "Rejestracja".
        registration_btt = driver.find_element_by_xpath('//div[@class="c-cell__body"]//span[contains(text(),"Rejestracja")]')
        registration_btt.click()

        sleep(10)



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
