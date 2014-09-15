#coding: utf-8

import cv2
import numpy as np
import sys

def imgReader(filename, flag):
    src = cv2.imread(filename, flag)
    return src

def hist(src, color):
    # init histgram array
    hist = [0] * 256

    # get height and width of img
    h, w = src.shape[:2]

    # get histgram
    for y in range(h):
        for x in range(w):
            hist[src[y, x]] += 1

    # get maxlevel to normarize
    maxLevel = max(hist)

    if color == None:
        # init histgram img
        histImg = 255 * np.ones((256, 256))
    else:
        histImg = 255 * np.ones((256, 256, 3))

    print color 

    # draw histgram
    for i in range(256):
        level = hist[i] 
        height = float(maxLevel - level) / maxLevel * 256

        if color == None:
            histImg[height : 256, i] = 0
        else:
            histImg[height : 256, i, :] = 0
            histImg[height : 256, i, color] = 255

    # show and save histgram
    cv2.namedWindow("Histgram")
    cv2.imshow("Histgram", histImg)
    cv2.waitKey(0)
    cv2.imwrite("hist"+str(color)+".png", histImg)

    return 

def main():
    ### usage:
    ### python histgram.py [imageName]
    ###

    argvs = sys.argv
    filename = argvs[1]

    # readImage
    src = cv2.imread(filename, 1)
    cv2.namedWindow("InputImg")
    cv2.imshow("InputImg", src)

    # get histgram per color
    for color in range(3):
        hist(src[:,:,color], color)

    # get histgram of whole image
    src = imgReader(filename, 0)
    hist(src, None)

    return

if __name__ == "__main__":
    main()
