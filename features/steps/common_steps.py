# features/steps/common_steps.py
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selectors import selectors

DEFAULT_TIMEOUT = 10

def click_by_css(driver, key, timeout=DEFAULT_TIMEOUT):
    locator = (By.CSS_SELECTOR, selectors[key])
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator)).click()

@given("a főoldalon vagyok")
def step_impl(context):
    context.driver.get(context.base_url)
    try:
        pass
    except Exception:
        pass

@when('ráklikkelek a "{selector_key}" kulcsú elemre')
def step_impl(context, selector_key):
    click_by_css(context.driver, selector_key)

@then('az URL "{path}" végződésre vált')
def step_impl(context, path):
    WebDriverWait(context.driver, DEFAULT_TIMEOUT).until(
        EC.url_to_be(context.base_url.rstrip("/") + path)
    )

@when ("visszalépek az előző oldalra")
def go_back(context):
    driver = context.driver
    driver.back()
