from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urllib3.util import wait

# browser= webdriver.Firefox()

browser= webdriver.Chrome()


browser.maximize_window()
print("---- Window maxed ----")
browser.get("https://qa10624.pamos.com/")

title = browser.title
print("Login title :--" ,title )


# Age verification pop-up
try:
    # Wait for the age verification pop-up to appear and click the button
    WebDriverWait(browser, 10).until(
        ec.visibility_of_element_located((By.XPATH, '//*[@id="age-gate"]/div/div'))
    )
    print("Pop is there")
    Age_button = browser.find_element(By.XPATH, '//*[@id="age-gate"]/div/div/div/div/div[2]/div[1]/button')
    Age_button.click()
    print("Closed age verification pop-up.")

except Exception as e:
    print(e," An error occurred while handling the age verification pop-up.")

# Closing the email 20% off pop-up
try:
    WebDriverWait(browser,17).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="newsletter-form"]/div/div')))
    print("Email pop-up is opened.")
    CloseEmail_pop_up = browser.find_element(By.XPATH,'//*[@id="newsletter-form"]/div/div/div[1]/div/button')
    CloseEmail_pop_up.click()
    print("Email-pop is closed successfully.")

except Exception as e:
    print(e, " Not able tto click on the email offer pop-up.")



# WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@title='Close model']")))
# print("Model opened")
# WebDriverWait(browser, 3)





# WebDriverWait(browser, 17).until(ec.presence_of_element_located((By.XPATH , "xpath")))

# CloseEmail_pop= browser.find_element(By.XPATH,"")
# CloseEmail_pop.click()


# driver.findElement(By.xpath("//button[@title='Close model']"))







print("Browser is closed")
browser.quit()
