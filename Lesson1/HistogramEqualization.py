import cv2
img = cv2.imread('D:\\q.JPG')
cv2.imshow("Before", img)
for i in range(0, 255):
    for j in range(0, 255):
        for k in range(0, 255):
