=====================
Selenium Practice
=====================

Development
==============

1. Setup the virtualenv or use the existing:

   - Prepare the coding environment with python3

     ::

       $ python3 -m venv .venv
       $ source .venv/bin/activate
       $ pip install -r requirements.txt

 

2. Get the firefox driver:

     ::

       wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
       tar -xvzf geckodriver*tar.gz
       chmod +x geckodriver*


How to start a test
===================
Go to project directory

::
  python3 email_test.py
  python3 password_test.py
  python3 registration_test.py
 
