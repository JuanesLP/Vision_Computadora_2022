import cv2

image = cv2.imread('butterfly.jpg', 0)
threshold = 230

for height, line in enumerate(image):
    for width, pixel in enumerate(line):
        if pixel >= threshold:
            image[height, width] = 255
        else:
            image[height, width] = 0

cv2.imwrite('resultado.png', image)
