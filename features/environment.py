from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

BASE_URL = "https://the-internet.herokuapp.com/"

#for screenshots
filename = f"screenshot_{int(time.time())}.png"


def screenshot(context):
    context.driver.save_screenshot(filename)

def before_all(context):
    context.base_url = BASE_URL

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(2)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        try:
            context.driver.save_screenshot(screenshot(context))
        except Exception:
            pass
    context.driver.quit()
