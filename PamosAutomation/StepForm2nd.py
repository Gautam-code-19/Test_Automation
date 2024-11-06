#chechout second step:-
def checkout_step_2(browser,time,By,logging):
    time.sleep(1)
    next_step_button = browser.find_element(By.XPATH, '//*[@id="action-next"]')
    order_review = browser.find_element(By.XPATH, '//*[@id="thwmscf-tab-panel-2"]/table')
    print('Table content',order_review.text)
    next_step_button.click()
    logging.info("2nd step table is fetched...✔️")