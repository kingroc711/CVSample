import  cv2
import os
import numpy as np

imgs = []
cl = []
imgPath = './Actor/zxc/'
model = cv2.face.EigenFaceRecognizer_create()
dirs = os.listdir(imgPath)
for f in dirs:
    file = imgPath + f
    img = cv2.imread(file, 0)
    imgs.append(img)
    cl.append(101)

array = np.array(cl)
model.train(imgs, array)
model.save('./XML/actor_zxc.xml')
cv2.destroyAllWindows()