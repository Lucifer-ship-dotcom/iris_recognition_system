import cv2
import numpy as np

def normalize_iris(image, pupil, limbus, output_size=(64, 512)):
    rows, cols = output_size
    theta = np.linspace(0, 2 * np.pi, cols)
    r = np.linspace(0, 1, rows)
    r, theta = np.meshgrid(r, theta)

    xp = pupil[0] + pupil[2] * r * np.cos(theta)
    yp = pupil[1] + pupil[2] * r * np.sin(theta)

    xl = limbus[0] + limbus[2] * r * np.cos(theta)
    yl = limbus[1] + limbus[2] * r * np.sin(theta)

    x = (1 - r) * xp + r * xl
    y = (1 - r) * yp + r * yl

    x = x.astype(np.float32)
    y = y.astype(np.float32)

    normalized = cv2.remap(image, x, y, cv2.INTER_LINEAR)
    return normalized
