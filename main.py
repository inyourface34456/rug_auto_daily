import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import random

# Initialize the undetected-chromedriver. It runs headless by default in recent versions
driver = uc.Chrome(headless=False)
wait = WebDriverWait(driver, 20)

if sys.argv.__len__() != 2:
    print(f"run this as python3 {sys.argv[0]} [account_gmail]")
    exit(1)

 # use javascript:(function(){function getXPath(el){if(el===document.body)return'/html/body';if(el.id)return"//*[@id='"+el.id+"']";var ix=0;var siblings=el.parentNode?el.parentNode.children:[];for(var i=0;i<siblings.length;i++){var sib=siblings[i];if(sib===el)return getXPath(el.parentNode)+'/'+el.tagName.toLowerCase()+'['+(ix+1)+']';if(sib.tagName===el.tagName)ix++;}return'';}let box=document.createElement('div');box.style.cssText='position:fixed;z-index:2147483647;background:rgba(20,20,20,.9);color:#fff;font:12px monospace;padding:6px 8px;border-radius:6px;pointer-events:none;';document.body.appendChild(box);let lastXpath='';document.addEventListener('mousemove',e=>{let el=e.target;if(!el||el===document) return;let xp=getXPath(el);lastXpath=xp;box.textContent=xp;box.style.left=(e.clientX+12)+'px';box.style.top=(e.clientY+12)+'px';});document.addEventListener('keydown',async e=>{if(e.key.toLowerCase()==='c'&&lastXpath){try{await navigator.clipboard.writeText(lastXpath);box.textContent='Copied! '+lastXpath;}catch(err){box.textContent='Clipboard blocked: '+lastXpath;}}});})(); to get xpath, and c to copy
def human_like_typing(element, text):
    """
    Types the given text into the web element character by character
    with a random delay to mimic human behavior.

    :param element: The selenium web element (e.g., a text input field).
    :param text: The string to type.
    """
    for char in text:
        element.send_keys(char)
        # Introduce a random delay between 0.05 and 0.2 seconds
        time.sleep(random.uniform(0.05, 0.2))

try:
    driver.get("https://rugplay.com")
    sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='sign in']")))
    sign_in.click()
    google_sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bits-c8']/div[2]/button[1]/span[1]")))
    google_sign_in.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    human_like_typing(email_input, sys.argv[1])  # Use a dedicated test account

    next_button = driver.find_element(By.ID, "identifierNext")
    next_button.click()
    time.sleep(2)
    # Wait for the password field to appear and enter the password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))
    )
    human_like_typing(password_input, "REMOVED

    signin_button = driver.find_element(By.ID, "passwordNext")
    signin_button.click()

    while True:
        pass

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
