from __future__ import print_function
import cv2
import numpy as np
from matplotlib import pyplot as plt
import cv2
from scipy import ndimage
import imutils
import math
import sys
import os
from tqdm import tqdm

def rotateandsave(folder):
    for i in tqdm(os.listdir(folder)):
        for j in os.listdir(folder+i+"/D2/"):
            try:
                img = cv2.imread(folder+"/"+i+'/D2/'+j,0)
            except IOError as e:
                print("({})".format(e))

            for theta in [-10,0,10]:
                rotated = imutils.rotate_bound(img, theta)

                os.makedirs("D2_2/"+i+"/D2/", exist_ok=True)
                cv2.imwrite("D2_2/"+i+"/D2/"+j[:-4]+"_"+str(theta)+".jpg", rotated)

rotateandsave('D2_1/')
