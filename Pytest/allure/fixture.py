from selenium import webdriver


def open_url():
        driver = webdriver.Chrome()
        driver.get(url)
        yield driver
        driver.quit()
