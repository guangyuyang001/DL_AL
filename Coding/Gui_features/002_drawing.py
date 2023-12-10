import cv2
import sys
import numpy as np

"""
draw different geometric shapes 
cv2.line(), cv2.circle(), cv2.rectangle(),cv2.ellipse(), cv2.putText()
"""
# start-point, end-point, draw_color, draw_pixel

# drawing line
def draw_line(image):
    # draw a diagonal blue line with thickness of 5 px
    cv2.line(image[0], (0, 0), (511, 511), (0, 0, 255), 10)

# drawing rectangle
def draw_rectangle(image):
    # draw a rectangle at top-right corner of image
    cv2.rectangle(image[0], (0, 120), (500, 510), (0, 0, 255), 3)

# drawing circle
def draw_circle(image):
    cv2.circle(image[0], (200, 100), 200, (255, 0, 0), 4)


# drawing ellipse
def draw_ellipse(image):
    cv2.ellipse(image[0], (200, 100), (50, 100), 180, 0, 180, (0, 255, 0), 2)

# drawing polygon
def draw_polygon(image):
    # position
    pts = np.array([[10, 5], [20, 30], [70, 120], [50, 10]], np.int32)
    print(pts.shape)
    pts = pts.reshape((-1, 1, 2))
    print(pts.shape)
    cv2.polylines(image[0], [pts], True, (0, 255, 0))

def draw():
    # create a black image
    image = np.zeros((512, 512, 3), np.uint8)

    # draw a diagonal blue line with thickness of 5 px
    draw_polygon([image])

    cv2.imshow('image', image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    draw()