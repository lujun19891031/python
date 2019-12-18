#coding:utf-8
import requests
from bs4 import BeautifulSoup

class Spider(object):

    def __init__(self, url):
        self.url = url

    def stop(self):
        pass

    def run(self):
        self.response = requests.get(self.url)
        self.response.encoding = "gbk"  # 默认编码为utf-8
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.div = self.soup.find(name="div" , attrs={"id": "auto-channel-lazyload-article"})
        self.li_list = self.div.find_all(name="li")
        for li in self.li_list:
            title = li.find(name="h3")
            if not title:
                continue
            title = title.text
            content = li.find(name="p").text
            link = "https:" + li.find(name="a").attrs.get("href")
            # print(title)
            # print(content)
            # print(link)

            img = "http:" + li.find(name="img").attrs.get("src")
            img_response = requests.get(img)  # 请求图片地址
            filename = img.split("/")[-1]
            with open(filename, "wb") as f:
                f.write(img_response.content)
            print("===================")

autohome = Spider("https://www.autohome.com.cn/news/")
autohome.run()