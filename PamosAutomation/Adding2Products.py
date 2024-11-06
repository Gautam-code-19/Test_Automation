import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


#from PamosCheckoutProcess import open_browser


browser = webdriver.Chrome()


# for further user
def open_browser1(url):
    browser.maximize_window()
    logging.info("---- Window maxed ----")
    browser.get(url)
    logging.info("Login title :-- %s", browser.title)

open_browser1(url='https://qa10624.pamos.com/nationwide/')