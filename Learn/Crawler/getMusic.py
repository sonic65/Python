#refer:https://www.weiney.com/2035.html

import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import threading
import requests
import os
from tqdm import tqdm
if not os.path.exists("album"):
    os.mkdir("album")
PATH = os.getcwd() + "\\album\\"
URL = "http://yoerking.com/static/music_player.html"
ALL_MUSICS = []
def get_page_sourse():
    browser = webdriver.Chrome()
    browser.get(URL)
    page_sourse = browser.page_source
    browser.close()
    return page_sourse
def parse_music():
    page_sourse = get_page_sourse()
    soup = BeautifulSoup(page_sourse, "html.parser")
    all_musics = soup.find_all("a", class_="url")
    for music_item in all_musics:
        single_music = dict()
        single_music["url"] = music_item.attrs["hrefsrc"]
        single_music["name"] = music_item.text
        single_music["album"] = re.search("(?<=music/)(.*?)(?=/)", single_music["url"]).group()
        ALL_MUSICS.append(single_music)
def create_dir(albums):
    for album in albums:
        if not os.path.exists(PATH + album):
            os.mkdir(PATH + album)
class DownloadThread(threading.Thread):
    def __init__(self, single_music, phar):
        threading.Thread.__init__(self)
        self.single_music = single_music
        self.phar = phar
    def run(self) -> None:
        req = requests.get(self.single_music["url"])
        with open(PATH + self.single_music["album"] + "\\" + self.single_music["name"], "wb") as f:
            f.write(req.content)
            self.phar.update(1)
if __name__ == '__main__':
    parse_music()
    ALL_ALBUMS = set([album["album"] for album in ALL_MUSICS])
    print("获取到专辑数量:{}, 歌曲数量:{}".format(len(ALL_ALBUMS), len(ALL_MUSICS)))
    print("正在创建专辑目录")
    create_dir(ALL_ALBUMS)
    print("专辑目录创建完成,开始下载歌曲")
    with tqdm(total=len(ALL_MUSICS)) as phar:
        for single in ALL_MUSICS:
            while threading.active_count() > 20:
                time.sleep(1)
            thread = DownloadThread(single, phar)
            thread.start()
    input("爬虫执行完成,按任意键退出")
