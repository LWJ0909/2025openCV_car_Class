import numpy as np
import cv2

def hsv():
    blue = np.uint8([[[255, 0, 0]]])   
    green = np.uint8([[[0, 255, 0]]]) 
    red = np.uint8([[[0, 0, 255]]])

    hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

    print('HSV for BLUE', hsv_blue)
    print('HSV for RED', hsv_red)
    print('HSV for GREEN', hsv_green)
hsv()

def tracking():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        blue_result,green_result,red_result = cv2.split(frame)
        zeros = np.zeros ((frame.shape[0], frame.shape[1]), dtype='uint8')
        blue_result = cv2.merge([blue_result, zeros,zeros])
        green_result = cv2.merge([zeros, green_result, zeros])
        red_result = cv2.merge([zeros, zeros, red_result])
        cv2.imshow("original", frame)
        cv2.imshow("blue", blue_result)
        cv2.imshow("red", red_result)
        cv2.imshow("green", green_result)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
    cv2.destroyAllWindows()
tracking()