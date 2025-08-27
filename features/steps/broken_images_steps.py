from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

@when("Megvizsgálom vannak-e kép elemek az oldalon")
def step_collect_images(context):
    try:
        WebDriverWait(context.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "img"))
        )
    except Exception:
        pass

    context.images = context.driver.find_elements(By.TAG_NAME, "img")
    assert context.images is not None, "Nem sikerült lekérni a képeket."


@when("Megvizsgálom melyik kép sérült")
def step_check_broken_images(context):
    if not hasattr(context, "images"):
        context.images = context.driver.find_elements(By.TAG_NAME, "img")

    broken = []

    for img in context.images:
        src = img.get_attribute("src")
        natural_width = context.driver.execute_script("return arguments[0].naturalWidth;", img)
        if natural_width == 0:
            broken.append(src)

    context.broken_images = broken


@then('{n:d} sérült képet találok')
def step_assert_broken_count(context, n):
    broken = getattr(context, "broken_images", [])
    assert len(broken) == n, f"Várt: {n} db sérült kép, talált: {len(broken)}. Források: {broken}"
