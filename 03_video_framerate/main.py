import cv2
video = cv2.VideoCapture(0)
while True:
    fps = video.get(cv2.CAP_PROP_FPS)
    ret, frame = video.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(int(fps)) & 0xFF == ord('q'):
        break
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

video.release()
cv2.destroyAllWindows()
