import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome browser
browser = webdriver.Firefox()
browser.maximize_window()
logging.info("---- Window maxed ----")
browser.get("https://www.pamos.com/nationwide/")
logging.info("Login title :-- %s", browser.title)


def age_and_email_pop_up():

    # Age verification pop-up
    try:
        # Wait for the age verification pop-up to appear and click the button
        WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="age-gate"]/div/div'))
        )
        logging.info("Age Pop-up is there.")
        age_button = browser.find_element(By.XPATH, '//*[@id="age-gate"]/div/div/div/div/div[2]/div[1]/button')
        age_button.click()
        logging.info("Closed age verification pop-up ✅.")
    except Exception as e:
        logging.error("An error occurred while handling the age verification pop-up: %s", e)


    # Closing the email 20% off pop-up
    try:
        WebDriverWait(browser, 17).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="newsletter-form"]/div/div')))
        logging.info("Email pop-up is opened.")
        mail_pop_up = browser.find_element(By.XPATH, '//*[@id="newsletter-form"]/div/div/div[1]/div/button')
        WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="newsletter-form"]/div/div/div[1]/div/button')))
        time.sleep(2)
        mail_pop_up.click()
        logging.info("Email-pop is closed successfully ✅.")
        WebDriverWait(browser, 5).until(ec.invisibility_of_element((By.XPATH, '//*[@id="newsletter-form"]/div/div')))
    except Exception as e:
        logging.error("An error occurred while closing the email pop-up: %s", e)






def add_to_cart():
    time.sleep(2)
    # Accessing the Cart
    try:
        product = browser.find_element(By.XPATH,'//*[@id="allTab"]/div/div[1]/div/a[2]/p')
        browser.execute_script("arguments[0].scrollIntoView();", product)
        WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="allTab"]/div/div[1]/div/div/a')))
        cart_button = browser.find_element(By.XPATH, '//*[@id="allTab"]/div/div[1]/div/div/a')
        time.sleep(2)
        cart_button.click()
        logging.info("Cart button clicked.")
        WebDriverWait(browser, 20).until(ec.title_contains("Cart - Pamos"))
        logging.info("Cart page title: %s", browser.title)
        subtotal_amount = browser.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td/span/bdi')
        logging.info("Cart Amount is:--", subtotal_amount.text)
    except Exception as e:
        logging.error(e, "Failed to access the Cart page:", )


def checkout_start():
    time.sleep(2)
    try:
        checkout = browser.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/a')
        WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/a')))
        checkout.click()
        logging.info('Checkout Button clicked 😊')

    except Exception as e:
        logging.error(e, "failed to find the button...")

def checkout_step_1(first_name, last_name, street_address, city, zip_code, state, phone_number, email):
    # Filling the first step of checkout
    time.sleep(2)

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

        # Sending the passed arguments to each field
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        time.sleep(1)
        street_address_field.send_keys(street_address)
        city_field.send_keys(city)
        time.sleep(1)

        zip_code_field.send_keys(zip_code)
        state_field.select_by_value(state)
        time.sleep(1)

        phone_number_field.send_keys(phone_number)
        email_field.send_keys(email)
        logging.info("All fields filled successfully 👍")
        time.sleep(1)
        next_step_button.click()
        logging.info("Next step button clicked 👍")

    except Exception as e:
        logging.error(e, "Failed to fill the fields...")


def checkout_step_2():
    time.sleep(2)
    order_review = browser.find_element(By.XPATH, '//*[@id="thwmscf-tab-panel-2"]/table')
    print(order_review)

# calling all the function as we needed

age_and_email_pop_up()    #call the pop funtion
add_to_cart()
checkout_start()
checkout_step_1(first_name = "Ram",
                last_name = "Ji",
                street_address="Village Mohali",
                city="Los Angeles",
                zip_code="82834",
                state="Wyoming",
                phone_number="3456789045",
                email="gautamtechmarocs@gmail.com")

checkout_step_2()



logging.info("Browser is closed")
# browser.quit()
