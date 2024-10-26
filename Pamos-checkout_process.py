import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome browser
browser = webdriver.Chrome()
browser.maximize_window()
logging.info("---- Window maxed ----")
browser.get("https://qa10624.pamos.com/")
logging.info("Login title :-- %s", browser.title)

# Age verification pop-up
try:
    # Wait for the age verification pop-up to appear and click the button
    WebDriverWait(browser, 10).until(
        ec.visibility_of_element_located((By.XPATH, '//*[@id="age-gate"]/div/div'))
    )
    logging.info("Pop is there")
    Age_button = browser.find_element(By.XPATH, '//*[@id="age-gate"]/div/div/div/div/div[2]/div[1]/button')
    Age_button.click()
    logging.info("Closed age verification pop-up.")
except Exception as e:
    logging.error("An error occurred while handling the age verification pop-up: %s", e)

# Closing the email 20% off pop-up
try:
    WebDriverWait(browser, 17).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="newsletter-form"]/div/div')))
    logging.info("Email pop-up is opened.")
    CloseEmail_pop_up = browser.find_element(By.XPATH, '//*[@id="newsletter-form"]/div/div/div[1]/div/button')
    CloseEmail_pop_up.click()
    logging.info("Email-pop is closed successfully.")
except Exception as e:
    logging.error("Not able to click on the email offer pop-up: %s", e)

# Navigating to 'Order Online'
try:
    order_online = browser.find_element(By.XPATH, '//*[@id="menu-item-938"]/a')
    order_online.click()
    logging.info("Navigated to Order Online page.")
except Exception as e:
    logging.error("Failed to click on Order Online: %s", e)

# Accessing the Cart
try:
    CartButton = browser.find_element(By.CSS_SELECTOR, '#allTab > div > div:nth-child(1) > div > div > a')
    browser.execute_script("arguments[0].scrollIntoView();", CartButton)
    time.sleep(2)  # Consider replacing this with an explicit wait
    CartButton.click()
    logging.info("Cart button clicked.")
    
    WebDriverWait(browser, 20).until(ec.title_contains("Cart - Pamos"))
    logging.info("Cart page title: %s", browser.title)
    
    SubtotalAmount = browser.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td/span/bdi')
    logging.info("Cart Amount is: %s", SubtotalAmount.text)
except Exception as e:
    logging.error(e, "Failed to access the Cart page:", )

logging.info("Browser is closed")
browser.quit()
