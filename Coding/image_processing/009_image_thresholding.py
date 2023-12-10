import cv2
import numpy as np
import matplotlib.pyplot as plt
"""
learn thresholding
"""
def simple_thresholding():
    # if the pixel value is smaller than the threshold, it is set to 0, otherwise it it set to maximum value
    img = cv2.imread("..\\pic\\gradient.png", cv2.COLOR_BGR2GRAY)
    assert img is not None, "img could not be read"

    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # (pixel > thresh) = maxval, else 0
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # (pixel > thresh) = 0, else maxval
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)  # (pixel > thresh) = threshval, else original
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # (pixel > thresh) = original, else 0
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # (pixel > thresh) = 0, else original


    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def adaptive_thresholding():
    # the threshold for a pixel based on a small region around it
    img = cv2.imread("..\\pic\\sudoku.png", cv2.IMREAD_GRAYSCALE)
    assert img is not None, "img could not be read"

    img = cv2.medianBlur(img, 5)

    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # the threshold value is the mean of the neighbourhood area minus the constant c
    thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 2)

    # threshold value is a gaussian-weighted sum of the neighbourhood area minus the constant c
    thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)  # the

    titles = ['Original Image', 'Global Thresholding (v = 127)',
              'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, thresh1, thresh2, thresh3]

    cv2.imshow('image', thresh1)

    for i in range(len(images)):
        plt.subplot(2, 2, i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def otsus_binarization():
    ...

if __name__ == "__main__":
    adaptive_thresholding()