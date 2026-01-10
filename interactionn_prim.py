from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import *
from logger import Level

def click_sign_in(driver, logger):
    wait = WebDriverWait(driver, 20)
    logger.log(Level.INFO, "going to rugplay")
    driver.get("https://rugplay.com")
    logger.log(Level.INFO, "clicking rugplay signin")
    sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='sign in']")))
    sign_in.click()
    logger.log(Level.INFO, "clicking google sign in")
    google_sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bits-c8']/div[2]/button[1]/span[1]")))
    google_sign_in.click()

def sign_into_google(driver, email, passw, logger):
    wait = WebDriverWait(driver, 20)
    email_input = wait.until(
        EC.element_to_be_clickable((By.ID, "identifierId"))
    )
    logger.log(Level.INFO, "natruly hovering on email input")
    move_nat(driver, email_input)
    logger.log(Level.INFO, "human sleep")
    time.sleep(rand_delay())
    logger.log(Level.INFO, "typing email")
    human_like_typing(email_input, email)

    next_button = wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
    time.sleep(rand_delay())
    logger.log(Level.INFO, "moving to next button")
    move_nat(driver, next_button)
    logger.log(Level.INFO, "sleeping before clicking next")
    time.sleep(rand_delay())
    next_button.click()
    time.sleep(rand_delay())
    password_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "Passwd"))
    )
    logger.log(Level.INFO, "moving natruly to passwd field")
    move_nat(driver, password_input)
    time.sleep(rand_delay())
    logger.log(Level.INFO, "typing password")
    human_like_typing(password_input, passw)

    signin_button = driver.find_element(By.ID, "passwordNext")
    logger.log(Level.INFO, "moving natruly to sign in")
    time.sleep(rand_delay())
    move_nat(driver, signin_button)
    logger.log(Level.INFO, "clicking sign in button")
    time.sleep(rand_delay())
    signin_button.click()
    time.sleep(rand_delay())

def claim_daily(driver, logger):
    wait = WebDriverWait(driver, 20)
    logger.log(Level.INFO, "claim daily")
    claim_daily = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]")))
    claim_daily.click()

def send_all_money_to_users(driver, uname, logger):
    wait = WebDriverWait(driver, 20)
    logger.log(Level.INFO, "enter portfolio page")
    portfolio = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[6]/a[1]")))
    portfolio.click()
    logger.log(Level.INFO, "open send dialoug")
    open_send_dialoug = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")))
    open_send_dialoug.click()
    logger.log(Level.INFO, "click max button")
    click_max_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='bits-c15']/div[2]/div[3]/div[1]/button[1]")))
    click_max_button.click()
    logger.log(Level.INFO, "click and enter username")
    uname_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recipient']")))
    logger.log(Level.INFO, "typing username")
    uname_field.send_keys(uname)
    logger.log(Level.INFO, "send money")
    click_send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bits-c15']/div[3]/button[2]")))
    click_send_button.click()