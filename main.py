import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import sys
import time
import random
import os

load_dotenv()

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
        # Introduce a random delay between 0.05 and 0.1 seconds
        time.sleep(random.uniform(0.05, 0.2))

def rand_delay():
    return 1.5 * random.uniform(0.7, 2)

def move_nat(target):
    size = target.size
    click_x = int(size["width"] * random.uniform(0.3, 0.7))
    click_y = int(size["height"] * random.uniform(0.3, 0.7))

    # Move to element first
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(target, 0, 0)  # top-left of element

    # Gradually move to random click point
    steps = 20
    dx = click_x / steps
    dy = click_y / steps

    for i in range(steps):
        actions.move_by_offset(dx, dy)
        actions.pause(0.01 * random.uniform(0.7, 1.3))

    # Click
    # actions.click()
    actions.perform()

try:
    driver.get("https://rugplay.com")
    sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='sign in']")))
    sign_in.click()
    google_sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bits-c8']/div[2]/button[1]/span[1]")))
    google_sign_in.click()

    email_input = wait.until(
        EC.element_to_be_clickable((By.ID, "identifierId"))
    )
    move_nat(email_input)
    time.sleep(rand_delay())
    human_like_typing(email_input, sys.argv[1])  # Use a dedicated test account

    next_button = wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
    time.sleep(rand_delay())
    move_nat(next_button)
    time.sleep(rand_delay())
    next_button.click()
    time.sleep(rand_delay())
    # Wait for the password field to appear and enter the password
    password_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "Passwd"))
    )
    move_nat(password_input)
    time.sleep(rand_delay())
    human_like_typing(password_input, os.getenv("PASSWORD"))

    signin_button = driver.find_element(By.ID, "passwordNext")
    time.sleep(rand_delay())
    move_nat(signin_button)
    time.sleep(rand_delay())
    signin_button.click()
    time.sleep(rand_delay())

    while True:
        pass

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
