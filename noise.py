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

noiseamount=float(sys.argv[1])

def addnoise(folder):
    k=0
    for j in tqdm(os.listdir(folder)):
        for i in os.listdir(folder+"/"+j+"/D2"):
            imname=i
            subfoldername=imname[:imname.find("_")]+"/"

            try:
                img = cv2.imread(folder+"/"+subfoldername+"/D2/"+i,0)
            except IOError as e:
                print("({})".format(e))

      
            height, width = img.shape[:2]
            noise=color3.generatenoise(width,height)
            # Store height and width of the image
            #noise = noise.resize((width,height))
            noise=np.asarray(noise)
            try:
                noised=noiseamount*noise+(1-noiseamount)*img
            except:
                import pdb; pdb.set_trace()
            imname=i
            subfoldername=imname[:imname.find("_")]+"/"
            os.makedirs("D2_6"+str(noiseamount)+"/"+subfoldername+"/D2", exist_ok=True)
            cv2.imwrite("D2_6"+str(noiseamount)+"/"+subfoldername+"/D2/"+imname, noised)
            cv2.imwrite(str(k)+".png",noise)
            k+=1

addnoise('D2_5')



