from selenium import webdriver
from time import sleep

for i in range(100):
    browser = webdriver.Chrome()
    # browser.maximize_window()
    browser.get('https://dev.techmarcos.com/')
    sleep(2)
    browser.quit()
