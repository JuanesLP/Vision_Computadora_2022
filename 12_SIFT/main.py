
import numpy as np
import cv2

MIN_MATCH_COUNT = 10
img1 = cv2.imread("imagen1.jpg")# Leemos la imagen 1
img2 = cv2.imread("imagen2.jpg")# Leemos la imagen 2
dscr = # Inicializamos el detector y el descriptor

kp1 , des1 = # Encontramos los puntos clave y los descriptores con SIFT en la imagen 1
kp2 , des2 = # Encontramos los puntos clave y los descriptores con SIFT en la imagen 2
matcher = cv2 . BFMatcher ( cv2 .NORM_L2)
matches = matcher . knnMatch ( des1 , des2 , k=2)
# Guardamos los buenos matches usando el test de razón de Lowe
good = [ ]
for m, n in matches :
i f m. di s t anc e < 0 . 7 * n . di s t anc e :
good . append (m)
i f ( len ( good ) > MIN_MATCH_COUNT) :
s r c _pt s = np . f l o a t 3 2 ( [ kp1 [m. queryIdx ] . pt for m in good ] ) . reshape ( −1 , 1 , 2)
ds t_pt s = np . f l o a t 3 2 ( [ kp2 [m. t r a inIdx ] . pt for m in good ] ) . reshape ( −1 , 1 , 2)
H, mask = cv2 . findHomography ( ds t_pt s , s r c_pt s , cv2 .RANSAC, 5 . 0 ) # Computamos la homografía con RANSAC
wimg2 = # Aplicamos la transformación perspectiva H a la imagen 2
# Mezclamos ambas imágenes
alpha = 0 . 5
blend = np . ar ray (wimg2 * alpha + img1 * (1 − alpha ) , dtype=np . uint8 )