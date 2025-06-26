import cv2
import numpy as np

def detect_iris_boundaries(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=100, param2=30, minRadius=20, maxRadius=80)
    pupil = limbus = None
    if circles is not None:
        circles = np.uint16(np.around(circles[0, :]))
        circles = sorted(circles, key=lambda x: x[2])
        pupil = circles[0]  # smaller
        limbus = circles[-1]  # larger
    return pupil, limbus
