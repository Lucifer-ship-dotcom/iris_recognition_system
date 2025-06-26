import cv2

def load_image(path):
    return cv2.imread(path)

def display_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
