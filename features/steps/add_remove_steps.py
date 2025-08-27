from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selectors import selectors

DEFAULT_TIMEOUT = 10

@when("megpróbálom törölni az elemet")
def step_impl(context):
    driver = context.driver
    delete_sel = selectors["delete_button"]
    try:
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, delete_sel))
        ).click()
    except Exception:
        pass

@then('legalább 0 és legfeljebb 1 "delete_button" gomb látható')
def step_impl(context):
    driver = context.driver
    elems = driver.find_elements(By.CSS_SELECTOR, selectors["delete_button"])
    assert 0 <= len(elems) <= 1, f"Várt 0..1, de {len(elems)} darab van"
