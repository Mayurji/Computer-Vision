
#-*- coding: utf-8 -*-

#import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
import random

#sample input image
#$ python load_display_save.py --image ../images/trex.png
###### Main Function ######
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True,
# help = "Path to the image")
# args = vars(ap.parse_args())
def required_size(image,old_size,desired_size):
    #if old_size != desired_size:
    ratio = float(desired_size)/max(old_size)
    updated_size = tuple([int(x*ratio) for x in old_size])
    img = cv2.resize(image, (updated_size[1], updated_size[0]))
    delta_w = desired_size - updated_size[1]
    delta_h = desired_size - updated_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    color = [0, 0, 0]
    new_im = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)
    #else:
    #    pass
    #print(new_im.shape[1])
    #print(new_im.shape[0])
    #cv2.imshow("image", new_im)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #print(ratio)
    return 0
    

def load_display(image,req_size):
    #image = cv2.imread(args["image"])
    image = cv2.imread(image)
    #desired_size = 500
    print("width: %d pixels" % (image.shape[1]))
    print("height: %d pixels" % (image.shape[0]))
    #old_size = image.shape[:2]
    #required_size(image,old_size,req_size)
    #print("channels: %d" % (image.shape[2]))
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)
    return 0

def write(image):
    ## change the path for image if required.
    cv2.imwrite("newimage.jpg", image)

def accessing_pixels(image):
    (b, g, r) = image[0, 0]
    print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))
    image[0, 0] = (0, 0, 255)
    (b, g, r) = image[0, 0]
    print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

def getting_setting_pixel(image):
    corner = image[0:100, 0:100]
    cv2.imshow("Corner", corner)
    image[0:100, 0:100] = (0, 255, 0)
    cv2.imshow("Updated", image)
    cv2.waitKey(0)

def drawing_rectangle(image):
    canvas = np.zeros((300, 300, 3), dtype = "uint8")
    green = (0, 255, 0)
    cv2.line(canvas, (0, 0), (300, 300), green)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    red = (0, 0, 255)
    cv2.line(canvas, (300, 0), (0, 300), red, 3)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    cv2.rectangle(canvas, (10, 10), (60, 60), green)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    blue = (255, 0, 0)
    cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

def drawing_circle(image):
    canvas = np.zeros((300, 300, 3), dtype = "uint8")
    (centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)
    white = (255, 255, 255)

    for r in range(0, 175, 25):
        cv2.circle(canvas, (centerX, centerY), r, white)

    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)


    
    for i in range(0, 25):
        radius = np.random.randint(5, high = 200)
        color = np.random.randint(0, high = 256, size = (3,)).tolist()
        pt = np.random.randint(0, high = 300, size = (2,))
        cv2.circle(canvas, tuple(pt), radius, color, -1)
    
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

def translate(image, x, y):
    M = np.float([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.
    shape[0]))

    return shifted

def translation(image):
    shifted = translate(image, 0, 100)
    cv2.imshow("Shifted Down", shifted)
    cv2.waitKey(0)

def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    
    return rotated

def rotation(image):
    rotated = rotate(image, 180)
    
    #cv2.imshow("Rotated by 180 Degrees", rotated)
    #cv2.waitKey(0)
    

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)
    return resized


def resized(image):
    resized = resize(image, width = 100)
    cv2.imshow("Resized via function:", resized)
    cv2.waitKey(0)

def flipping(image,direction,num):
    #image = cv2.imread(image)
    #cv2.imshow("Original", image)

    flipped = cv2.flip(image, direction) # 1 - horizontal flip, 0 - vertical flip , -1 flipped completely
    #cv2.imshow("Flipped ", flipped)
    cv2.imwrite("mayur_"+str(num)+".jpg",flipped)

def cropping(image):
    image = cv2.imread(image)
    cv2.imshow("Original", image)
    cropped = image[30:120 , 240:335]
    cv2.imshow("T-Rex Face", cropped)
    cv2.waitKey(0)

def arthimetic():
    print("max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100]))))
    print("min of 0: " + str(cv2.subtract(np.uint8([50]), np.uint8([100]))))
    print("wrap around: " + str(np.uint8([200]) + np.uint8([100])))
    print("wrap around: " + str(np.uint8([50]) - np.uint8([100])))

def arthimetic_on_image(image):
    M = np.ones(image.shape, dtype = "uint8") * 100
    added = cv2.add(image, M)
    cv2.imshow("Added", added)

    M = np.ones(image.shape, dtype = "uint8") * 50
    subtracted = cv2.subtract(image, M)
    cv2.imshow("Subtracted", subtracted)
    cv2.waitKey(0)

def bitwise(image):
    rectangle = np.zeros((300, 300), dtype = "uint8")
    cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
    cv2.imshow("Rectangle", rectangle)

    circle = np.zeros((300, 300), dtype = "uint8")
    cv2.circle(circle, (150, 150), 150, 255, -1)
    cv2.imshow("Circle", circle)

    bitwiseAnd = cv2.bitwise_and(rectangle, circle)
    cv2.imshow("AND", bitwiseAnd)
    cv2.waitKey(0)
    
    bitwiseOr = cv2.bitwise_or(rectangle, circle)
    cv2.imshow("OR", bitwiseOr)
    cv2.waitKey(0)
    
    bitwiseXor = cv2.bitwise_xor(rectangle, circle)
    cv2.imshow("XOR", bitwiseXor)
    cv2.waitKey(0)
    
    bitwiseNot = cv2.bitwise_not(circle)
    cv2.imshow("NOT", bitwiseNot)
    cv2.waitKey(0)

def masking(image):
    image = cv2.imread(image)
    cv2.imshow("Original", image)

    mask = np.zeros(image.shape[:2], dtype = "uint8")
    (cX, cY) = (image.shape[1] / 2, image.shape[0] / 2)
    cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255,-1)
    cv2.imshow("Mask", mask)
    
    masked = cv2.bitwise_and(image, image, mask = mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)

    # circle

    mask = np.zeros(image.shape[:2], dtype = "uint8")
    cv2.circle(mask, (cX, cY), 100, 255, -1)
    masked = cv2.bitwise_and(image, image, mask = mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)

def splitting_merging(image):
    image = cv2.imread(image)
    (B, G, R) = cv2.split(image)

    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    cv2.waitKey(0)

    merged = cv2.merge([B, G, R])
    cv2.imshow("Merged", merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    zeros = np.zeros(image.shape[:2], dtype = "uint8")
    cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
    cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
    cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
    cv2.waitKey(0)

def colorspace(image):
    image = cv2.imread(image)
    cv2.imshow("Original", image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    cv2.imshow("L*a*b*", lab)
    cv2.waitKey(0)

def grayscaleHistogram(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original", image)

    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)

def colorHistogram(image):
    image = cv2.imread(image)
    cv2.imshow("Original", image)
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title("’Flattened’ Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])

    fig = plt.figure()

    ax = fig.add_subplot(131)
    hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,
    [32, 32], [0, 256, 0, 256])
    p = ax.imshow(hist, interpolation = "nearest")
    ax.set_title("2D Color Histogram for G and B")
    plt.colorbar(p)

    ax = fig.add_subplot(132)
    hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,
    [32, 32], [0, 256, 0, 256])
    p = ax.imshow(hist, interpolation = "nearest")
    ax.set_title("2D Color Histogram for G and R")
    plt.colorbar(p)

    ax = fig.add_subplot(133)
    hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,
    [32, 32], [0, 256, 0, 256])
    p = ax.imshow(hist, interpolation = "nearest")
    ax.set_title("2D Color Histogram for B and R")
    plt.colorbar(p)

    print("2D histogram shape: %s, with %d values" % (hist.shape, hist.flatten().shape[0]))
    hist = cv2.calcHist([image], [0, 1, 2],None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    print("3D histogram shape: %s, with %d values" % (hist.shape, hist.flatten().shape[0]))

    plt.show()


def hist_equalization(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(image)
    cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
    cv2.waitKey(0)

def plot_histogram(image, title, mask = None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])

def hist_equali_on_mask(image):
    image = cv2.imread(image)
    cv2.imshow("Original", image)
    plot_histogram(image, "Histogram for Original Image")