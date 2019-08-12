from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time, sys

display = Display(visible=0, size=(800, 800))
display.start()
# input your own information
USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
browser = webdriver.Chrome()
browser.get("http:/github.com/new")

username_input = browser.find_element_by_id('login_field')
username_input.send_keys(USERNAME)
password = browser.find_element_by_id('password')
password.send_keys(PASSWORD)
signin_button = browser.find_element_by_name('commit')
signin_button.click()

name = browser.find_element_by_id('repository_name')
name.send_keys(sys.argv[3])
name.submit()

setup_url = browser.find_element_by_id('empty-setup-clone-url')
print(setup_url.get_attribute('value'))

browser.quit()
display.stop()