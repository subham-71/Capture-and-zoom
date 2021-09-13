import cv2

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret, frame = videoCaptureObject.read()
    img1 = cv2.resize(frame, (200, 200))
    cv2.imwrite("NewPicture.jpg", img1)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
