import os
import shutil
from PIL import Image

DirList = [
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/drawings',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/hentai',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/neutral',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/porn',
     '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/sexy'
]


def is_valid_jpg(jpg_file):
    with open(jpg_file, 'rb') as f:
        f.seek(-2, 2)
        buf = f.read()
        return buf == b'\xff\xd9'


def is_valid_png(png_file):
    with open(png_file, 'rb') as f:
        f.seek(-3, 2)
        buf = f.read()
        if buf == b'\x60\x82\x00':
            return True
        elif buf[1:] == b'\x60\x82':
            return True
        else:
            return False


def is_valid_pic(pic_file):
    if pic_file.endswith('jpeg'):
        return is_valid_jpg(pic_file)

    elif pic_file.endswith('png'):
        return is_valid_png(pic_file)
    else:
        return False


for path in DirList:
    for file in os.listdir(path):
        pic_file = os.path.join(path, file)
        if not is_valid_pic(pic_file):
            try:
                img = Image.open(pic_file)
                img.load()
            except Exception as e:
                #print(e)
                print(pic_file)
                #shutil.copy(pic_file, '/home/king/Desktop/')
                #os.remove(pic_file)
