import numpy as np;
import cv2;

image = cv2.imread('image.jpeg')

def traslation(image, x, y):
    (height, width) = (image.shape[0], image.shape[1])

    rotation_matrix = np.float32([[1, 0, x],[0, 1, y]]);

    shifted_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return shifted_image;


result = traslation(image, 100, 100)

cv2.imshow('resultado', result)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('resultado.png', image)
else:
    cv2.destroyAllWindows()

