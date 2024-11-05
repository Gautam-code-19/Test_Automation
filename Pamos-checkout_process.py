import logging
import threading
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# Set up logging:-
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome browser:-
browser = webdriver.Chrome()
browser.maximize_window()
logging.info("---- Window maxed ----")
browser.get("https://qa10624.pamos.com/nationwide/")
logging.info("Login title :-- %s", browser.title)


def age_and_email_pop_up():

    # Age verification pop-up:-
    try:
        # Wait for the age verification pop-up to appear and click the button:-
        WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="age-gate"]/div/div'))
        )
        logging.info("Age Pop-up is there.")
        age_button = browser.find_element(By.XPATH, '//*[@id="age-gate"]/div/div/div/div/div[2]/div[1]/button')
        age_button.click()
        logging.info("Closed age verification pop-up ✅.")
    except Exception as e:
        logging.error("An error occurred while handling the age verification pop-up: %s", e)

    # try:
    #     WebDriverWait(browser, 17).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="newsletter-form"]/div/div')))
    #     logging.info("Email pop-up is opened.")
    #     mail_pop_up = browser.find_element(By.XPATH, '//*[@id="newsletter-form"]/div/div/div[1]/div/button')
    #     WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="newsletter-form"]/div/div/div[1]/div/button')))
    #     time.sleep(1)
    #     mail_pop_up.click()
    #     logging.info("Email-pop is closed successfully ✅.")
    #     WebDriverWait(browser, 5).until(ec.invisibility_of_element((By.XPATH, '//*[@id="newsletter-form"]/div/div')))
    # except Exception as e:
    #     logging.error("An error occurred while closing the email pop-up: %s", e)



# Closing the email 20% off pop-up:-
def close_email_popup():
    try:
        WebDriverWait(browser, 17).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="newsletter-form"]/div/div')))
        logging.info("Email pop-up is opened.")
        mail_pop_up = browser.find_element(By.XPATH, '//*[@id="newsletter-form"]/div/div/div[1]/div/button')
        WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="newsletter-form"]/div/div/div[1]/div/button')))
        time.sleep(1)
        mail_pop_up.click()
        logging.info("Email-pop is closed successfully ✅.")
        WebDriverWait(browser, 5).until(ec.invisibility_of_element((By.XPATH, '//*[@id="newsletter-form"]/div/div')))
    except Exception as e:
        logging.error("An error occurred while closing the email pop-up: %s", e)



def add_to_cart():
    time.sleep(1)
    # Accessing the Cart:-
    try:
        product = browser.find_element(By.XPATH,'//*[@id="allTab"]/div/div[1]/div/a[2]/p')
        browser.execute_script("arguments[0].scrollIntoView();", product)
        WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="allTab"]/div/div[1]/div/div/a')))
        cart_button = browser.find_element(By.XPATH, '//*[@id="allTab"]/div/div[1]/div/div/a')
        time.sleep(1)
        cart_button.click()
        logging.info("Cart button clicked.")
        WebDriverWait(browser, 20).until(ec.title_contains("Cart - Pamos"))
        logging.info("Cart page title:-", browser.title)
        subtotal_amount = browser.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td/span/bdi')
        logging.info("Cart Amount is:-", subtotal_amount.text)
    except Exception as e:
        logging.error( "Failed to access the Cart page:",e )


def checkout_start():
    time.sleep(1)
    try:
        checkout = browser.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/a')
        WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/a')))
        checkout.click()
        logging.info('Checkout Button clicked 😊')

    except Exception as e:
        logging.error( "failed to find the button...",e)

def checkout_step_1(first_name, last_name, street_address, city, zip_code, state, phone_number, email):
    # Filling the first step of checkout:-
    time.sleep(1)

    next_step_button = browser.find_element(By.XPATH, '//*[@id="action-next"]')

    first_name_field = browser.find_element(By.XPATH, '//*[@id="billing_first_name"]')
    last_name_field = browser.find_element(By.XPATH, '//*[@id="billing_last_name"]')
    street_address_field = browser.find_element(By.XPATH, '//*[@id="billing_address_1"]')
    city_field = browser.find_element(By.XPATH, '//*[@id="billing_city"]')
    zip_code_field = browser.find_element(By.XPATH, '//*[@id="billing_postcode"]')
    state_field = browser.find_element(By.XPATH, '//*[@id="billing_state"]')
    phone_number_field = browser.find_element(By.XPATH, '//*[@id="billing_phone"]')
    email_field = browser.find_element(By.XPATH, '//*[@id="billing_email"]')
    logging.info("All founded found successfully 👍")


    try:
        form_heading = browser.find_element(By.XPATH, '//*[@id="thwmscf-tab-panel-1"]/div[1]/div/h3')
        browser.execute_script("arguments[0].scrollIntoView();", form_heading)
        logging.info("Form heading found successfully")

        # Sending the passed arguments to each field:-
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        street_address_field.send_keys(street_address)
        city_field.send_keys(city)
        zip_code_field.send_keys(zip_code)

        state_field.find_elements(By.TAG_NAME, "option")
        i=0
        for option in state_field.find_elements(By.TAG_NAME, "option"):
            if option.text == state:
                browser.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
                break
            i += 1

        phone_number_field.send_keys(phone_number)
        email_field.send_keys(email)
        logging.info("All fields filled successfully 👍")
        next_step_button.click()
        logging.info("Next step button clicked 👍")

    except Exception as e:
        logging.error( "Failed to fill the fields...",e)

#chechout second step:-
def checkout_step_2():
    time.sleep(1)
    next_step_button = browser.find_element(By.XPATH, '//*[@id="action-next"]')
    order_review = browser.find_element(By.XPATH, '//*[@id="thwmscf-tab-panel-2"]/table')
    print('Table content',order_review.text)
    next_step_button.click()
    logging.info("2nd step id cleared...")


# filly card details and placing the order:-
def final_checkout(tc_card_number , tc_card_month , tc_card_year , tc_card_cvv):
    time.sleep(1)
    card_number = browser.find_element(By.XPATH,'//*[@id="bfws_ccNumber"]')
    card_month = browser.find_element(By.XPATH,'//*[@id="cc-exp-month"]')
    card_year = browser.find_element(By.XPATH,'//*[@id="cc-exp-year"]')
    card_cvv = browser.find_element(By.XPATH,'//*[@id="bfws_cvv"]')
    place_order = browser.find_element(By.XPATH, '//*[@id="place_order"]')

    try:
        card_number.send_keys(tc_card_number)
        logging.info("card number filled", card_number)
    except Exception as e:
        logging.error( "Not able to fill the card number...",e)

    try:
        card_month.find_elements(By.TAG_NAME, "option")
        i = 0
        for option in card_year.find_elements(By.TAG_NAME, "option"):
            if option.text == tc_card_month:
                browser.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
                break
            i += 1
        logging.info("card number filled", tc_card_month)
    except Exception as e:
        logging.error( "Not able to fill the card month...",e)

    try:
        card_year.find_elements(By.TAG_NAME, "option")
        i = 0
        for option in card_year.find_elements(By.TAG_NAME, "option"):
            if option.text == tc_card_year:
                browser.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
                break
            i += 1
        logging.info("card number filled", tc_card_year)
    except Exception as e:
        logging.error( "Not able to fill the card Year...",e)

    try:
        card_cvv.send_keys(tc_card_cvv)
        logging.info("card number filled", tc_card_cvv)
    except Exception as e:
        logging.error( "Not able to fill the card CVV number...",e)

    try:
        browser.execute_script("arguments[0].scrollIntoView();", place_order)
        WebDriverWait(browser, 10).until(ec.element_to_be_clickable(place_order))
        place_order.click()
        logging.info("Order Placed Successfully")
    except Exception as e:
        logging.error(e,"Failed to place order...")
    time.sleep(10)


# Fetching order details:-
def order_details():
    WebDriverWait(browser, 20).until(ec.text_to_be_present_in_element((By.XPATH, "//*[contains(text(), 'THANK YOU!')]"), "THANK YOU!"))
    try:
        order_base_details = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[2]/div/ul')))
        print(order_base_details.text)
    except Exception as e:
        logging.error( "Failed to find the order base details..." ,e)

    try:
        billing_address = browser.find_element(By.XPATH,'//*[@id="wrap"]/div[2]/div/div[2]/div[2]/section/section/div[1]/h2')
        browser.execute_script("arguments[0].scrollIntoView();", billing_address)
        address_value = browser.find_element(By.XPATH,'//*[@id="wrap"]/div[2]/div/div[2]/div[2]/section/section/div[1]/address').text
        print(address_value)
    except Exception as e:
        logging.error( "Failed to find the billing address...",e)





try:
    # calling all the function as we needed:-
    age_and_email_pop_up()    #call the pop funtion
    timer_thread = threading.Timer(14, close_email_popup)
    timer_thread.start()
    add_to_cart()
    checkout_start()

    # fill billing details:-
    checkout_step_1(first_name = "Gautam",
                    last_name = "Jaswal",
                    street_address="Village Mohali",
                    city="Los Angeles",
                    zip_code="82005",
                    state="Wyoming",
                    phone_number="3456789045",
                    email="gautamtechmarocs@gmail.com")

    checkout_step_2()

    # fill the form:-
    final_checkout(tc_card_cvv="123",
                   tc_card_year="2034",
                   tc_card_month="Dec",
                   tc_card_number="4111111111111111")

    # order details:-
    order_details()

finally:
    logging.info("Browser is closed")
    # browser.quit()
