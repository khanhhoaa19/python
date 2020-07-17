import cv2
img = cv2.imread('D:\\abcd.JPG')
#print(img.shape)
cv2.imshow('before',img)

a = 5 #a > 1 increase
s = 128 #centerpointofconstrast
for i in range(len(img)):
    for j in range(len(img[0])):
        for k in range(3):
            img[i,j,k] = a*(img[i,j,k] -s) + s
            if(img[i,j,k] <0) :
                img[i,j,k] = 0
            elif(img[i,j,k] >255):
                 img[i,j,k] = 255
cv2.imshow("after", img)
cv2.waitKey(0)
cv2.destroyAllWindows()