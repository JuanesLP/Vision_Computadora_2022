import cv2
import numpy as np
from matplotlib import pyplot as plt

originalImage = cv2.imread("840_560.jpeg", cv2.IMREAD_COLOR)
image2 = cv2.imread("img.png", cv2.IMREAD_COLOR)
img = originalImage.copy()

# variables
selectedPoints = []
counter = 0
rows, cols, ch = img.shape

imagePoints = [[0, 0], [0, cols], [rows, cols]]


def draw_dot(event, x, y, flags, param):
    global img

    if event == cv2.EVENT_LBUTTONUP:

        cv2.circle(img, (x, y), 2, (0, 0, 255), 4)
        append_new_point([x, y])


def append_new_point(point):
    global counter
    selectedPoints.append(point)
    counter += 1
    print(selectedPoints, counter)


cv2.namedWindow(winname= "Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_dot)

while counter != 3:
    cv2.imshow("Title of Popup Window", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('r'):
        img = originalImage.copy()

pts1 = np.float32([selectedPoints])
pts2 = np.float32([imagePoints])
M = cv2.getAffineTransform(pts2, pts1)
dst = cv2.warpAffine(image2, M, (cols, rows))

grayDst = cv2.cvtColor(np.ascontiguousarray(dst), cv2.COLOR_RGB2GRAY)
(_, mask) = cv2.threshold(grayDst, 0, 255, cv2.THRESH_BINARY) #aca tiraba error, pero crea una máscara a partir
maskInv = cv2.bitwise_not(mask) #debemos invertir la mascara ya que sino quedará como una "ventana" del espacio de la 2da imagen y su transformación afin, y el resto quedará negro


maskedImage = cv2.bitwise_and(originalImage, originalImage, mask=maskInv) #ahora la imagen tiene un espacio negro que coincide con la 2da imagen transformada


finalImage = cv2.add(maskedImage, dst) #al mergearlas, ahora no se mezclaran, ya que se podria considerar el espacio de la máscara como vacío

cv2.imshow('Imagen final', finalImage)

plt.subplot(121)
plt.imshow(img)
plt.title('Input')

plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.show()

cv2.destroyAllWindows()

