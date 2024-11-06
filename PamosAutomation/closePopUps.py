def age_and_email_pop_up(browser,time,By,logging,WebDriverWait,ec):

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
        logging.error("🩻 An error occurred while closing the email pop-up: %s", e)
