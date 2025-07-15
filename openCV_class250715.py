import numpy as np
import cv2

# def hsv():
#     blue = np.uint8([[[255, 0, 0]]])   
#     green = np.uint8([[[0, 255, 0]]]) 
#     red = np.uint8([[[0, 0, 255]]])

#     hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
#     hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
#     hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

#     print('HSV for BLUE', hsv_blue)
#     print('HSV for RED', hsv_red)
#     print('HSV for GREEN', hsv_green)
# hsv()

# def tracking():
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         blue_result,green_result,red_result = cv2.split(frame)
#         zeros = np.zeros ((frame.shape[0], frame.shape[1]), dtype='uint8')
#         blue_result = cv2.merge([blue_result, zeros,zeros])
#         green_result = cv2.merge([zeros, green_result, zeros])
#         red_result = cv2.merge([zeros, zeros, red_result])
#         cv2.imshow("original", frame)
#         cv2.imshow("blue", blue_result)
#         cv2.imshow("red", red_result)
#         cv2.imshow("green", green_result)
#         key = cv2.waitKey(1) & 0xFF
#         if key == 27:
#             break
#     cv2.destroyAllWindows()
# tracking()

range = 18

def tracking2():
    cap = cv2.VideoCapture(0)
    lower_blue = np.array([120-range, 20, 20])
    upper_blue = np.array([120+range, 255, 255])
    lower_green = np.array([60-range, 20, 20])
    upper_green = np.array([60+range, 255, 255])
    lower_red = np.array([0-range, 20, 20])
    upper_red = np.array([0+range, 255, 255])

    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blue_range = cv2.inRange(hsv, lower_blue, upper_blue)        
        green_range = cv2.inRange(hsv, lower_green, upper_green)
        red_range = cv2.inRange(hsv, lower_red, upper_red)
        blue_result = cv2.bitwise_and(frame, frame, mask=blue_range)
        red_result = cv2.bitwise_and(frame, frame, mask=red_range)
        green_result = cv2.bitwise_and(frame, frame, mask=green_range)

        cv2.imshow("original", frame)
        cv2.imshow("blue", blue_result)
        cv2.imshow("red", red_result)
        cv2.imshow("green", green_result)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
    cv2.destroyAllWindows()
tracking2()

cap = cv2.VideoCapture(r'd:\python\play\sample3.mp4')