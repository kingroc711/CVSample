import cv2 as cv

fileList = ['res/mohu.jpg', 'res/mohu1.jpg', 'res/mohu2.jpg',
            'res/mohu3.png', 'res/mediablur.png', 'res/jeep.jpeg']

for f in fileList:
    grayImag = cv.imread(f, 0)
    imageVar = cv.Laplacian(grayImag, cv.CV_64F).var()
    print(imageVar)