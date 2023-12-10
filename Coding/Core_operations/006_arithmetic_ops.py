import cv2
import numpy as np

"""
Learn several arithmetic operations on image
cv2.add(), cv2.addWeighted()
"""

def add():

    image1 = cv2.imread("..\\pic\\ml.png")
    image2 = cv2.imread("..\\pic\\opencv-logo.png")
    assert image1 is not None, "image1 could not be read"
    assert image2 is not None, "image2 could not be read"
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0])) # make sure both pictures are the same size

    dst1 = cv2.add(image1, image2)
    dst2 = cv2.addWeighted(image1, 1, image2, 0, 0)
    # dst = a1*image1+a2*image2+b

    cv2.imshow("image1", dst1)
    cv2.imshow("image2", dst2)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

def bitwish_ops():
    # load two images
    image1 = cv2.imread("..\\pic\\messi5.jpg")
    image2 = cv2.imread("..\\pic\\opencv-logo-white.png") # logo picture
    cv2.namedWindow("image1")  # create a image window


    # put logo on top-left corner, so i create a ROI
    row, col, channel = image2.shape  # get the shape of the logo
    roi = image1[0:row, 0:col]  # get the pixel values of the added image

    # create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)  # image2 is converted to grayscale
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) # exceed the threshold value are assigned a value of 255, logol is white
    mask_inv = cv2.bitwise_not(mask)  # 255 is converted to 0, logo is black

    # take only region of logo from logo image
    img2_fg = cv2.bitwise_and(image2, image2, mask=mask)
    # colourful logo and background turns black(=0)

    # now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    # the pixel of mask=0 is set 0 else retain, black logo(=0) position is setting black

    # put logo in ROI and modify the main image
    dst = cv2.add(img1_bg, img2_fg)
    image1[0:row, 0:col] = dst


    cv2.imshow("image1", img1_bg)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    bitwish_ops()