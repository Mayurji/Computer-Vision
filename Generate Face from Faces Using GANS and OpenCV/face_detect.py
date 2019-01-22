import cv2
import numpy as np
import os
image_path = '/Users/mayurjain/Documents/Gan on Faces/Cropped/'

face_cascade = cv2.CascadeClassifier('/Users/mayurjain/Documents/Gan on Faces/haarcascade_frontalface_default.xml')

count = 0
for file in os.listdir(image_path):
    if file.endswith('.jpg'):
        img = cv2.imread(image_path+file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #for (x, y, w, h) in faces:
        #    cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #    gray_images = gray[y:y+h, x:x+w]
        cv2.imwrite('/Users/mayurjain/Documents/Gan on Faces/Mayur/mayur_' +str(count)+'.jpg', gray)
        count +=1
