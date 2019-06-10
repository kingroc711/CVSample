import cv2
import time
import numpy as np
import os
import socket


from threading import Thread

#用于控制线程的停止
threadStop = False

#我的屏幕分辨率，这里是写死的了，没有动态获取。
windowHigh = 1080
windowWidth = 1920

#我用来测试的直播地址，都是localhost开头的，证明我在本地搭建的服务器。
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


#同时监控显示9路视频流，每个视频流是一个线程。
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
            time.sleep(0.1)

            #创建sock链接，用于将抽帧的图片发给Tensorflow服务器。
            client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            client.connect("/tmp/tfserver.sock")
            client.send(bytes(fileFullName, 'utf-8'))

            #等待获取打分结果。
            resultbyte = client.recv(1024)
            resultStr = str(resultbyte, encoding="utf-8")
            splitString = resultStr.split('\n')

            #获得的打分，我只要第一个。因为第一个分值是最高的。
            print('aaaaaaaaaaaaaaaaaaaaaaaaa : ' + splitString[0])

            img = cv2.imread(fileFullName)

            img_w = (int)(windowWidth/3)
            img_h = (int)(windowHigh/3)

            print(img_w, img_h)

            #对抽出的帧，做缩放，适合同时在一个屏幕中显示这9路视频流。
            reSize = cv2.resize(img, (img_w, img_h), interpolation=cv2.INTER_CUBIC)

            score = splitString[0].split('=')[1].strip()
            print('get score string : ' + score)
            score = score.split('.')[0]

            print('get score : ' + score)

            if(int(score) > 50):
                #这里根据分值的不同，显示不同的颜色
                if(splitString[0].startswith('porn')):
                    cv2.putText(reSize, splitString[0], (30, 60), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)
                elif(splitString[0].startswith('neutral')):
                    cv2.putText(reSize, splitString[0], (30, 60), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1)
                elif(splitString[0].startswith('sexy')):
                    cv2.putText(reSize, splitString[0], (30, 60), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 1)
                else:
                    cv2.putText(reSize, splitString[0], (30, 60), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 1)

            board_x = (int)(self.args/3)
            board_y = self.args%3

            start_x = board_x*img_h
            start_y = board_y*img_w
            print(self.args, board_x, board_y, start_x, start_y, img_w, img_h)

            #现在显示到屏幕上的不同区域上。
            bgrImage[start_x:start_x+img_h, start_y:start_y+img_w] = reSize

        print('Tread : ' + str(self.args) + ', ' + self.name + ' stop')

#生成一个比较大的画板，用于绘制这9路视频。
randomByteArray = bytearray(os.urandom(windowWidth*windowHigh*3))
flatNumpyArray = np.array(randomByteArray)
bgrImage = flatNumpyArray.reshape(windowHigh, windowWidth, 3)

#创建9个线性，每个线程去读取一个直播流。
for i in range(9):
    t = MonitorThread(name='monitor', args=(i))
    t.start()

cv2.namedWindow('image', cv2.WINDOW_FULLSCREEN)
#cv2.setWindowProperty('image', cv2.)
while True:
    if cv2.waitKey(1) == 27:
        break
    #这里就是每隔0.1秒显示一次画板。
    time.sleep(0.1)
    cv2.imshow('image', bgrImage)

#标注线程结束，线程停止循环读取数据。
threadStop = True
#销毁窗口。
cv2.destroyAllWindows()