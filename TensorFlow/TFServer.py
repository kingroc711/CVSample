import tensorflow as tf
import os
import numpy as np
import socket

def init_socket():
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    if os.path.exists("/tmp/tfserver.sock"):
        os.unlink("/tmp/tfserver.sock")
    server.bind("/tmp/tfserver.sock")
    server.listen(0)
    return server

def id_to_string(node_id):
    if node_id not in uid_to_human:
        return ''
    return uid_to_human[node_id]

lines = tf.gfile.GFile('./inception_model/output_labels.txt').readlines()
uid_to_human = {}
TFServer = init_socket()

for uid, line in enumerate(lines):
    line = line.strip('\n')
    uid_to_human[uid] = line

with tf.gfile.FastGFile('./inception_model/output_graph.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    while True:
        #这里等待接收用户的图片信息。
        connection, address = TFServer.accept()
        rec = connection.recv(1024)
        picPath = str(rec, encoding="utf-8")
        print (picPath)
        image_data = tf.gfile.GFile(picPath, 'rb').read()
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[::-1]
        result = ''
        for node_id in top_k:
            human_string = id_to_string(node_id)
            score = predictions[node_id]
            buf = ('%s (score = %.2f%%) \n' % (human_string, score*100))
            result = result + buf
        print(result)
        #将打分结果返回给提交打分申请的客户端
        connection.send(bytes(result, 'utf-8'))
    connection.close()

