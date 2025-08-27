from behave import when, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from Selectors import selectors


@when('A "{selector_key}" elemet áthúzom a "{target_key}" elemre')
def drag_and_drop(context, selector_key, target_key):
    driver = context.driver


    source = driver.find_element(By.CSS_SELECTOR, selectors[selector_key])
    target = driver.find_element(By.CSS_SELECTOR, selectors[target_key])

    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()

@then ("Megvizsgálom, hogy helyet cseréltek-e")
def check_swap(context):
    driver = context.driver

    a = driver.find_element(By.CSS_SELECTOR, selectors["dd_a"]).text.strip()
    b = driver.find_element(By.CSS_SELECTOR, selectors["dd_b"]).text.strip()

    assert a == "B" and b == "A", f"Helycsere sikertelen: A={a}, B={b}"


@when ('A {selector_key} elemet áthúzom a {target_key} elemre')
def drag_and_drop(context, selector_key, target_key):
    driver = context.driver

    source = driver.find_element(By.CSS_SELECTOR, selectors[selector_key])
    target = driver.find_element(By.CSS_SELECTOR, selectors[target_key])

    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()



@then ("Megvizsgálom, hogy helyet cseréltek-e ismét")
def check_swap_again(context):
    driver = context.driver

    b = driver.find_element(By.CSS_SELECTOR, selectors["dd_b"]).text.strip()
    a = driver.find_element(By.CSS_SELECTOR, selectors["dd_a"]).text.strip()

    assert a == "A" and b == "B", f"Helycsere sikertelen: A={a}, B={b}"