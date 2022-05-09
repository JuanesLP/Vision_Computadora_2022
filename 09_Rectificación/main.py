import numpy as np
import cv2

originalImage = cv2.imread("rectificationImage.jpg")
img = originalImage.copy()
counter = 0
rows, cols, ch = img.shape
selectedPoints = []

print("SELECCIONE LAS ESQUINAS EN SENTIDO HORARIO, COMENZANDO CON LA ESQUINA SUPERIOR IZQUIERDA")


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


while counter != 4:
    cv2.imshow("Title of Popup Window", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('r'):
        img = originalImage.copy()

RECTIFIED_WIDTH = selectedPoints[1][0] - selectedPoints[0][0] #estos puntos son para aproximar el tamaño final de la imagen
RECTIFIED_HEIGHT = selectedPoints[3][1] - selectedPoints[0][1]

rectifiedPoints = [[0, 0], [RECTIFIED_WIDTH, 0], []]
src = np.array([selectedPoints], np.float32)
dst = np.array([[0, 0], [RECTIFIED_WIDTH, 0], [RECTIFIED_WIDTH, RECTIFIED_HEIGHT], [0, RECTIFIED_HEIGHT]], np.float32)

M = cv2.getPerspectiveTransform(src, dst)
warped = cv2.warpPerspective(originalImage, M, (RECTIFIED_WIDTH, RECTIFIED_HEIGHT))

cv2.imwrite("output.jpg", warped)

while(1):
    cv2.imshow("Title of Popup Window", warped)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
#fuente donde se buscó la solución: https://stackoverflow.com/questions/49397489/using-getperspective-in-opencv
