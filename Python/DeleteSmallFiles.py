import os

DirList = [
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/drawings',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/hentai',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/neutral',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/porn',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/sexy']


for path in DirList:
    print(path)
    tall = 0
    small = 0
    for filename in os.listdir(path):
        fullName = os.path.join(path, filename)
        size = os.path.getsize(fullName)
        if size < 20 * 1024:
            small = small + 1
            os.remove(fullName)
        tall = tall + 1
    print(tall, small, small/tall * 100)