import cv2 as cv
import numpy as np

fileList = ['./res/hashsame.jpeg', './res/hashsame1.jpeg', './res/hashsame2.jpeg', './res/hashsame3.jpeg',
            './res/face.jpeg']

def hashAVGComp(imgList):
    hashList = []
    for img in imgList:
        avg = np.mean(img)
        #小于均值的值0
        img[img <= avg] = 0
        #大于均值的值1
        img[img > avg] = 1
        hashList.append(img.flatten())

    for i in range(len(hashList)):
        for j in range(i + 1, len(hashList)):
            # 这里的与运算就是查找相同位置为1的，sum统计总共有几个。
            print(np.sum(hashList[i] & hashList[j]), fileList[i], fileList[j])

def hashSubComp(imgList):
    hashList = []
    for img in imgList:
        fla = img.flatten()
        # 这里比较奇妙，也没理由，如果自身大于后一个，值1，否则值0 例如：【10， 20， 5， 100】转换过完为【0， 1， 0， 1】，最后一个为没得比较直接设置成了1。
        for i in range(len(fla) - 1):
            if fla[i] <= fla[i+1]:
                fla[i] = 0
            else:
                fla[i] = 1
        fla[i+1] = 0
        hashList.append(fla)

    for i in range(len(hashList)):
        for j in range(i + 1, len(hashList)):
            print(np.sum(hashList[i] & hashList[j]), fileList[i], fileList[j])

def main():
    imgList = []
    for f in fileList:
        #图片以灰度单通道的方式加载
        img = cv.imread(f, 0)
        imgList.append(cv.resize(img, (8, 8), cv.INTER_CUBIC))

    hashSubComp(imgList)
    print('****************')
    hashAVGComp(imgList)

if __name__ == "__main__":
    main()
