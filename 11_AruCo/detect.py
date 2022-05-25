import cv2
import cv2 as cv
import numpy as np

# Cargamos el diccionario.
dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

# Creamos el detector
parameters = cv.aruco.DetectorParameters_create()
charmander = cv2.imread("charmander.png")
bulbasaur = cv2.imread("bulbasaur.png")
squirtle = cv2.imread("squirtle.png")

pokemons = {
    33: charmander,
    34: squirtle,
    35: bulbasaur
}


def augmented_aruco(corner, id, frame, img_aug):
    top_left = corner[0][0][0], corner[0][0][1]
    top_right = corner[0][1][0], corner[0][1][1]
    bottom_right = corner[0][2][0], corner[0][2][1]
    bottom_left = corner[0][3][0], corner[0][3][1]

    height, width, channels = img_aug.shape

    points_1 = np.array([top_left, top_right, bottom_right, bottom_left])
    points_2 = np.float32([[0,0],[width, 0],[width, height],[0, height]])

    matrix, _ = cv2.findHomography(points_2, points_1)

    img_out = cv2.warpPerspective(img_aug, matrix, (frame.shape[1], frame.shape[0]))
    cv2.fillConvexPoly(frame, points_1.astype(int), (255,255,0))
    img_out = frame + img_out

    return img_out


cap = cv.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    # Detectamos los marcadores en la imagen
    corners, ids, rejected = cv.aruco.detectMarkers(frame, dictionary, parameters=parameters)
    if ids is not None:
        count = 0
        for id in ids:
            frame = augmented_aruco(corners[count], id, frame, pokemons[int(id)])
            count = count + 1

        # Dibujamos los marcadores detectados en la imagen
        #frame = cv.aruco.drawDetectedMarkers(frame, corners, ids)

    cv.imshow("ventana", frame)
    key = cv.waitKey(50)
    if(key == 27):
        break
