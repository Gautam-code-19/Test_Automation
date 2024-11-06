def add_to_cart(browser,time,By,logging,WebDriverWait,ec):
    time.sleep(1)
    # Accessing the Cart:-
    try:
        product = browser.find_element(By.XPATH,'//*[@id="allTab"]/div/div[1]/div/a[2]/p')
        browser.execute_script("arguments[0].scrollIntoView();", product)
        WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="allTab"]/div/div[1]/div/div/a')))
        cart_button = browser.find_element(By.XPATH, '//*[@id="allTab"]/div/div[1]/div/div/a')
        time.sleep(0.5)
        cart_button.click()
        logging.info("Cart button clicked.")
        WebDriverWait(browser, 20).until(ec.title_contains("Cart - Pamos"))
        subtotal_amount_table = browser.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table')
        print(subtotal_amount_table.text)
    except Exception as e:
        logging.error( "🩻 Failed to access the Cart page:",e )