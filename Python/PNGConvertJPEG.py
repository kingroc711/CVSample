import os
from PIL import Image

DirList = [
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/drawings',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/hentai',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/neutral',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/porn',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/sexy'
]

for path in DirList:
    for filename in os.listdir(path):
        fullName = os.path.join(path, filename)
        if fullName.endswith('.png'):
            mainName, ext = os.path.splitext(fullName)
            print(fullName, mainName + '.jpeg')
            im = Image.open(fullName).convert("RGBA")
            bg = Image.new('RGB', im.size, (255, 255, 255))
            x, y = im.size
            bg.paste(im, (0, 0, x, y), im)
            bg.save(mainName + '.jpeg', quality=99)
            os.remove(fullName)