import cv2 as cv

row = 15
column = 15

org_img = cv.imread('D:\code\wangpeng58\lockscreenruninbrower\/005.jpg')
height, width = org_img.shape[:2]
print('height %d widht %d' % (height, width))

row_step = (int)(height/row)
column_step = (int)(width/column)

print('row step %d col step %d'% (row_step, column_step))

print('height %d widht %d' % (row_step*row, column_step*column))

img = org_img[0:row_step*row, 0:column_step*column]

for i in range(row):
    for j in range(column):
        # pic_name = "D:\PycharmProjects\CVSample\OpenCV\out" + '\\' + str(i) + "_" + str(j) + ".jpeg"
        pic_name = "D:\code\wangpeng58\lockscreenruninbrower\wallpager/n15x15/5" + '\\' + str(i) + "_" + str(j) + ".jpeg"
        tmp_img = img[(i*row_step):(i*row_step+row_step), (j*column_step):(j*column_step)+column_step]
        cv.imwrite(pic_name, tmp_img)



