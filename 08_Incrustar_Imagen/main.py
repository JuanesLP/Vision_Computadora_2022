import cv2


orig = cv2.imread("840_560.jpeg")
img = orig.copy()





# variables



def draw_dot(event, x, y, flags, param):
    global img

    if event == cv2.EVENT_LBUTTONUP:

        cv2.circle(img, (x, y), 2, (0, 0, 255), 4)



cv2.namedWindow(winname= "Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_dot)

while True:
    cv2.imshow("Title of Popup Window", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('r'):
        img = orig.copy()
    elif k == ord('g'):
        print(iy, fy, ix, fx)
        crop_img = img[iy:fy, ix:fx]
        cv2.imshow("cropped", crop_img)
        cv2.imwrite("resultado.jpeg", crop_img)
        if cv2.waitKey(0) & 0xFF == 27:
            cv2.destroyWindow("cropped")





cv2.destroyAllWindows()

