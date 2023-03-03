import cv2
import numpy as np
import imutils
import math
import os
def rotate(imname):
    print("rotate",imname)
    img = cv2.imread(imname)
    rotated=img
    img = cv2.resize(img, (1200, 800))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)


    lines=cv2.HoughLines(edges,1, math.pi / 180.0, 200)
    if lines is not None:
        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            print(theta)
            img = cv2.imread(imname)
            rotated = imutils.rotate_bound(img,  math.cos(math.radians(theta)))
            #cv2.line(img ,(x1,y1),(x2,y2),(0,0,255),2)
            resized = cv2.resize(img, (1200, 800))
            #cv2.imshow('reszief2',resized)
            #cv2.waitKey(0)
            w,h,_=img.shape
            #rotated=rotated[150:w - 150,150:h - 150]
    return rotated


def main(i):
    return rotate(i)
