# import selenium, a test automator for web applications
from selenium import webdriver

# run selenium using the chrome browser
browser = webdriver.Chrome('C:/Users/Ec/Desktop/Python/Software Dev practices/tdd_avec_python/browser/chromedriver')

# port on which to run the application
browser.get('http://localhost:8000')

# maximize window when running the app
browser.maximize_window()

# testing for the correct url
assert 'Django' in browser.title