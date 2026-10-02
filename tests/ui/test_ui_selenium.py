import base64
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = pytest.mark.ui

def test_title_selenium(driver):
    driver.get("https://example.com")
    assert "Example" in driver.title


def test_form_selenium(driver):
    driver.get("https://httpbin.org/forms/post")

    name = driver.find_element(By.NAME, "custname")
    name.send_keys("Ken")
    assert name.get_attribute("value") == "Ken"

    driver.find_element(By.TAG_NAME, "button").click()

    pre = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "pre"))
    )
    assert "Ken" in pre.text

def test_screenshot_selenium(driver):
    driver.get("https://playwright.dev/python/")

    driver.save_screenshot("sel_shot.png")

    png = driver.execute_cdp_cmd("Page.captureScreenshot", {"captureBeyondViewport": True})
    with open("sel_full.png", "wb") as f:
        f.write(base64.b64decode(png["data"]))
        