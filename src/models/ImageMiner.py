from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import json

import os
import shutil

class ImageMiner(object):

    original_query = None
    internet_query = None
    limit = None
    images_url = None
    default_dir = 'temp/pictures'
    image_type = 'ActiOn'
    on_download_complete_action = None

    def __init__(self, query, limit):
        self.original_query = query
        self.limit = limit
        self.images_url = []

    def get_soup(self, url, header):
        return BeautifulSoup(urlopen(Request(url, headers=header)), 'html.parser')

    def search_images(self):
        self.internet_query = self.original_query.split()
        self.internet_query = '+'.join(self.internet_query)
        url = 'https://www.google.co.in/search?q=' + self.internet_query + '&source=lnms&tbm=isch'

        header_str  = 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
        header_str += 'AppleWebKit/537.36 (KHTML, like Gecko) '
        header_str += 'Chrome/43.0.2357.134 Safari/537.36'

        header = {'User-Agent': header_str}

        soup = self.get_soup(url, header)

        i = 0
        for a in soup.find_all("div", {"class":"rg_meta"}):
            if (i >= self.limit):
                break

            link , Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            self.images_url.append((link, Type))
            i += 1

    def create_dir(self):
        if not os.path.exists(self.default_dir):
                    os.mkdir(self.default_dir)

    def clean_dir(self):
        shutil.rmtree(self.default_dir)

    def load_images(self):

        self.create_dir()

        for i , (img , Type) in enumerate(self.images_url):
            try:
                req = Request(img)
                raw_img = urlopen(req).read()

                cntr = len([i for i in os.listdir(self.default_dir) if self.image_type in i]) + 1
                if len(Type)==0:
                    f = open(os.path.join(self.default_dir , self.image_type + "_"+ str(cntr)+".jpg"), 'wb')
                else :
                    f = open(os.path.join(self.default_dir , self.image_type + "_"+ str(cntr)+"."+Type), 'wb')


                f.write(raw_img)
                f.close()
            except Exception as e:
                print("could not load : "+img)
                print(e)

    def set_on_download_complete_action(self, function):
        self.on_download_complete_action = function

    def mine(self):
        self.search_images()
        self.load_images()
        self.on_download_complete_action()
