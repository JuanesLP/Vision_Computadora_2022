import numpy as np;
import cv2;

image = cv2.imread('image.jpeg')


def rotate(image, angle, center=None, scale=1.0):
    (height, width) = (image.shape[:2])
    if center is None:
        center = (width/2, height/2)

    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image


def traslate(image, x, y):
    (height, width) = (image.shape[0], image.shape[1])

    rotation_matrix = np.float32([[1, 0, x],[0, 1, y]]);

    shifted_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return shifted_image;


rotated_image = rotate(image, 90)

eculid_transformated_image = traslate(rotated_image, 100, 100)

cv2.imshow('resultado', eculid_transformated_image)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('resultado.png', eculid_transformated_image)
else:
    cv2.destroyAllWindows()

