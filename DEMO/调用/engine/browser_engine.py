from selenium import webdriver

class BrowserEngine(object):

    def __init__(self,driver):
        self.driver = driver

    browser_type = ""   
    # browser_type = "IE"    
    # browser_type = "Firefox"     

    def chose_browser(self):

        if self.browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif self.browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif self.browser_type == 'IE':
            driver = webdriver.Ie()
        else: driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        return driver