import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
canny edge detection
step:
1. noise reduction(5*5 Gaussian filter)
2. finding intensity gradient 
3. non-maximum suppression
4. hysteresis threshold
"""

def canny():
    img = cv2.imread("..\\pic\\messi5.jpg", cv2.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be found"

    edges1 = cv2.Canny(img, 220, 250)
    edges2 = cv2.Canny(img, 100, 200)

    cv2.imshow("orginal image", img)
    cv2.imshow("edge1 image", edges1)
    cv2.imshow("edge2 image", edges2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    canny()