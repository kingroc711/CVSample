from PIL import Image
from pylab import *

# 读取图片信息到数组中
im = array(Image.open('./res/aero3.jpg'))

# 绘制图像
imshow(im)

# 随意给的一些点
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# 使用红色-星状标记需要绘制的点
plot(x, y, 'r*')

# 将数组中的前两个点进行连线
plot(x[:2], y[:2])

# 添加标题信息
title('Plotting: "empire.jpg"')

# 隐藏坐标轴
# axis('off')

# 显示到屏幕窗口
show()
