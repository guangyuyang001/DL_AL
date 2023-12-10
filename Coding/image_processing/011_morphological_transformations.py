import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
learn different morphological operations like erosion, dilation, opening, closing etc.
"""


def mor_ops():
    img = cv2.imread("..\\pic\\j.png")
    assert img is not None, "img could not be found"

    kernel = np.ones((5, 5), np.uint8)

    # a pixel in the original image(either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise made to zero
    erosion = cv2.erode(img, kernel)

    # a pixel in the original image(either 1 or 0) will be considered 1 if at least one pixels under the kernel is 1, otherwise made to zero
    dilation = cv2.dilate(img, kernel)

    # erosion followd by dilation
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    # dilation followd by erosion
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # the difference between dilation and erosion of an image, dilation(image)-erosion(image)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    # gradient = dilation-erosion

    # the difference between input image and opening of the image
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    # tophat = img - opening

    # the difference between the closing of the input image and input image
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    # blackhat = closing-img

    all_images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]
    titles = ['original', 'erosion', 'dilation', 'opening', 'closing', 'gradient', 'tophat', 'blackhat']
    for i in range(len(all_images)):
        plt.subplot(4, 2, i + 1)
        plt.imshow(all_images[i], "gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


def structuring_element():
    # rectangular kernel
    cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # ellipse kernel
    cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    # cross-shaped kernel
    cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))


if __name__ == "__main__":
    mor_ops()
