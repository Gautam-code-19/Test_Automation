def order_details(browser, WebDriverWait,logging,ec,By):
    WebDriverWait(browser, 20).until(ec.text_to_be_present_in_element((By.XPATH, "//*[contains(text(), 'THANK YOU!')]"), "THANK YOU!"))
    try:
        order_base_details = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[2]/div/ul')))
        print(order_base_details.text)
    except Exception as e:
        logging.error( "Failed to find the order base details... 🩻 " ,e)