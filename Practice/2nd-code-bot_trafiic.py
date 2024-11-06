from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configure ChromeDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs browser in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")  # Prevent issues in some environments

# Set the path to your ChromeDriver
webdriver_service = Service("/path/to/chromedriver")  # Update path accordingly

# Set the URL to simulate traffic
url = "https://www.techmarcos.com/"

# Function to simulate traffic
def simulate_traffic(visits=10, wait_time=2):
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    for visit in range(visits):
        print(f"Visit {visit + 1} to {url}")
        driver.get(url)  # Visit the website
        
        # Simulate scrolling
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(wait_time)  # Wait to simulate user time on site
        
        # Click on some links or buttons (optional)
        # Example: Find a link and click it
        try:
            link = driver.find_element(By.PARTIAL_LINK_TEXT, "About")
            link.click()
            print("Clicked on About link")
            time.sleep(wait_time)
        except Exception as e:
            print("No clickable link found:", e)

    # Close the driver
    driver.quit()

# Call the function to simulate 10 visits with a 2-second wait between actions
simulate_traffic(visits=50, wait_time=2)
