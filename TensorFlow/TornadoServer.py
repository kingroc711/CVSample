import tornado.ioloop
import tornado.web
import os
import time
import operator
import socket
import glob

staticFilePath = 'static'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Main")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Index")

class UploadFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('UploadFile.html')

    def getFileName(self):
        now = time.time()
        millisecond = int((now - int(now)) * 1000)
        t = time.localtime(now)
        time_str = "%d-%d-%d-%d-%d-%d-%d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, millisecond)
        return time_str

    def post(self):
        # 文件的暂存路径
        upload_path = os.path.join(os.path.dirname(__file__) + '/static', str(self.request.remote_ip))
        if(os.path.exists(upload_path) == False):
            os.makedirs(upload_path)

        file_metas = self.request.files['file']    #提取表单中‘name’为‘file’的文件元数据
        fileData = file_metas[0]
        fileName = fileData['filename']
        arr = os.path.splitext(fileName)
        extFileName = arr[len(arr) - 1]

        fileType = fileData['content_type']
        print(fileName)
        print(fileType)
        #这里判断图片是否为jpeg格式的文件，将其他格式的图片进行了过滤。
        if (operator.eq(fileType, 'image/jpeg') == False):
            self.write('请上传JPEG格式的图片!')
            return
        else:
            fileNameTime = self.getFileName()
            fileName = fileNameTime + extFileName
            fileFullName = os.path.join(upload_path, fileName)
            #将用户上传的图片进行本地化存储。
            with open(fileFullName, 'wb') as up:
                 up.write(fileData['body'])
            #self.write('finished!')

            #通过socket管道将图片路径传给Tensorflow服务器
            client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            client.connect("/tmp/tfserver.sock")
            client.send(bytes(fileFullName, 'utf-8'))

            #接收Tensorflow服务的打分数据
            resultbyte = client.recv(1024)
            resultStr = str(resultbyte, encoding="utf-8")

            n = fileFullName.find(staticFilePath)
            imagePath = fileFullName[n:]

            #将图片源文件和打分数据同时进行显示。
            htmlSource = '<!DOCTYPE html> ' \
                       + '<head> <meta charset="UTF-8"> </head> ' \
                       + '<body> ' \
                       + '<p> ' +  resultStr  + '</p>' \
                       + '<img src="' + imagePath + '"/>' \
                       + '</body>' \
                       + '</html>'
            print(htmlSource)
            self.write(htmlSource)
        return

#handlers = [(r"/", UploadFileHandler),]

setting = dict(
    #template_path = os.path.join(os.path.dirname(__file__), "temploop"),
    static_path = os.path.join(os.path.dirname(__file__), staticFilePath)
)

application = tornado.web.Application([
    (r"/main", MainHandler),
    (r"/index", IndexHandler),
    (r'/file',UploadFileHandler),
], **setting)

#application = tornado.web.Application(handlers, template_path, static_path)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()