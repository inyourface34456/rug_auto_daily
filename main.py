import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# Initialize the undetected-chromedriver. It runs headless by default in recent versions
driver = uc.Chrome()

if sys.argv.__len__() != 2:
    print(f"run this as python3 {sys.argv[0]} [account_gmail]")
    exit(1)

try:
    # Navigate to the Google login page
    driver.get("https://accounts.google.com/servicelogin")

    # Use explicit waits and stable locators to interact with elements
    # Enter email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys(sys.argv[1]) # Use a dedicated test account

    next_button = driver.find_element(By.ID, "identifierNext")
    next_button.click()
    time.sleep(2)
    # Wait for the password field to appear and enter the password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))
    )
    password_input.send_keys("REMOVED

    signin_button = driver.find_element(By.ID, "passwordNext")
    signin_button.click()

    # After successful login, you can navigate to other Google services
    WebDriverWait(driver, 20).until(
        EC.url_contains("myaccount.google.com")
    )
    print("Logged in successfully!")

    # Keep the browser open for a few seconds to verify
    while True:
        pass

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
