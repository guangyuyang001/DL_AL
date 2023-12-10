import cv2
import numpy as np
"""
learn how to convert images from one color-space to another
"""

def changeing_color_space():
    flags = [i for i in dir(cv2) if i.startswith("COLOR_")]
    print(len(flags))
    image = cv2.imread("..\\pic\\lena.jpg")

    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cv2.imshow("image", image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def object_tracking():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot find camera.")
        exit()
    while True:
        # Take each frame
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exit ...")
            break

        frame = cv2.GaussianBlur(frame, (3, 3), 0)
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # define range of blue color in HSV
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        # # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)  # mask大于0的位置显示

        cv2.imshow("Video!", res)
        cv2.imshow("mask", mask)
        if cv2.waitKey(10) == ord("Q"):
            break

        # print(hsv.shape)
        # print(mask.shape)
        # break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    object_tracking()
