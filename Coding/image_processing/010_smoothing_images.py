import cv2
import numpy as np

"""
bur image with various low pass filters
apply custom-made filters to images(2D convolution)
images can be filered with various low-pass filters(LPF), high-pass(HPF)
LPF helps in removing noise, blurring image
HPF helps in finding edges in images
"""

def twoD_filter():
    # replace the central pixel with the average value
    img = cv2.imread("..\\pic\\opencv-logo-white.png")
    assert img is not None, "img could not be read"

    kernel = np.ones((5, 5), np.uint8) / 25
    dst = cv2.filter2D(img, -1, kernel)

    cv2.imshow("original", img)
    cv2.imshow("averaging", dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def image_blur():
    img = cv2.imread("..\\pic\\opencv-logo-white.png")
    assert img is not None, "img could not be read"

    blur = cv2.blur(img, (5, 5))
    gblur = cv2.GaussianBlur(img, (5, 5), 0)
    mblur = cv2.medianBlur(img, 5)

    cv2.imshow("original", img)
    cv2.imshow("Avg", blur)
    cv2.imshow("Gauss", gblur)
    cv2.imshow("Median", mblur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_blur()