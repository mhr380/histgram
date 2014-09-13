#coding: utf-8

import cv2
import numpy as np
import sys

def imgReader(filename):
    src = cv2.imread(filename, 0)
    return src

def hist(src):
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

    # init histgram img
    histImg = 255 * np.ones((256, 256))

    # draw histgram
    for i in range(256):
        level = hist[i] 
        height = float(maxLevel - level) / maxLevel * 256
        histImg[height : 256, i] = 0

    # show and save histgram
    cv2.namedWindow("InputImg")
    cv2.namedWindow("Histgram")
    cv2.imshow("InputImg", src)
    cv2.imshow("Histgram", histImg)
    cv2.waitKey(0)
    cv2.imwrite("hist.png", histImg)

    return 

def main():
    ### usage:
    ### python histgram.py [imageName]
    ###

    argvs = sys.argv
    filename = argvs[1]

    # readImage
    src = imgReader(filename)

    # get histgram
    hist(src)
    
    return

if __name__ == "__main__":
    main()
