from behave import when, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Selectors import selectors


@when ('Kiválasztom {selector_key} kulcsú elemet')
def drop_down(context, selector_key):
    driver = context.driver

    driver.find_element(By.CSS_SELECTOR, selectors[selector_key]).click()