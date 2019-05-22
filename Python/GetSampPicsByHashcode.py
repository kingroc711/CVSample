import os
import hashlib

DirList = [
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/drawings',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/hentai',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/neutral',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/porn',
    '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/sexy'
]


def getMD5(file, readLen=1024 * 20):
    md5code = hashlib.md5()
    with open(file, 'rb') as f:
        data = f.read()

        # *********一定要注意这里下面的写法是错误的**********
        # 带有读取限制的方式是错误的，有的图片头部是相同的，往往有几十K的头，这些头都相同的，
        # 如果想加读取限制，保险的情况就是限制的大小和较小的那个文件相同。
        # data = f.read(readLen)

    md5code.update(data)

    ret = md5code.hexdigest()
    return ret


m = dict()
html_start = '<html>\n' \
             '<style>\n' \
             'img{\n' \
             'width: 200px;\n' \
             'height: auto;\n' \
             '}\n' \
             '</style>\n\n' \
             '<body>\n\n'

html_end = '</body>\n' \
           '</html>\n'

div_string = '<div>\n' \
             '<img src="%s" />\n' \
             '<img src="%s" />\n' \
             '</div>\n\n'

html = open('/home/king/Desktop/a.html', 'w')
html.write(html_start)

same = 0

for path in DirList:
    for filename in os.listdir(path):
        fullName = os.path.join(path, filename)
        if os.path.isfile(fullName):
            md5 = getMD5(fullName)
            if md5 not in m.keys():
                m[md5] = fullName
            else:
                html.write(div_string % (fullName, m[md5]))
                print(fullName, m[md5])
                # 使用时请打开
                # os.remove(fullName)
                same = same + 1
                # 这里写200个目的就是先通过网页检查一遍，如果没有错误，再打开删除语句。当然了这里只是测试代码。
                if (same > 200):
                    break
print(same)
html.write(html_end)
html.close()
