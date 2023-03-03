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


def cropandsave(D0,templatename):
    for imname in tqdm(os.listdir(D0)):
    
        try:
            #print(imname)
            img = cv2.imread(D0+imname,0)
            #img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img3 = img[:]#cv2.imread(imname)
            template = cv2.imread(templatename,0)
        except IOError as e:
            print("({})".format(e))
        else:
            img2 = img.copy()
            w, h = template.shape[::-1]

        # All the 6 methods for comparison in a list
            methods = ['cv2.TM_CCOEFF']

            #, 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            #         'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

        for meth in methods:
            img = img2.copy()
            method = eval(meth)

            # Apply template Matching
            maxval=0
            for theta in range(0,1):#-20,21):
                rotated = imutils.rotate_bound(img, math.cos(math.radians(theta)))

                
                res = cv2.matchTemplate(img,template,method)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                if max_val > maxval:
                    thetatmp=theta
                    maxval=max_val
            img = imutils.rotate_bound(img, math.cos(math.radians(thetatmp)))
            res = cv2.matchTemplate(img, template, method);
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            #print(imname)
            #print(" ")
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = (min_loc[0] -150,min_loc[1]-150)
            else:
                top_left = (max_loc[0] -50,max_loc[1]-50)
            #bottom_right = (top_left[0] + w +150, top_left[1] + h+150)

            #cv2.rectangle(img,top_left, bottom_right, 255, 2)

            '''
            plt.subplot(121),plt.imshow(res,cmap = 'gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(img,cmap = 'gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth) #; plt.legend([min_val, max_val, min_loc, max_loc], ["min_val", "max_val", "min_loc", "max_loc"])
            
            plt.show()
            '''

            cropsize=0
            w+=50
            h+=50
            box = img3[top_left[1]+cropsize:top_left[1]+h-cropsize,top_left[0]+cropsize:top_left[0] + w-cropsize]
            #cv2.imshow(imname,cv2.resize(box, (round(w * 0.5), round(h * 0.5))))
            #cv2.waitKey(0)
            
            #imname=sys.argv[1]
            subfoldername=imname[:imname.find("_")]+"/"
            imname=imname.replace("_raw","")     
            os.makedirs("D2_1/"+subfoldername+'D2', exist_ok=True)
            cv2.imwrite("D2_1/"+subfoldername+"D2/"+imname, box)

            
            cropsize=150
            box = img3[top_left[1]+cropsize:top_left[1]+h-cropsize,top_left[0]+cropsize:top_left[0] + w-cropsize]
            os.makedirs("D1_1/"+subfoldername+"/D1", exist_ok=True)
            cv2.imwrite("D1_1/"+subfoldername+"/D1/"+imname, box)

import rotate as rt

templatename='template7.JPG'
cropandsave('D0/',templatename)
