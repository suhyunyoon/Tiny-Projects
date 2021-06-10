import cv2
import sys
import os
import numpy as np

'''
img = cv2.imread(os.path.join(os.path.dirname(os.path.realpath(__file__)),'cat.bmp'))

if img is None:
    print('Image load failed')
    sys.exit()

#img = cv2.bitwise_not(img)


cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
'''
xml = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(os.path.join(os.path.dirname(os.path.realpath(__file__)),xml))
rgbNum = [(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(255, 0, 255),(0, 255, 255)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)

    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(g, 1.05, 5)

    if len(faces):
        for i, (x,y,w,h) in enumerate(faces):
            cv2.rectangle(frame, (x,y), (x+w, y+h), rgbNum[i], 2)

    cv2.imshow("VideoFrame", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # Esc 키를 누르면 종료
        break

capture.release()
cv2.destroyAllWindows()