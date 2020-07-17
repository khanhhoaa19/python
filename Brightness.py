# from PIL import Image, ImageEnhance
# img = Image.open("D:\\test.jpg")
# enhancer = ImageEnhance.Brightness(img)
# # Lighter
# increaseBrightnessImage = enhancer.enhance(10)
# # Darker
# degreaseBrightnessImage = enhancer.enhance(-10)
# increaseBrightnessImage.show()
# degreaseBrightnessImage.show()
# import cv2
# img = cv2.imread('D:\\test.JPG')
# for i in range(0, len(img)):
#     for j in range(0, len(img[0])):
#         img[i][j] = img[i][j] - 10
# cv2.imshow("Display", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
img = cv2.imread("D:\\abcd.JPG")
#print(img.shape)
cv2.imshow('before',img)
print(img)
value = 20
img = np.asarray(img, dtype=float)
# print(min(np.min(img)))
# print(max(np.max(img)))

# cv2.imshow('After 1', img2 + value)
c = 0
for i in range(len(img)):
    for j in range(len(img[0])):
        for k in range(3):
            img[i,j,k] += value
            if(img[i,j,k] > 255):
                img[i,j,k] = 255
                c+=1
print(c)
cv2.imshow("After", img/255.0)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
