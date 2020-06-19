from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
import sys
import glob
import numpy as np
import cv2 as cv

def c_i_t_a():
    folder = "/Users/mayurjain/Documents/Gan on Faces/Mayur/"
    count = 0
    for f in os.listdir(folder):
        count +=1
    print(count)
    onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    #[f for f in glob.glob(folder+'*.jpg')]
    print(onlyfiles)

    print("Working with {0} images".format(len(onlyfiles)))
    train_files = []
    y_train = []
    i=0
    for _file in onlyfiles:
        train_files.append(_file)
        #label_in_file = _file.find("_")
        #y_train.append(int(_file[0:label_in_file]))

    print("Files in train_files: %d" % len(train_files))

    # Original Dimensions
    image_width = 300
    image_height = 300
    channels = 1
    nb_classes = 1

    dataset = np.ndarray(shape=(len(train_files), channels, image_height, image_width),
                         dtype=np.float32)

    i = 0
    for _file in train_files:
        #img = load_img(folder + "/" + _file)  # this is a PIL image
        # img1 = cv2.imread(folder + "/" + _file)
        # print(_file)
        # print(img1.shape)
        #img.thumbnail((image_width, image_height))
        # Convert to Numpy Array
        try:
            image = cv.imread(folder + "/" + _file,0)
            print(image.shape)
            x = img_to_array(image)  
            #print(x.shape)
            x = np.moveaxis(x, -1, 0)
            #print(x.shape)
            #x = x.reshape((1,89,89))
            # Normalize
            #x = (x - 128.0) / 128.0
            dataset[i] = x
        except Exception as e:
            print(e)
            continue
    return dataset

#c_i_t_a()
