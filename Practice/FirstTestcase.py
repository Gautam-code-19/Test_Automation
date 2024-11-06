from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser= webdriver.Firefox()

browser.maximize_window()
browser.get("https://dev.letsmakeinvoice.com/")
title = browser.title
print(title, "Before login the user.")
# title captured

assert "Invoice Generator - LetsMakeInvoice | Business Invoicing with Taxes" in title

# targeting the login button
Login_button = browser.find_element(By.XPATH, "//button[text()='Login / SignUp']")
Login_button.click()

# targeting the email
email = browser.find_element(By.NAME, 'email')
email.send_keys('gautamsinghji2002@gmail.com')


# targeting the password field
password = browser.find_element(By.NAME, 'password')
password.send_keys('12345678@aA')

Form_Login = browser.find_element(By.XPATH, "//button[@type='submit']")
Form_Login.click()

Login_title = "Invoice Generator - Let's Make Invoice | Business Invoicing with Taxes"
WebDriverWait(browser, 10).until(ec.title_is(Login_title))

if browser.title == Login_title:
    Logout_button = WebDriverWait(browser, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, '.fa-arrow-right-from-bracket'))
    )

    Logout_button.click()
    Confirm_logout = WebDriverWait(browser, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[text()='Yes']"))
    )
    Confirm_logout.click()
    print("Logout Done")
else:
    print("failed to logout")