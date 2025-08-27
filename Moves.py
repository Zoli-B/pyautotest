from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Selectors import selectors

DEFAULT_TIMEOUT = 2

def click_by_css(driver, key, timeout=DEFAULT_TIMEOUT):
    locator = (By.CSS_SELECTOR, selectors[key])
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator)).click()

def add_remove(driver):
    click_by_css(driver, "add_remove_link")
    time.sleep(DEFAULT_TIMEOUT)
    click_by_css(driver, "add_button")
    time.sleep(DEFAULT_TIMEOUT)
    try:
        click_by_css(driver, "delete_button")
        time.sleep(DEFAULT_TIMEOUT)
    except Exception:
        pass

def auth(driver, user="admin", pwd="admin"):
    click_by_css(driver, "auth")
    time.sleep(DEFAULT_TIMEOUT)
    driver.get(f"https://{user}:{pwd}@the-internet.herokuapp.com/basic_auth")
    time.sleep(DEFAULT_TIMEOUT)

def broken_image(driver):
    click_by_css(driver, "broken_image")
    time.sleep(DEFAULT_TIMEOUT)
    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        src = img.get_attribute("src")
        natural_width = driver.execute_script("return arguments[0].naturalWidth;", img)

        if natural_width == 0:
            print("Sérült kép:", src)
        else:
            print("OK kép:", src)

