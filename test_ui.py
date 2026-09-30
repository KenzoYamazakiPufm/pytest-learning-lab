import allure
import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui

@allure.title("标题检查")
def test_title(page):
    page.goto("https://example.com")
    assert "Example" in page.title()

@allure.title("表单提交:填写姓名并验证结果")
def test_form(page):
    with allure.step("打开表单页"):
        page.goto("https://httpbin.org/forms/post")

    with allure.step("输入姓名"):
        page.locator("input[name='custname']").fill("Ken")
        # expect(page.locator("input[name='custname']")).to_have_value("Ken")

    with allure.step("提交并验证"):
        page.locator("button").click()
        expect(page.locator("pre")).to_contain_text("Ken")

    # with allure.step("保存截图到报告"):
    #     allure.attach(
    #         page.screenshot(),
    #         name="提交后的结果页",
    #         attachment_type=allure.attachment_type.PNG,
    #     )

@allure.title("截图对比:视口VS整页")
def test_screenshot(page):
    page.goto("https://playwright.dev/python/")
    page.screenshot(path="shot.png")
    page.screenshot(path="full.png", full_page=True)
