from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

Site_url = 'https://hrm.techmarcos.com/web/index.php/auth/login'
UserName = 'GautamSingh'
Password = 'Asjdwh@492'
Login_title = 'OrangeHRM'

Browser = webdriver.Firefox()
Browser.maximize_window()
Browser.get(Site_url)
# WebDriverWait(Browser,5).until(ec.title_is(Login_title))

WebDriverWait(Browser, 5).until(ec.presence_of_element_located((By.NAME, 'username')))

User_name_input=Browser.find_element(By.NAME, 'username')
Password_input = Browser.find_element(By.NAME, 'password')

User_name_input.send_keys(UserName)
Password_input.send_keys(Password)

Login_button = Browser.find_element(By.XPATH, "//button[@type='submit']")
Login_button.click()


# finding the time tab

WebDriverWait(Browser,5).until(ec.presence_of_all_elements_located((By.XPATH, "//span[text()='Time']")))
Time_tab = Browser.find_element(By.XPATH, "//span[text()='Time']")
Time_tab.click()

WebDriverWait(Browser, 5).until(ec.presence_of_element_located((By.XPATH, '//header/div[2]/nav[1]/ul[1]/li[2]/span[1]')))

Attendance = Browser.find_element(By.XPATH, '//header/div[2]/nav[1]/ul[1]/li[2]/span[1]')
Attendance.click()

WebDriverWait(Browser, 5).until(ec.presence_of_element_located((By.XPATH , "//a[text()='Punch In/Out']")))
PunchIn_out_tab= Browser.find_element(By.XPATH , "//a[text()='Punch In/Out']")
PunchIn_out_tab.click()


WebDriverWait(Browser,6).until(ec.invisibility_of_element((By.CSS_SELECTOR, '.oxd-form-loader')))

sleep(2)

WebDriverWait(Browser, 5).until(ec.visibility_of_element_located((By.XPATH , "//button[@type='submit']")))
PunchIn_out_button = Browser.find_element(By.XPATH , "//button[@type='submit']")
PunchIn_out_button.click()

Browser.quit()