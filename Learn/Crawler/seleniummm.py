from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

URL = "https://www.bilibili.com"

def get_page_source(url):
    browser = webdriver.Chrome()
    browser.get(url)
    sleep(5)
    page_source = browser.page_source
    print(page_source)
    browser.close()
    return page_source

def save_html(filename,page_source):
    with open(filename,"wb") as f:
        f.write(page_source)

def main():
    filename = "provider.html"
    '''
    从str到bytes: 调用方法.encode()
    从bytes到str: 调用方法.decode()
    '''
    page_source = get_page_source(URL).encode()
    save_html(filename,page_source)


if __name__ == "__main__":
    main()