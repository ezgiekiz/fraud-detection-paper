import math 
import numpy as np
from PIL import Image 
from random import randint

def generatenoise(W,H):
    im = Image.new('RGB', (W, H)).convert('L')
    ld = im.load()

    heatmap = [

        [0, (0.5, 0.5,0.5)],
        [0, (0.5, 0.5, 0.5)],
    ]

    # x y coordinates of starting point for gradient
    t=randint(0,1)
    p=randint(0,1)
    if t:
        start_x = randint(0,im.size[0])
        start_y = [0,im.size[1]][p]
    else:
        start_y = randint(0,im.size[1])
        start_x = [0,im.size[0]][p]


    for x in range(im.size[0]):
        for y in range(im.size[1]):
            dist = math.sqrt(math.pow(start_x - x,2) + math.pow(start_y - y,2))
            start_rgb = heatmap[0][1]
            end_rgb = heatmap[1][1]
            dist = dist / (math.sqrt(math.pow(im.size[0],2) + math.pow(im.size[1],2))) 
            b = map(lambda x,y: x+y, map(lambda a: a*(1-dist/3), start_rgb), map(lambda b: b*(1-dist/3), end_rgb))
            b = [int(256 * v) for v in (b)]
            ld[x, y] = b[0]


    '''
    print(start_x,start_y)
    start_x=0
    start_y=0
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            dist = math.fabs(start_x - x) + math.fabs(start_y - y)
            start_rgb = heatmap[0][1]
            end_rgb = heatmap[1][1]
            dist = dist / (im.size[0] + im.size[1])
            b = map(lambda x,y: x+y, map(lambda a: a*dist, start_rgb), map(lambda b: b*dist, end_rgb))
            b = [int(256 * v) for v in b]
            ld[x, y] = b
    '''
    return im

