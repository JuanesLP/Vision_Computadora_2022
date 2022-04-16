import numpy as np;
import cv2;

image = cv2.imread('image.jpeg')


def rotate(img, angle, center=None, scale=1.0):
    (height, width) = (img.shape[:2])

    if center is None:
        center = (width/2, height/2)

    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))

    return rotated_image


def traslate(img, x, y):
    (height, width) = (img.shape[0], img.shape[1])

    rotation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    shifted_image = cv2.warpAffine(img, rotation_matrix, (width, height))

    return shifted_image;


def euclid_transformation(img, angle, x_traslation, y_traslation):
    rotated = rotate(img, angle);
    euclid = traslate(rotated, x_traslation, y_traslation)

    return euclid


eculid_transformated_image = euclid_transformation(image, 35, 30, 20)

cv2.imshow('resultado', eculid_transformated_image)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('resultado.png', eculid_transformated_image)
else:
    cv2.destroyAllWindows()

