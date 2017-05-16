import time

from PIL import ImageGrab
import numpy as np
from numpy import genfromtxt
import cv2


def edge_detect(image):
    lower_black = genfromtxt('lower_black.csv', delimiter=',', dtype=np.uint8)
    upper_black = genfromtxt('upper_black.csv', delimiter=',', dtype=np.uint8)
    mask = cv2.inRange(image, lower_black, upper_black)
    return mask


def roi(image, verticies):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [verticies], 255)
    return cv2.bitwise_and(image, mask)


def draw_lines(image, lines):
    if lines is None:
        return
    try:
        for line in lines:
            coords = line[0]
            cv2.line(image, (coords[0], coords[1]), (coords[2], coords[3]),
                     [255, 255, 255], 3)
    except AttributeError:
        pass


def green_mask(image):
    min_green = np.array([10, 0, 10])
    max_green = np.array([10, 180, 10])
    return cv2.inRange(image, min_green, max_green)


def orange_mask(image):
    min_orange = np.array([100, 0, 80])
    max_orange = np.array([255, 10, 255])
    return cv2.inRange(image, min_orange, max_orange)


def red_mask(image):
    min_red = np.array([100, 0, 80])
    max_red = np.array([255, 10, 255])
    return cv2.inRange(image, min_red, max_red)


def grab_screen():
    verticies = np.array([[10, 500], [10, 300], [300, 200],
                          [500, 200], [800, 300], [800, 500]])
    while True:
        image = np.array(ImageGrab.grab(bbox=(5, 30, 800, 600)))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.GaussianBlur(image, (7, 7), 0)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        green = green_mask(image)
        cv2.imshow('green', image)
        #orange = orange_mask(image)
        #red = red_mask(image)

        #cv2.imshow('blurred', image)
        #frame = edge_detect(image)
        #frame = roi(frame, verticies)
        #lines = cv2.HoughLinesP(frame, 1, np.pi/180, 180, np.array([]), 100, 5)
        #draw_lines(frame, lines)
        #cv2.imshow('edged', image)
        cv2.waitKey(1)
