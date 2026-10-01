import pytest
import allure
from etl import output
from api_client import ApiClient

@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    report = yield
    setattr(item, "rep_" + report.when, report)
    return report

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

    # 收尾，如果刚才测试失败了，自动截图挂进报告。
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        allure.attach(
            p.screenshot(),
            name="失败截图",
            attachment_type=allure.attachment_type.PNG,
        )

    p.close()

@pytest.fixture
def rows():
    return output()

@pytest.fixture(scope="session")
def api():
    c = ApiClient("https://httpbin.org")
    c.login("ken")
    return c


@pytest.fixture(scope="session")
def driver():
    from selenium import webdriver
    d = webdriver.Chrome()
    yield d
    d.quit()