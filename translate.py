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

def translateandsave(folder):
    for subfoldername in tqdm(os.listdir(folder)):
        for imname in os.listdir(folder+"/"+subfoldername+"/D2"):
            i=imname
            subfoldername=imname[:imname.find("_")]+"/"

            try:
                img = cv2.imread(folder+"/"+subfoldername+"/D2/"+i,0)
            except IOError as e:
                print("({})".format(e))

            for tx in [0,10]:
      
                for ty in [0,10]:
                
                    if (tx==10 and ty==10):
                    	continue
      
                    # Store height and width of the image
                    height, width = img.shape[:2]
                      
                    #quarter_height, quarter_width = height / 4, width / 4
                      
                    T = np.float32([[1, 0, tx], [0, 1, ty]])
                      
                    # We use warpAffine to transform
                    # the image using the matrix, T
                    translated = cv2.warpAffine(img, T, (width, height))
                    os.makedirs("D2_3/"+subfoldername+'/D2', exist_ok=True)
                    cv2.imwrite("D2_3/"+subfoldername+"/D2/"+imname[:-4]+"_"+str(tx)+"_"+str(ty)+".jpg", translated)

translateandsave('D2_2')
