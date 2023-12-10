import cv2
import numpy as np
import matplotlib.pyplot as plt


"""
Learn to read and edit pixel values, working with image ROI and other basic operations
"""

def modify():
    img = cv2.imread("..\\pic\\messi5.jpg")
    px = img.item(10, 10, 2) # access pixel values
    print(px)
    img.itemset((10, 10, 2), 100)  # modifying pixel value
    px = img.item(10, 10, 2)
    print(px)

def properties():
    img = cv2.imread("..\\pic\\messi5.jpg")
    print(img.shape)
    print(img.size)
    print(img.dtype)

def ROI():
    img = cv2.imread("..\\pic\\messi5.jpg")

    ball = img[280:340, 330:390]  # using numpy indexing, copy a ball to another region in the image
    img[273:333, 100:160] = ball

    cv2.imshow("image", img)
    flag = cv2.waitKey(0)
    if flag == 27:
        cv2.destroyAllWindows()

def split_merge():
    img = cv2.imread("..\\pic\\messi5.jpg")

    b, g, r = cv2.split(img)
    img = cv2.merge((b, g, r))

    cv2.imshow("image", img)
    flag = cv2.waitKey(0)
    if flag == 27:
        cv2.destroyAllWindows()

def border():
    img1 = cv2.imread("..\\pic\\opencv-logo.png")
    assert img1 is not None, "img1 could not be read, check with os.path.exists()"
    BLUE = [0, 0, 255]
    replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
    #
    # plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
    # plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    # plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    # plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    # plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    # plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
    # plt.show()
    cv2.imshow("image", img1)
    cv2.imshow("image1", replicate)
    cv2.imshow("image2", reflect)
    cv2.imshow("image3", reflect101)
    cv2.imshow("image4", wrap)
    cv2.imshow("image5", constant)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





if __name__ == "__main__":
    border()