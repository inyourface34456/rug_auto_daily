from email.policy import default

import undetected_chromedriver as uc
from dotenv import load_dotenv
from interactionn_prim import *
from logger import Logger
# from runargs import Args
# from mut_elu import MutuallyExclusiveOption
# import click
# import os
import sys

# @click.command()
# @click.option("--email", help="password for the email")
# @click.option("--target-acc", required=False, help="what account to send the money to")
# @click.option("--password", required=False, help="password")
# @click.option("--from-env", required=False, is_flag=True, default=True, help="use environment variables",
#               cls=MutuallyExclusiveOption,
#               mutually_exclusive=["password", "target_acc"]
# )
# def get_args(email, password, from_env, target_acc):
#     print("line 21")
#     return Args(email, password, from_env, target_acc)

load_dotenv()
driver = uc.Chrome(headless=False)

# use the bookmarklet in the readme to get xpath, and c to copy

try:
    # args = get_args()
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
