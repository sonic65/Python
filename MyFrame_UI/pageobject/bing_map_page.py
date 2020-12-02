from common.base_page import BasePage

class MapHomePage(BasePage):

    map_link = 'xpath=>//*[@id="scpl4"]'

    def click_map(self):
        self.click(self.map_link)
        self.sleep(2)
