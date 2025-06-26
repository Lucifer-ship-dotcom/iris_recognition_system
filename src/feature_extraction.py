import cv2
import numpy as np

def extract_features(normalized_iris):
    resized = cv2.resize(normalized_iris, (64, 64))
    laplacian = cv2.Laplacian(resized, cv2.CV_64F)
    features = np.sign(laplacian).astype(np.uint8).flatten()
    return features
