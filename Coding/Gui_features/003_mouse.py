import cv2
import numpy as np

"""
Learn to handle mouse events in OpenCV
cv2.setMouseCallback()
"""



# mouse callback function
def demo():
    def draw_circle(event, x, y, flags, userdata):
        if event == cv2.EVENT_RBUTTONDBLCLK:
            cv2.circle(image,(x,y),100,(255,0,0),-1)
    # Create a black image, a window and bind the function to window
    image = np.zeros((512,512,3), np.uint8)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)

    while True:
        cv2.imshow('image', image)
        # print(cv2.waitKey(20))
        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

# def advanced_demo():


def draw_circle(event, x, y, flags, userdata):
    global ix, iy, drawing, mode
    # print(event, cv2.EVENT_LBUTTONDOWN)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 1)
            else:
                cv2.circle(img, (x, y), 5, (255, 0, 0), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        else:
            cv2.circle(img, (x, y), 5, (255, 0, 0), 1)

drawing = False # true if mouse is pressed
mode = True  # if true, drae rectangle, press 'm' to toggle to curve
ix, iy = -1, -1
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
#
# if __name__ == "__main__":
#     advanced_demo()