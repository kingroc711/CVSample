import cv2
import os
from concurrent.futures import ThreadPoolExecutor
import threading
import psutil

import datetime

DirList = [
    '/home/king/imageNet/nsfw_data_scrapper-master/data/test/neutral/'
    # '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/drawings',
    # '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/hentai',

    #'/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/neutral',

    # '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/porn',
    # '/home/king/PycharmProjects/nsfw_data_scrapper/raw_data/sexy'
]

mutex = threading.Lock()
histMap = dict()
keyList = []


def calHist(file):
    im = cv2.imread(file, 0)

    mutex.acquire()
    histMap[file] = cv2.calcHist([im], [0], None, [256], [0, 256])
    mutex.release()


def compareHist(file):
    i = keyList.index(file)

    for j in range(i + 1, len(keyList)):
        cmp = cv2.compareHist(histMap[file], histMap[keyList[j]], cv2.HISTCMP_CHISQR_ALT)
        score = cmp * 100
        if score < 1:
            print(file, keyList[i])

    # newList = keyList[i + 1:]#可以提高CPU利用率
    # m = histMap.copy() #可以提高CPU利用率
    # for f in newList:
    #     cmp = cv2.compareHist(m[file], m[f], cv2.HISTCMP_CHISQR_ALT)
    #     score = cmp * 100
    #     if score < 1:
    #         print(file, f)


def main():
    global keyList

    fileList = []
    for path in DirList:
        for filename in os.listdir(path):
            fullName = os.path.join(path, filename)
            fileList.append(fullName)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    with ThreadPoolExecutor(psutil.cpu_count()) as executor:
        executor.map(calHist, fileList)

    print(len(histMap))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    keyList = list(histMap.keys())
########################单线程部分########################
    for i in range(len(keyList)):
        for j in range(i + 1, len(keyList)):
            cmp = cv2.compareHist(histMap[keyList[i]], histMap[keyList[j]], cv2.HISTCMP_CHISQR_ALT)
            score = cmp * 100
            #print(score)
            if score < 1:
                if os.path.exists(keyList[j]):
                    pass#os.remove(keyList[j])
                print(keyList[i], keyList[j])
###################多线程部分####################
############不知道为什么，多线程的效率没有单线程的效率高，但准确率是相同的########

    # with ThreadPoolExecutor(psutil.cpu_count()) as executor:
    #     executor.map(compareHist, keyList)



    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('finish')


if __name__ == '__main__':
    main()
