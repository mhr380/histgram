#!/usr/bin/env python
# -*- coding: utf-8 -*-

author__ = 'Hajime MIHARA'

import cv2
import numpy as np
import sys

def hist(src, color):
    # init histgram array
    hist = [0] * 256

    # get height and width of img
    h, w = src.shape[:2]

    # get histgram by increment
    for y in range(h):
        for x in range(w):
            hist[src[y, x]] += 1

    # get maximum level to normarize
    maxLevel = max(hist)

    # color or grayscale
    if color == None:
        # init histgram img
        histImg = 255 * np.ones((256, 256))
    else:
        histImg = 255 * np.ones((256, 256, 3))

    # draw histgram
    for i in range(256):
        # current level
        level = hist[i] 
        height = float(maxLevel - level) / maxLevel * 256

        if color == None:
            # in grayscale img, histgram is drawn by black
            histImg[height : 256, i] = 0
        else:
            # in color img, histgram is drawn by 255
            histImg[height : 256, i, :] = 0         # the background of graph
            histImg[height : 256, i, color] = 255   # drawn color

    # show and save histgram
    cv2.namedWindow("Histgram")
    cv2.imshow("Histgram", histImg)
    cv2.waitKey(0)
    cv2.imwrite("hist"+str(color)+".png", histImg)

    return 

def check(filename, src, flag):
    if src == None:
        print "Unable to load "+str(filename)
        print "Exit"
        sys.exit()
    else:
        if flag == 1:
            print "Successfully loaded "+str(filename)
        return

def main():
    ### usage:
    ### python histgram.py [imageName]
    ###

    argvs = sys.argv
    filename = argvs[1]

    # read and show image
    src = cv2.imread(filename, 1)
    check(filename, src, 1)
    cv2.namedWindow("InputImg")
    cv2.imshow("InputImg", src)

    # get histgram per color
    # color = 0: green
    # color = 1: blue
    # color = 2: red
    for color in range(3):
        hist(src[:,:,color], color)

    # get histgram of whole image(use grayscale img)
    src = cv2.imread(filename, 0)
    check(filename, src, 0)

    hist(src, None)

    print "Fin."

    return

if __name__ == "__main__":
    main()
