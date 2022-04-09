import cv2

videoInput = cv2.VideoCapture(0)
videoFourcc = cv2.VideoWriter_fourcc(*'XVID')
videoOutput = None

isFirst = True
while True:
    fps = videoInput.get(cv2.CAP_PROP_FPS)
    ret, frame = videoInput.read()

    if isFirst:
        fps = videoInput.get(cv2.CAP_PROP_FPS)
        #width, height, dimension = frame.shape
        width = videoInput.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = videoInput.get(cv2.CAP_PROP_FRAME_HEIGHT)
        videoOutput = cv2.VideoWriter('Output01.avi', videoFourcc, fps, (int(width), int(height)), True)
        isFirst = False

    if ret is True:
        videoOutput.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(int(fps)) & 0xFF == ord('q'):
            break
    else:
        break




videoInput.release()
videoOutput.release()
cv2.destroyAllWindows()