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
import color3
from tqdm import tqdm

def resize(folder):
    '''
    minsum=99999999
    for j in tqdm(os.listdir(folder)):
        for i in os.listdir(folder+"/"+j+"/D2"):
            imname=i
            subfoldername=imname[:imname.find("_")]+"/"
            try:
                img = cv2.imread(folder+"/"+subfoldername+"/D2/"+i,0)
            except IOError as e:
                print("({})".format(e))

            sumi=img.shape[0]+img.shape[1]
            if sumi < minsum:
                minsum=sumi
                h=img.shape[0]
                w=img.shape[1]
                ii=i
                jj=j
    print(minsum,w,h,w*3/870,h*3/870,j)
    '''
    h=435
    w=435
    for j in tqdm(os.listdir(folder)):
        for i in os.listdir(folder+"/"+j+"/D1"):

            imname=i
            subfoldername=j#imname[:imname.find("_")]+"/"

            try:
                img = cv2.imread(folder+"/"+subfoldername+"/D1/"+i,0)
            except IOError as e:
                print("({})".format(e))


            # Store height and width of the image
            height, width = img.shape[:2]
            
            
            marginh=int((height-h)/2)
            marginw=int((width-w)/2)
            
            if height >= 435:
            	if width >= 435:
            		img=img[marginh:height-marginh,marginw:width-marginw] 
            

            		imname=i
            		os.makedirs("D1_2/"+subfoldername+"/D1/", exist_ok=True)
            		cv2.imwrite("D1_2/"+subfoldername+"/D1/"+imname, img)
            	else:
            		pass
            else:
            	pass
resize('D1_1')



