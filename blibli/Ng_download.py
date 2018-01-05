"""
    download NG's video form www.blibli.com

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
    with open('./Lhy_names.txt', 'w', encoding='utf8') as f:
        f.write(names_str)


def modify_name(videos_dir_path: str):
    name_list = []
    f = open('./names.txt', 'r', encoding='utf8')
    for line in f:
        name_list.append(line.replace('\n', ''))
    names = os.listdir(videos_dir_path)
    for name in names:
        old_name = videos_dir_path + name
        index = re.search('(\d+)', name).group()
        new_name = videos_dir_path + name_list[int(index) - 1] + '.mp4'
        os.rename(old_name, new_name)


def rename(videos_dir_path: str):
    names = os.listdir(videos_dir_path)
    for name in names:
        print(name)
        if '、' not in name:
            continue
        else:
            old_name = videos_dir_path + name
            name_p = name.split('、')[1]
            new_name = videos_dir_path + name_p
            os.rename(old_name, new_name)


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/av10590361/#page=1'
    get_names(url)
