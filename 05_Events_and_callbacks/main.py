import cv2


orig = cv2.imread("840_560.jpeg")
img = orig.copy()
drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press ’m’ to toggle to curve




# variables
ix = -1
iy = -1
drawing = False
fx = -1
fy = -1

def draw_reactangle_with_drag(event, x, y, flags, param):
    global fx, fy, ix, iy, drawing, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y


    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = cv2.imread("840_560.jpeg")
            if mode is True:
                cv2.rectangle(img, pt1=(ix,iy), pt2=(x, y),color=(0,0,255),thickness=5)
                #img = img2
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        img = cv2.imread("840_560.jpeg")
        if mode is True:
            cv2.rectangle(img, pt1=(ix,iy), pt2=(x, y),color=(0,0,255),thickness=5)
            fx = x
            fy = y
            #img = img2
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), 1)
            fx = x
            fy = y


cv2.namedWindow(winname= "Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_reactangle_with_drag)

while True:
    cv2.imshow("Title of Popup Window", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    elif k == ord('r'):
        img = orig.copy()
    elif k == ord('g'):
        print(iy,fy,ix,fx)
        crop_img = img[iy:fy, ix:fx]
        cv2.imshow("cropped", crop_img)
        cv2.imwrite("resultado.jpeg", crop_img)
        if cv2.waitKey(0) & 0xFF == 27:
            cv2.destroyWindow("cropped")





cv2.destroyAllWindows()

