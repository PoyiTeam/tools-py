import cv2


cap = cv2.VideoCapture('To be continued.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    bgr = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    # cv2.imshow('frame', gray)
    cv2.imshow('frame',  bgr)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
