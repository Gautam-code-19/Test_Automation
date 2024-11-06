def checkout_start(browser,time,WebDriverWait,ec,By,logging):
    time.sleep(1)
    try:
        checkout = browser.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/a')
        WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/a')))
        checkout.click()
        logging.info('Checkout Button clicked 😊')
    except Exception as e:
        logging.error( "failed to find the button...🩻",e)