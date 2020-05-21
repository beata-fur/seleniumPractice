'''
Scenariusz testowy:
Rejestracja na stronie https://www.vinted.pl/

Warunki wstepne:
Przeglądarka otwarta na stronie https://www.vinted.pl/

Przypadek testowy:
Błędne imię (obecnośc znaku '@')

Kroki:
1. Kliknij "Zarejestruj się"
2. Kliknij "Zarejestruj się"
3. Wprowadz błędne imię i prawidłowe nazwisko
4. Podaj nazwę profilu //"796344620"
6. Wpisz prawidłowy adres e-mail // "horicana-2123@yopmail.com"
7. Wpisz prawidłowe hasło // "t3gdMWFAtZ"
8. Kliknij Zarejestruj sie

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

class vintedRegistration(unitttest.TestCase):
