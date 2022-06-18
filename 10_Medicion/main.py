import numpy as np
import cv2
import  math

originalImage = cv2.imread("test.jpeg")
originalImage = cv2.resize(originalImage,(800,600), interpolation=cv2.INTER_CUBIC)
img = originalImage.copy()
counter = 0
rows, cols, ch = img.shape
selectedPoints = []
window = ""
index = 0
height = 2.10
width = 0.83

print("SELECCIONE LAS ESQUINAS EN SENTIDO HORARIO DE LA PUERTA, COMENZANDO CON LA ESQUINA SUPERIOR IZQUIERDA")


def draw_dot(event, x, y, flags, param):
    global img
    global window
    global counter

    if event == cv2.EVENT_LBUTTONUP:
        if window == "Points" or window == "Mesure" and counter < 2:
            cv2.circle(img, (x, y), 2, (0, 0, 255), 4)
            append_new_point([x, y])


def append_new_point(point):
    global counter
    selectedPoints.append(point)
    counter += 1
    print(selectedPoints, counter)


cv2.namedWindow(winname= "Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_dot)
window = "Points"

while counter != 4:
    cv2.imshow("Title of Popup Window", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('r'):
        img = originalImage.copy()

RECTIFIED_WIDTH = selectedPoints[1][0] - selectedPoints[0][0] #estos puntos son para aproximar el tamaño final de la imagen
RECTIFIED_HEIGHT = selectedPoints[3][1] - selectedPoints[0][1]

WIDTH_DISTANCE = math.sqrt(math.pow(selectedPoints[1][0] - selectedPoints[0][0],2) + math.pow(selectedPoints[1][1] - selectedPoints[0][1],2))
HEIGHT_DISTANCE = math.sqrt(math.pow(selectedPoints[3][0] - selectedPoints[0][0],2) + math.pow(selectedPoints[3][1] - selectedPoints[0][1],2))

rate = (RECTIFIED_WIDTH / WIDTH_DISTANCE)

print(WIDTH_DISTANCE,HEIGHT_DISTANCE,rate)

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
        cv2.destroyWindow("Title of Popup Window")
        break

counter = 0
selectedPoints.clear()
cv2.namedWindow(winname= "Mesure")
cv2.setMouseCallback("Mesure", draw_dot)
img = originalImage.copy()
window = "Mesure"

while(1):
    while counter < 2:
        cv2.imshow("Mesure", img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        elif k == ord('r'):
            img = originalImage.copy()
            counter = 0
    cv2.imshow("Mesure", img)
    if counter > 2:
        counter = 2
        del selectedPoints[2:len(selectedPoints) - 1]

    mesured_distance = math.sqrt(
        math.pow(selectedPoints[1][0] - selectedPoints[0][0], 2) + math.pow(selectedPoints[1][1] - selectedPoints[0][1],
                                                                            2))

    final_mesure = mesured_distance * width / WIDTH_DISTANCE



    if final_mesure > 0:
        x = ((selectedPoints[1][0] - selectedPoints[0][0]) / 2) + selectedPoints[0][0]
        y = ((selectedPoints[1][1] - selectedPoints[0][1]) / 2) + selectedPoints[0][1]
        final = str(round(final_mesure * rate,4))
        img2 = img.copy()
        cv2.putText(img2,final, (int(x), int(y)), 1, 0.75, (0,0,0),1,cv2.LINE_AA)
        #cv2.addText(img,final,(x, y),1,1,(0,255,0),1,1,1)
        cv2.imshow("Mesure", img2)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    if key == ord('r'):
        img = originalImage.copy()
        counter = 0
        selectedPoints.clear()

#fuente donde se buscó la solución: https://stackoverflow.com/questions/49397489/using-getperspective-in-opencv
