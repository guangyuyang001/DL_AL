import cv2
import sys


"""
image
"""
# read an image from image

def image():
    image = cv2.imread(cv2.samples.findFile("..\\pic\\starry_night.jpg"))

    if image is None:
        sys.exit("Could not read the image.")
    cv2.imshow("Lenna", image)
    # cv2.waitKey(1000)  # delay 1ms

    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

    # while True:
    #     char_flag = chr(cv2.waitKey(0)).lower()
    #     print(char_flag)
    #     if char_flag == 'q':
    #         cv2.destroyAllWindows()
    #         # cv2.imwrite("Lenna_image.png", image)
    #         print("Exit!")
    #         break

"""
read video
"""
def video():
    cap = cv2.VideoCapture(0) # filename or index
    if not cap.isOpened():
        print("Cannot open camera.")
        exit()
    # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH) , cv2.CAP_PROP_FRAME_WIDTH // 10)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # se
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        # capture frame-by-frame
        retval, frame = cap.read()  # return val
        # if frame is read correctly ret is True
        if not retval:
            print("Can't receive frame (stream end?). Exit ...")
            break

        # our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # display the resulting on the frame come here
        cv2.imshow("Frame", gray)

        if cv2.waitKey(50) == ord('q'): # delay 500ms
            break

    # when everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def write_video():
    # open capture
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object

    fourcc = cv2.VideoWriter.fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    # determine if a camera is on
    if not cap.isOpened():
        print("Can't open camera.")
        exit()
    while True:
        ret, frame = cap.read() # capture frame by frame

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # frame = cv2.flip(frame, 1)
        # write the flipped frame
        cv2.imshow('frame', frame)
        out.write(frame)
        if cv2.waitKey(100) == ord("q"):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image()