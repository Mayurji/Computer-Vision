import cv2
import numpy as np
import os
from openCV import flipping
image_path = '/Users/mayurjain/Documents/Gan on Faces/Mayur/'

count = 41
for file in os.listdir(image_path):
    if file.endswith('.jpg'):
        img = cv2.imread(image_path+file)
        flipping(img,1,num=count)
        count +=1
