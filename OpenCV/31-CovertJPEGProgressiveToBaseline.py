import cv2
import os
import string
from PIL import Image

file_dir = './res/'

def progressive_to_baseline(path, file):
    tmpfile = 'tmp' + file
    print(tmpfile)
    img = cv2.imread(path + file)

    cv2.imwrite(path + tmpfile, img)
    os.remove(path + file)
    os.rename(path + tmpfile, path + file)

for file in os.listdir(file_dir):
    #ret = os.system('identify -verbose ' + file_dir + file + ' | grep Interlace')
    ret = os.popen('file ' + file_dir + file)
    lines = ret.readlines()
    if 'progressive,' in str(lines):
        print(file_dir + file)
        progressive_to_baseline(file_dir, file)
