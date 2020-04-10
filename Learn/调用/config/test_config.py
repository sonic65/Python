import configparser
import os

class ConfigTest(object):

    def get_value(self):

        dir = os.path.dirname(os.path.abspath('.')) 
        # config_path =dir + '\config\config.ini'
        config_path = '../config/config.ini'
        print(dir)
        config = configparser.ConfigParser()

        config.read(config_path, encoding='utf-8')
        browser = config.get("browserType","browserName")
        url = config.get("testServer","URL")

        return(browser,url)

trc = ConfigTest()
print(trc.get_value())        


