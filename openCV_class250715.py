import numpy as np
import cv2

# # HSV 색상값 확인
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

# 
# # BGR 채널별 영상 분리
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

# # HSV 색상 범위로 색 추적
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

# # 동영상 파일 열기
# cap = cv2.VideoCapture(r'd:\python\play\sample3.mp4')


# # 허프 변환으로 원 검출 (정지 이미지)
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


# # 허프 변환으로 여러 반지름의 원 검출 (정지 이미지)
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

# # 도형 이름 표시 함수
# def setLabel(image, text, pos):
#     (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)
#     M = cv2.moments(pos)

#     if M['m00'] != 0:
#         cx = int(M['m10'] / M['m00'])
#         cy = int(M['m01'] / M['m00'])
#         cv2.putText(image, text, (cx - int(text_width / 2), cy + int(text_height / 2)), 
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


# # 외곽선 검출 및 도형 분류
# img_color = cv2.imread('C:\\2024vacation\\image111\\sample6.png', cv2.IMREAD_COLOR)
# img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
# ret, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
#     epsilon = 0.005 * cv2.arcLength(cnt, True)
#     approx = cv2.approxPolyDP(cnt, epsilon, True)

#     size = len(approx)

#     cv2.drawContours(img_color, [approx], 0, (0, 255, 0), 2)
#     if cv2.isContourConvex(approx):
#         if size == 3:
#             setLabel(img_color, "triangle", cnt)
#         elif size == 4:
#             setLabel(img_color, "rectangle", cnt)
#         elif size == 5:
#             setLabel(img_color, "pentagon", cnt)
#         elif size == 6:
#             setLabel(img_color, "hexagon", cnt)
#         elif size == 8:
#             setLabel(img_color, "octagon", cnt)
#         elif size == 10:
#             setLabel(img_color, "decagon", cnt)
#         else:
#             setLabel(img_color, str(size), cnt)
#     else:
#         setLabel(img_color, str(size), cnt)

# cv2.imshow('result', img_color)
# cv2.waitKey(0)


# # 허프 변환으로 직선 검출
# img2 = cv2.imread('C:\\2024vacation\\image111\\sample6.png')
# gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (5,5), 0)
# edges = cv2.Canny(blur,50,150, None, 3)
# lines = cv2.HoughLinesP(edges,2,np.pi/180,20,minLineLength=10, maxLineGap=5 )
# for line in lines:
#     x1,y1,x2,y2 = line[0]
#     cv2.line(img2,(x1,y1),(x2,y2),(0,0,0),3)
    
# cv2.imshow('edges', edges)
# cv2.imshow('result', img2)

# cv2.waitKey()
# cv2.destroyAllWindows()

# 움직임 감지 (Motion Detection)
# 웹캠에서 영상을 받아와서 움직임이 있는 부분을 감지하고, 해당 영역에 사각형과 중심점을 표시하는 코드입니다.
# cap = cv2.VideoCapture(0)  # 0번 카메라(웹캠)에서 영상 캡처 시작
# fgbg = cv2.createBackgroundSubtractorMOG2(history=2, varThreshold=50, detectShadows=0)  # 배경 제거 객체 생성
# while(True):
#     ret, frame = cap.read()  # 프레임 읽기
#     fgmask = fgbg.apply(frame)  # 배경 제거 마스크 생성 (움직임이 있는 부분이 흰색)
#     nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(fgmask)  # 연결된 영역(객체) 정보 추출
#     for index, centroid in enumerate(centroids):
#         # 첫 번째 인덱스(배경)는 무시
#         if stats[index][0] == 0 and stats[index][1] == 0:
#             continue
#         # 중심점에 NaN이 있으면 무시
#         if np.any(np.isnan(centroid)):
#             continue
#         x, y, width, height, area = stats[index]  # 객체의 위치(x, y), 크기(width, height), 면적(area)
#         centerX, centerY = int(centroid[0]), int(centroid[1])  # 중심점 좌표
        
#         if area > 100:  # 일정 크기 이상의 객체만 표시
#             cv2.circle(frame, (centerX, centerY), 1, (0, 255, 0), 2)  # 중심점에 초록색 원 그리기
#             cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255))  # 객체 영역에 빨간색 사각형 그리기
#     cv2.imshow('mask', 255-fgmask)  # 움직임 마스크(반전) 표시
#     cv2.imshow('frame', frame)  # 원본 프레임에 표시된 결과 출력
#     if cv2.waitKey(1) & 0xFF == 27:  # ESC 키를 누르면 종료
#         break
# cap.release() 
# cv2.destroyAllWindows()

# 원영상의 형상인식
cap = cv2.VideoCapture('C:\\2024vacation\\play\\sample2_1.mp4')

h = 640
w = 800
pts1 = np.float32([[300, 650], [580, 460], [720, 460], [1100, 650]])
pts2 = np.float32([[200, 640], [200, 0], [600, 0], [600, 640]])
M = cv2.getPerspectiveTransform(pts1, pts2)

while(True):
    ret, frame = cap.read()
    img2 = cv2.warpPerspective(frame, M, (w, h))
    
    cv2.imshow('Original', frame)
    cv2.imshow('Calibrated', img2)
    
    if cv2.waitKey(60) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

