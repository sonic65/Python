from common.base_page import BasePage

class ArticleHomePage(BasePage):

    article_link = 'xpath=>//*[@id="scpl2"]'

    def click_article(self):
        self.click(self.article_link)
        self.sleep(2)
