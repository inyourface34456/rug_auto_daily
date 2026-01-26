import undetected_chromedriver as uc
from dotenv import load_dotenv
from interactionn_prim import *
from logger import Logger
import sys
import json
import random

user_agents = json.loads(open('index.json').read())
user_agent = random.choice(user_agents)

chrome_options = uc.ChromeOptions()
chrome_options.add_argument(f"--user-agent={user_agent}")

width = random.randint(1024, 1920)
height = random.randint(768, 1080)
chrome_options.add_argument(f"--window-size={width},{height}")

load_dotenv()
driver = uc.Chrome(headless=False, options=chrome_options)

try:
    password = sys.argv[2]
    email = sys.argv[1]
    target_acc = sys.argv[3]

    logger = Logger(True)

    click_sign_in(driver, logger)

    sign_into_google(driver, email, password, logger)

    claim_daily(driver, logger)

    send_all_money_to_users(driver, target_acc, logger)

    print("done")
except Exception as e:
    print(f"An error occurred: {e}")
