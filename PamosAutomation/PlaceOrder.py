# filly card details and placing the order:-

def final_checkout(browser , time , By , logging , WebDriverWait , ec, tc_card_number , tc_card_month , tc_card_year , tc_card_cvv):
    time.sleep(1)
    card_number = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="bfws_ccNumber"]'))
    )
    card_month = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="cc-exp-month"]'))
    )
    card_year = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="cc-exp-year"]'))
    )
    card_cvv = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="bfws_cvv"]'))
    )
    place_order = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="place_order"]'))
    )

    try:
        card_number.send_keys(tc_card_number)
        logging.info("card number filled...👍",)
    except Exception as e:
        logging.error( "Not able to fill the card number...",e)

    try:
        card_month.find_elements(By.TAG_NAME, "option")
        i = 0
        for option in card_year.find_elements(By.TAG_NAME, "option"):
            if option.text == tc_card_month:
                browser.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
                logging.info("Card Month filled...👍")
                break
            i += 1

    except Exception as e:
        logging.error( "Not able to fill the card month...",e)

    try:
        card_year.find_elements(By.TAG_NAME, "option")
        i = 0
        for option in card_year.find_elements(By.TAG_NAME, "option"):
            if option.text == tc_card_year:
                browser.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
                logging.info("Card Year filled...👍")
                break
            i += 1

    except Exception as e:
        logging.error( "Not able to fill the card Year...",e)

    try:
        card_cvv.send_keys(tc_card_cvv)
        logging.info("card CVV number filled...👍")
    except Exception as e:
        logging.error( "Not able to fill the card CVV number...",e)

    try:
        time.sleep(1)
        browser.execute_script("arguments[0].scrollIntoView();", place_order)
        WebDriverWait(browser, 10).until(ec.element_to_be_clickable(place_order))
        place_order.click()
        logging.info("Order Placed Successfully...🫡")
    except Exception as e:
        logging.error(e,"Failed to place order...")
    time.sleep(10)