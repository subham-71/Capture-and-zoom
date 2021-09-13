import cv2
from cvzone.HandTrackingModule import HandDetector
import os

os.system('python cam.py')

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
startDistance = None
scale = 0
cx, cy = 500, 500
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img1 = cv2.imread("NewPicture.jpg")

    if(len(hands) == 2):
        # print(detector.fingersUp(hands[0]),detector.fingersUp(hands[1]))
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and\
                detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            # print("zoom gesture")
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            # lmList1[8],lmList2[8]
            if startDistance is None:
                length, info, img = detector.findDistance(
                    lmList1[8], lmList2[8], img)
                print(length)
                startDistance = length

            length, info, img = detector.findDistance(
                lmList1[8], lmList2[8], img)
            scale = int((length-startDistance)//2)
            cx, cy = info[4:]
            print(scale)
    else:
        startDistance = None

    try:
        h1, w1, _ = img1.shape
        newH, newW = 2*((h1+scale)//2), 2*((w1+scale)//2)
        img1 = cv2.resize(img1, (newW, newH))
        # print("cx ",cx,"cy ",cy)
        # print("h1 ",h1,"w1 ",w1)
        # print("newh ",newH,"newW ",newW)
        img[cy-60-newH//2:cy-60+newH//2, cx-newW//2:cx+newW//2] = img1
    except:
        pass
    cv2.imshow("Image", img)
    cv2.waitKey(1)
