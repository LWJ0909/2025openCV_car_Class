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

# range = 18

# def tracking2():
#     cap = cv2.VideoCapture(0)
#     lower_blue = np.array([120-range, 20, 20])
#     upper_blue = np.array([120+range, 255, 255])
#     lower_green = np.array([60-range, 20, 20])
#     upper_green = np.array([60+range, 255, 255])
#     lower_red = np.array([0-range, 20, 20])
#     upper_red = np.array([0+range, 255, 255])

#     while True:
#         ret, frame = cap.read()
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         blue_range = cv2.inRange(hsv, lower_blue, upper_blue)        
#         green_range = cv2.inRange(hsv, lower_green, upper_green)
#         red_range = cv2.inRange(hsv, lower_red, upper_red)
#         blue_result = cv2.bitwise_and(frame, frame, mask=blue_range)
#         red_result = cv2.bitwise_and(frame, frame, mask=red_range)
#         green_result = cv2.bitwise_and(frame, frame, mask=green_range)

#         cv2.imshow("original", frame)
#         cv2.imshow("blue", blue_result)
#         cv2.imshow("red", red_result)
#         cv2.imshow("green", green_result)

#         key = cv2.waitKey(1) & 0xFF
#         if key == 27:
#             break
#     cv2.destroyAllWindows()
# tracking2()

# cap = cv2.VideoCapture(r'd:\python\play\sample3.mp4')


# img = cv2.imread('C:\\2024vacation\\image111\\sample3.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=35, minRadius=0, maxRadius=0)
# circles = np.uint16(np.around(circles))

# for c in circles[0, :]:
#     center = (c[0], c[1])
#     radius = c[2]

#     cv2.circle(img, center, radius, (0, 255, 0), 2)
#     cv2.circle(img, center, radius, (0, 0, 255), 3)

# cv2.imshow('result', img)

# if cv2.waitKey(0) & 0xFF == 27:
#     cv2.destroyAllWindows()


# img2 = cv2.imread('C:\\2024vacation\\image111\\sample3-1.jpg')
# gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray2, (5, 5), 0)

# while (True):
#     circles1 = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=35, minRadius=0, maxRadius=100)
#     circles1 = np.uint16(np.around(circles1))

#     for c in circles1[0, :]:
#         center = (c[0], c[1])
#         radius = c[2]

#         cv2.circle(img2, center, radius, (0, 255, 0), 2)
#         cv2.circle(img2, center, radius, (0, 0, 255), 3)

#     circles2 = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=35, minRadius=100, maxRadius=200)
#     circles2 = np.uint16(np.around(circles2))

#     for c in circles2[0, :]:
#         center = (c[0], c[1])
#         radius = c[2]

#         cv2.circle(img2, center, radius, (0, 255, 0), 2)
#         cv2.circle(img2, center, radius, (0, 255, 0), 3)

#     circles3 = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=35, minRadius=200, maxRadius=300)
#     circles3 = np.uint16(np.around(circles3))

#     for c in circles3[0, :]:
#         center = (c[0], c[1])
#         radius = c[2]

#         cv2.circle(img2, center, radius, (0, 255, 0), 2)
#         cv2.circle(img2, center, radius, (255, 0, 0), 3)

#     cv2.imshow('result', img2)

#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()

def setLabel(image, text, pos):
    (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)
    M = cv2.moments(pos)

    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(image, text, (cx - int(text_width / 2), cy + int(text_height / 2)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


img_color = cv2.imread('C:\\2024vacation\\image111\\sample6.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.005 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    size = len(approx)

    cv2.drawContours(img_color, [approx], 0, (0, 255, 0), 2)
    if cv2.isContourConvex(approx):
        if size == 3:
            setLabel(img_color, "triangle", cnt)
        elif size == 4:
            setLabel(img_color, "rectangle", cnt)
        elif size == 5:
            setLabel(img_color, "pentagon", cnt)
        elif size == 6:
            setLabel(img_color, "hexagon", cnt)
        elif size == 8:
            setLabel(img_color, "octagon", cnt)
        elif size == 10:
            setLabel(img_color, "decagon", cnt)
        else:
            setLabel(img_color, str(size), cnt)
    else:
        setLabel(img_color, str(size), cnt)

cv2.imshow('result', img_color)
cv2.waitKey(0)