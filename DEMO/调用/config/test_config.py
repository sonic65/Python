import configparser
import os

class ConfigTest(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))
        print(root_dir)

        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath(".") + "/config.ini"        # file_path = './config.ini'
        config.read(file_path)
        browser = config.get("browserType","browserName")
        url = config.get("testServer","URL")

        return(browser,url)

trc = ConfigTest()
print(trc.get_value())        


