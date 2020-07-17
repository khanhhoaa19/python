import cv2
import numpy
img = cv2.imread('D:\\q.JPG')
cv2.imshow("before", img)
a = 0.1 #a > 1 increase
for i in range(0, len(img)):
    for j in range(0, len(img[0])):
        img[i][j] = 255 * numpy.power((img[i][j]/255),(1/a))
cv2.imshow("after", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
