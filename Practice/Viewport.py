from selenium import webdriver
import time

viewports =[(1024,768),(768,1024),(375, 667),(414,896)]

browser = webdriver.Firefox()
browser.get('https://dev.letsmakeinvoice.com/')

try:
    for width,height in viewports:
        browser.set_window_size(width,height)
        time.sleep(4)

finally:
    browser.close()