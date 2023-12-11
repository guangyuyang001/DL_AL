import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
find image gradients, edges etc
"""

def laplacian():
    img = cv2.imread("..\\pic\\sudoku.png")
    assert img is not None, "file could not be found"

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

    images = [img, laplacian, sobelx, sobely]
    title = ['img', 'laplacian', 'sobelx', 'sobely']
    for i in range(len(images)):
        plt.subplot(2, 2, i+1)
        plt.imshow(images[i], 'gray')
        plt.xticks([])
        plt.yticks([])
        plt.title(title[i])
    plt.show()

def sobel_8u():
    img = np.zeros((250, 250, 3), np.uint8)
    img[3:80, 2:80, :] = 255
    # img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    abs_sobel64f = np.absolute(sobelx64f)
    sobelx8u = np.uint8(abs_sobel64f)
    # print(img, sobelx64f)
    images = [img, sobelx64f, sobelx8u]
    title = ['img', 'sobelx64f', 'sobelx8u']
    # for i in range(len(images)):
    #     plt.subplot(1, 3, i+1)
    #     plt.imshow(images[i], cmap='gray')
    #     plt.xticks([])
    #     plt.yticks([])
    #     plt.title(title[i])
    #     cv2.imshow(title[i], images[i])
    # plt.show()

    cv2.imshow(title[0], images[0])
    cv2.imshow(title[1], images[1])
    cv2.imshow(title[2], images[2])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    sobel_8u()