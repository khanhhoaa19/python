import cv2

histogram = []

for j in range(0, 256):
    histogram.append(0)
#print(img.shape)
for x in range(0, len(img[0])):
    for y in range(0, len(img)):
        histogram[img[y][x]] = histogram[img[y][x]] + 1
print(histogram)

