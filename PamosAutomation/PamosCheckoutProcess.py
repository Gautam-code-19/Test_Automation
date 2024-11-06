import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from PamosAutomation.Order_details import order_details
from PlaceOrder import final_checkout
from StepForm2nd import checkout_step_2
from StepOneForm import checkout_step_1
from closePopUps import age_and_email_pop_up
from AddinngProductInCart import add_to_cart
from StartCheckout import checkout_start

# Set up logging:-
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome browser:-
browser = webdriver.Chrome()

# for further user
def open_browser(url):
    browser.maximize_window()
    logging.info("---- Window maxed ----")
    browser.get(url)
    logging.info("Login title :-- %s", browser.title)

# calling all the function as we needed:-
try:
    open_browser(url='https://qa10624.pamos.com/nationwide/')

    age_and_email_pop_up(browser,time,By,logging,WebDriverWait,ec)    #call the pop function

    add_to_cart(browser,time,By,logging, WebDriverWait, ec)

    checkout_start(browser,time,WebDriverWait,ec,By,logging)

    # fill billing details:-
    checkout_step_1(browser,By,time,logging,
                    first_name = "Gautam",
                    last_name = "Jaswal",
                    street_address= "Village Mohali",
                    city= "Los Angeles",
                    zip_code= 82005,
                    state= "Wyoming",
                    phone_number= 3456789045,
                    email= "gautamtechmarocs@gmail.com")

    checkout_step_2(browser,time,By,logging)

    # function for payment:-
    final_checkout(browser,time,By,logging,WebDriverWait , ec,
                   tc_card_number = 4111111111111111,
                   tc_card_month = "Dec",
                   tc_card_year = "2034",
                   tc_card_cvv = 1234 )

    # order details:-
    order_details(browser,WebDriverWait,logging,ec,By)

finally:
    time.sleep(1)
    logging.info("Browser is closed")
    browser.quit()