import cv2
import time
import numpy as np
import os
import socket


from threading import Thread

threadStop = False
windowHigh = 1080
windowWidth = 1920

videoList = ['rtmp://localhost/vod/sample1.mp4',
             'rtmp://localhost/vod/sample2.mp4',
             'rtmp://localhost/vod/sample3.mp4',

             'rtmp://localhost/vod/sample4.mp4',
             'rtmp://localhost/vod/sample5.mp4',
             'rtmp://localhost/vod/sample9.mp4',

             'rtmp://localhost/vod/sample6.mp4',
             'rtmp://localhost/vod/sample7.mp4',
             'rtmp://localhost/vod/sample8.mp4']

def getVideoURL(num):
    return videoList[num]

class MonitorThread(Thread):

    def __init__(self, name, args):
        super().__init__()
        self.name = name
        self.args = args
        self.cameraCapture = cv2.VideoCapture(getVideoURL(self.args))
        print('Thread : ' + str(self.args) + ', ' + self.name + ' start')

    def run(self):
        while threadStop is not True:
            success, frame = self.cameraCapture.read()
            fileFullName = 'pic/' + str(self.args) + '.jpg'
            cv2.imwrite(fileFullName, frame)
            time.sleep(0.05)

            #sock
            client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            client.connect("/tmp/tfserver.sock")
            client.send(bytes(fileFullName, 'utf-8'))
            resultbyte = client.recv(1024)
            resultStr = str(resultbyte, encoding="utf-8")
            splitString = resultStr.split('\n')
            print('aaaaaaaaaaaaaaaaaaaaaaaaa : ' + splitString[0])

            img = cv2.imread('pic/' + str(self.args) + '.jpg')

            img_w = (int)(windowWidth/3)
            img_h = (int)(windowHigh/3)

            print(img_w, img_h)

            reSize = cv2.resize(img, (img_w, img_h), interpolation=cv2.INTER_CUBIC)
            cv2.putText(reSize, splitString[0], (0, 60), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)

            board_x = (int)(self.args/3)
            board_y = self.args%3

            start_x = board_x*img_h
            start_y = board_y*img_w
            print(self.args, board_x, board_y, start_x, start_y, img_w, img_h)

            bgrImage[start_x:start_x+img_h, start_y:start_y+img_w] = reSize

        print('Tread : ' + str(self.args) + ', ' + self.name + ' stop')

randomByteArray = bytearray(os.urandom(windowWidth*windowHigh*3))
flatNumpyArray = np.array(randomByteArray)
bgrImage = flatNumpyArray.reshape(windowHigh, windowWidth, 3)

for i in range(6):
    t = MonitorThread(name='monitor', args=(i))
    t.start()

cv2.namedWindow('image', cv2.WINDOW_FULLSCREEN)
#cv2.setWindowProperty('image', cv2.)
while True:
    if cv2.waitKey(1) == 27:
        break
    time.sleep(0.05)
    cv2.imshow('image', bgrImage)

threadStop = True
cv2.destroyAllWindows()