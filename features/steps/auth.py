from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

@when("beírtam a felhasználónevet és a jelszót")
def auth(context, user="admin", pwd="admin"):
    context.driver.get(f"https://{user}:{pwd}@the-internet.herokuapp.com/basic_auth")

@then("Congratulations! You must have the proper credentials. szöveget kapom vissza")
def auth_valid(context):
    WebDriverWait(context.driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.example p"))
    )
    text = context.driver.find_element(By.CSS_SELECTOR, "div.example p").text.strip()
    assert text == "Congratulations! You must have the proper credentials.", f"Kapott: {text}"
