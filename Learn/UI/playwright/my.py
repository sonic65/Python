from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to chrome-error://chromewebdata/
    page.goto("chrome-error://chromewebdata/")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=playwright&fenlei=256&rsv_pq=a8c0f7540024ee9b&rsv_t=e175rgmyjDIVVCY5kWYXT36yOX%2Brl%2FFqOMC2%2Byqc4z37YZx%2BjagMTtgGtRY&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=11&rsv_sug1=9&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=playwright&rsp=5&inputT=3242&rsv_sug4=5135"):
    with page.expect_navigation():
        page.fill("input[name=\"wd\"]", "playwright")

    # Press Enter
    page.press("input[name=\"wd\"]", "Enter")

    # Press Enter
    page.press("//body[starts-with(normalize-space(.), \"if (navigator.userAgent.indexOf('Edge') > -1) { var body = document.querySelecto\")]", "Enter")

    # Click text="-python 教程_天下任我行-CSDN博客"
    # with page.expect_navigation(url="https://blog.csdn.net/lb245557472/article/details/111572119"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("text=\"-python 教程_天下任我行-CSDN博客\"")
        page1 = popup_info.value

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)