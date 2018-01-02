"""
    download video form www.blibli.com

"""
import gzip
import os
import re
from io import BytesIO
from urllib import request

from bs4 import BeautifulSoup


def get_names(root_url: str):
    req = request.Request(url=root_url)
    response = request.urlopen(url=req)
    html = response.read()
    compressed_stream = BytesIO(html)
    gzipper = gzip.GzipFile(fileobj=compressed_stream)
    data = gzipper.read()
    bs_obj = BeautifulSoup(data, 'lxml')
    plist = bs_obj.find(id='plist')
    names_str = plist.get_text()
    f = open('./names.txt', 'w', encoding='utf8')
    f.write(names_str)
    f.close()


def modify_name(video_dir: str):
    name_list = []
    f = open('./names.txt', 'r', encoding='utf8')
    for line in f:
        name_list.append(line.replace('\n', ''))
    names = os.listdir(video_dir)
    for name in names:
        old_name = video_dir + name
        index = re.search('(\d+)', name).group()
        new_name = video_dir + name_list[int(index) - 1] + '.mp4'
        os.rename(old_name, new_name)


if __name__ == '__main__':
    video_dir = '/Users/gbzhu/data/machine_learning/Ng_machine_learning/'
    modify_name(video_dir)
