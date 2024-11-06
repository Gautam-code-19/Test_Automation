def checkout_step_1(browser,By,time,logging,first_name, last_name, street_address, city, zip_code, state, phone_number, email):
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
        logging.info("Step 1 of the form filled successfully 👍")
        time.sleep(3)
        next_step_button.click()
        logging.info("Next step button clicked 👍")
    except Exception as e:
        logging.error( "Failed to fill the fields...🩻",e)