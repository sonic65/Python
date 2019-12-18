from common.base_pase import BasePage

class MapHomePage(BasePage):

    Map_link = 'xpath=>//*[@id="scpl4"]'

    def click_Map(self):
        self.click(self.Map_link)
        self.sleep(2)
