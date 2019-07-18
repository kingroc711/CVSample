import cv2
import platform

print("OS : ", platform.system())
print("platform : ", platform.platform())
print("version : ", platform.version())
print("arch : ", platform.architecture())
print("machine : ",  platform.machine())
print("name : ", platform.uname())
print("python vision : ", platform.python_version())
print("OpenCV Version : ", cv2.__version__)
print(cv2.getBuildInformation())

