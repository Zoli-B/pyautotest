from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selectors import *
from features.steps.common_steps import click_by_css
import time

DEFAULT_TIMEOUT = 10

filename = f"screenshot_{int(time.time())}.png"

@when('rákattintok a "{selector_key}" boxra')
def checkbox_one(context, selector_key):
    driver = context.driver
    try:
        click_by_css(driver, selector_key)
    except Exception:
        pass


@then ("megvizsgálom a változást")
def checkbox_valid(context):
    driver = context.driver
    checkbox = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
    if checkbox.is_selected():
        print("Működik")
    else:
        print("nem működik")