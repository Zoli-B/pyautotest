from behave import when, then
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




DEFAULT_TIMEOUT = 10
ATTEMPTS = 8
PER_ATTEMPT_TIMEOUT = 2


@then ("Megvizsgálom, hogy a főoldalon vagyok-e")
def step_impl(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "#content > h1").text
    assert text == "Welcome to the-internet", f"Kapott: {text}"


TTEMPTS = 8


@when('megkeresem az eltűnt elemet és rákattintok')
def click_gallery_by_text(context):
    driver = context.driver
    for i in range(ATTEMPTS):
        if i > 0:
            driver.refresh()
            time.sleep(0.3)

        try:
            el = WebDriverWait(driver, PER_ATTEMPT_TIMEOUT).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Gallery"))
            )
            el.click()
            print(f" Gallery kattintva (próba #{i+1})")
            return
        except TimeoutException:
            print(f" Gallery még nincs jelen (próba #{i+1})")

    raise AssertionError(" Nem jelent meg a 'Gallery' link a megadott próbálkozások alatt.")

