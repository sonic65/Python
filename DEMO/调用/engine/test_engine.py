import time
from browser_engine import BrowserEngine

class TestEngine(object):

    def open_browser(self):
        browserengine = BrowserEngine(self)
        driver = browserengine.chose_browser()

ts = TestEngine()
ts.open_browser()           