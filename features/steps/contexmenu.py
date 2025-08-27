from behave import when, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selectors import selectors
from Selectors import selectors

DEFAULT_TIMEOUT = 10


@when ("Jobb klikkel rákatintok a fekete elemre")
def context_menu(context):
    driver = context.driver
    element = driver.find_element(By.CSS_SELECTOR, selectors["cm_select"])

    action = ActionChains(driver)
    action.context_click(element).perform()

@then ("Megvizsgálom sikeres volt-e a kattintás")
def context_check(context):
    driver = context.driver
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()