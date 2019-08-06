import cv2 as cv
import numpy as np
import os

html_end = '</body>\n' \
           '</html>\n'

div_string = '<div>\n' \
             '<img src="%s" />\n' \
             '<img src="%s" />\n' \
             '</div>\n\n'



def createHtml():
    html_start = '<html>\n' \
                 '<style>\n' \
                 'img{\n' \
                 'width: 200px;\n' \
                 'height: auto;\n' \
                 '}\n' \
                 '</style>\n\n' \
                 '<body>\n\n'
    html = open('./a.html', 'w')
    html.write(html_start)
    return html

def getBigCircle(file):
    img = cv.imread(file, cv.IMREAD_COLOR)
    height, width = img.shape[:2]
    print("height : " + str(height) + ', width : ' + str(width))

    img = cv.resize(img, (int(width / 2), int(height / 2)))
    cimg = img.copy()
    img = cv.medianBlur(img, 3)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.GaussianBlur(img, (5, 5), 0, 0)
    img = cv.Canny(img, 50, 200)
    # img = cv.GaussianBlur(img, (9, 9), 2, 2)
    #cv.imshow('blur', img)

    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, int(height / 2), np.array([]), param1=100, param2=30,
                              minRadius=int(height / 8), maxRadius=int(height / 2))
    circles = np.uint16(np.around(circles))
    print(circles)
    if len(circles) is not 0:
        for i in circles[0, :]:
            # draw the outer circle
            cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    #cv.imshow('circles', cimg)
    #cv.waitKey()
    #cv.destroyAllWindows()
    return cimg

def main():
    html = createHtml()
    path = './buliang'
    for filename in os.listdir(path):
        fullName = os.path.join(path, filename)
        img = getBigCircle(fullName)
        cv.imwrite(os.path.join('./out', filename), img)
        html.write(div_string % (fullName, os.path.join('./out', filename)))

    html.write(html_end)
    html.close()

if __name__ == '__main__':
    main()