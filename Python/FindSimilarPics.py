import cv2
import os

DirList = [
     #'/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/drawings',
     '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/hentai',
     #'/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/neutral',
     #'/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/porn',
     #'/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/sexy'
]

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
num = 0
for path in DirList:
    for filename in os.listdir(path):
        fullName = os.path.join(path, filename)
        if os.path.isfile(fullName):
            im = cv2.imread(fullName, 0)
            m[fullName] = cv2.calcHist([im], [0], None, [256], [0, 256])
            num = num + 1
            if num % 500 == 0:
                print(num)

print('to compareHist')
keyList = list(m.keys())
for i in range(len(keyList)):
    for j in range(i + 1, len(keyList)):
        cmp = cv2.compareHist(m[keyList[i]], m[keyList[j]], cv2.HISTCMP_CHISQR_ALT)
        score = cmp * 100
        #print(score)
        if score < 1:
            html.write(div_string % (keyList[i], keyList[j]))
            if os.path.exists(keyList[j]):
                os.remove(keyList[j])
            print(keyList[i], keyList[j])

html.write(html_end)
html.close()
