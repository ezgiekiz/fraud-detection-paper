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

    for j in tqdm(os.listdir(folder)):
        for i in os.listdir(folder+"/"+j+"/D2"):
            imname=i

            try:
                img = cv2.imread(folder+"/"+j+"/D2/"+i,0)
            except IOError as e:
                print("({})".format(e))

      
            # Store height and width of the image
            height, width = img.shape[:2]
            cropsize=150
            cropped = img[cropsize:width-cropsize,cropsize:height-cropsize]
            imname=i
            subfoldername=imname[:imname.find("_")]+"/"
            os.makedirs("D2_4/"+j+'/D2', exist_ok=True)
            try:
                cv2.imwrite("D2_4/"+j+"/D2/"+imname, cropped)
            except:
                pass
rotateandsave('D2_3')
