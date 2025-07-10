import numpy as np
import cv2

img = cv2.imread('C:\\2024vacation\\image111\\sample2-1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv2.drawContours(img, [cnt], 0, (255, 0, 0), 3)

    area = cv2.contourArea(cnt)
    print(area)

cv2.imshow('result', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()