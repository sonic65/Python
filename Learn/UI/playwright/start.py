# 安装playwright库
# pip install playwright

# 安装浏览器驱动文件
# python -m playwright install

# 比如，我要在baidu.com搜索，用chromium驱动，将结果保存为my.py的python文件。
# python -m playwright codegen --target python -o 'my.py' -b chromium https://www.baidu.com

from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()
    # Open new page
    page = context.newPage()
    page.goto("https://www.baidu.com/")
    page.click("input[name=\"wd\"]")
    page.fill("input[name=\"wd\"]", "jingdong")
    page.click("text=\"京东\"")
    # Click //a[normalize-space(.)='京东JD.COM官网 多快好省 只为品质生活']
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("//a[normalize-space(.)='京东JD.COM官网 多快好省 只为品质生活']")
        page1 = popup_info.value
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)