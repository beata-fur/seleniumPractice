"""
Constants used for tests
"""
VALID_NAME = "Beata Kowalska"
INVALID_NAME = "Beat@ Kowalska"
VALID_USER_NICK = "bea796344620"
VALID_EMAIL = "horicana-2123@onet.pl"
INVALID_EMAIL = "horicana-2123yopmail.com"
VALID_PASSWORD = "t3gdMWFAtZ"
INVALID_PASSWORD = "katastrofa"

SIGN_FORM_NAME_INPUT = 'user_real_name'
SIGN_FORM_LOGIN_INPUT = 'user_login'
SIGN_FORM_EMAIL_INPUT = 'user_email'
SIGN_FORM_PASSWORD_INPUT = 'user_password'
SIGN_FORM_REGISTER_BTN = '//div[@class="c-cell__body"]//span[contains(text(),"Rejestracja")]'
SIGN_FORM_INPUT_ERROR_HINT = '//div[@class="c-input__validation c-input__validation--warning"]'
SIGN_FORM_ERROR_MSG = '//div[@class="notification__body "]//ul'
