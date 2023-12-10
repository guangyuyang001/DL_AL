import numpy as np
import cv2

"""
learn to apply different geometric transfromations to images, like translation, rotation, affine transformation etc.
"""


def scaling():
    image = cv2.imread("..\\pic\\messi5.jpg")
    height, width = image.shape[:2]
    res = cv2.resize(image, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("image", image)
    cv2.imshow("res", res)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


def translation():
    # translation is the shifting of an object's location
    image = cv2.imread("..\\pic\\messi5.jpg")
    height, width = image.shape[:2]
    M = np.float32([[1, 0, 100], [0, 1, 50]])

    dst = cv2.warpAffine(image, M, (width, height))  #
    cv2.imshow("image", image)
    cv2.imshow("res", dst)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


def rotation():
    image = cv2.imread("..\\pic\\messi5.jpg")
    height, width = image.shape[:2]
    M = cv2.getRotationMatrix2D(((width-1)/2.0, (height-1)/2.0), 90, 1)

    dst = cv2.warpAffine(image, M, (width, height))  #
    cv2.imshow("image", image)
    cv2.imshow("res", dst)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

def affine_transformation():
    image = cv2.imread("..\\pic\\messi5.jpg")
    assert image is not None, "iamge could not be read"
    height, width = image.shape[:2]
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)

    dst = cv2.warpAffine(image, M, (width, height))

    cv2.imshow("image", image)
    cv2.imshow("res", dst)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

def perspective_transformation():
    image = cv2.imread("..\\pic\\sudoku.png")
    assert image is not None, "image could not be read"

    height, width = image.shape[:2]
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(image, M, (300, 300))  #
    cv2.imshow("image", image)
    cv2.imshow("res", dst)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    perspective_transformation()
