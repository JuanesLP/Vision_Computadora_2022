
import numpy as np
import cv2

MIN_MATCH_COUNT = 30
img1 = cv2.imread("img1.jpeg")# Leemos la imagen 1
convert1 = cv2.resize(img1,(800,600), interpolation=cv2.INTER_CUBIC)

img2 = cv2.imread("img2.jpeg")# Leemos la imagen 2
convert2 = cv2.resize(img2,(800,600), interpolation=cv2.INTER_CUBIC)


dscr = cv2.SIFT_create()# Inicializamos el detector y el descriptor

kp1 , des1 = dscr.detectAndCompute(convert1,None)# Encontramos los puntos clave y los descriptores con SIFT en la imagen 1
kp2 , des2 = dscr.detectAndCompute(convert2,None)# Encontramos los puntos clave y los descriptores con SIFT en la imagen 2

matcher = cv2.BFMatcher(cv2.NORM_L2)
matches = matcher.knnMatch(des1, des2, k=2)
# Guardamos los buenos matches usando el test de razón de Lowe
good = [ ]
for m, n in matches:
    if m.distance < 0.8 * n.distance:
        good.append(m)
if(len(good) > MIN_MATCH_COUNT):
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0) # Computamos la homografía con RANSAC



wimg2 = cv2.warpPerspective(convert2, H, (800,600))


# Mezclamos ambas imágenes
alpha = 0.5

blend = np.array(wimg2 * alpha + convert1 * (1 - alpha), dtype=np.uint8)

while(1):
    cv2.imshow("final", blend)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
