import pytest
import allure

@pytest.fixture(scope="session")
def browser():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome", headless=True)
        yield b
        b.close()

@pytest.fixture
def page(browser, request):
    p = browser.new_page()
    yield p
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        allure.attach(p.screenshot(), name="失败截图",
                      attachment_type=allure.attachment_type.PNG)
    p.close()

@pytest.fixture(scope="session")
def driver():
    from selenium import webdriver
    d = webdriver.Chrome()
    yield d
    d.quit()
