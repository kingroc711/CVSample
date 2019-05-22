import magic
import os
import filetype

DirList = [
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/drawings',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/hentai',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/neutral',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/porn',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/sexy'
]

for path in DirList:
    for file in os.listdir(path):
        pic_file = os.path.join(path, file)
        if pic_file.endswith('jpeg') or pic_file.endswith('png'):
            # a = magic.from_file(pic_file,mime=True )
            # print(pic_file, a)
            kind = filetype.guess(pic_file)
            getExt = str(kind.mime).split('/')[1]
            #print(pic_file, kind.extension, kind.mime)
            mainName, ext = os.path.splitext(pic_file)
            ext = ext[1:]
            if ext != getExt:
                # if(getExt != 'jpeg' and getExt != 'png'):
                #     os.remove(pic_file)
                print(pic_file, getExt)
                os.renames(pic_file, mainName + "." + getExt)

