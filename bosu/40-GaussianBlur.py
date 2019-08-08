import cv2 as cv
import numpy as np
import os

html_end = '</body>\n' \
           '</html>\n'

div_string = '<div>\n' \
             '<img src="%s" />\n' \
             '<img src="%s" />\n' \
             '</div>\n\n'



def createHtml(path):
    html_start = '<html>\n' \
                 '<style>\n' \
                 'img{\n' \
                 'width: 400px;\n' \
                 'height: auto;\n' \
                 '}\n' \
                 '</style>\n\n' \
                 '<body>\n\n'
    html = open(path + '.html', 'w')
    html.write(html_start)
    return html

def getBigCircle(file, downthreshold=0):
    img = cv.imread(file, cv.IMREAD_COLOR)
    height, width = img.shape[:2]
    #print("height : " + str(height) + ', width : ' + str(width))

    img = cv.resize(img, (int(width / 2), int(height / 2)))
    cimg = img.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img, 7)
    #img = cv.GaussianBlur(img, (5, 5), 0, 0)
    img = cv.Canny(img, 100 - downthreshold/2, 200 - downthreshold)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, int(height / 2), np.array([]), param1=100, param2=50,
                              minRadius=int(height / 8), maxRadius=int(height / 4))
    circles = np.uint16(np.around(circles))
    print(circles, file)
    if len(circles) is not 0:
        for i in circles[0, :]:
            if int(i[0]) - int(i[2]) > 0 and int(i[0]) + int(i[2]) < width / 2 and int(i[1]) - int(i[2]) > 0 and int(i[1]) + int(i[2]) < height / 2:
                # draw the outer circle
                cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
                cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
            else:
                return None
    else:
        return None

    return cimg

def main():
    path = './quejiao'
    html = createHtml(path)
    for filename in os.listdir(path):
        fullName = os.path.join(path, filename)
        global img
        for i in range(4):
            img = getBigCircle(fullName, downthreshold=40*i)
            if img is not None:
                cv.imwrite(os.path.join('./out', filename), img)
                html.write(div_string % (fullName, os.path.join('./out', filename)))
                break
        if img is None:
            html.write(div_string % (fullName, fullName))

    html.write(html_end)
    html.close()
    cv.waitKey()

if __name__ == '__main__':
    main()