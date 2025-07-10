# text = 'Today\'s coffee:\n"커피라떼"\n"아메리카노"'
# print(text)

# poem1 = '\n죽는 날까지 하늘을 우러러\n한점 부끄럼이 없기를,\n잎새에 이는 바람에도\n' \
# '나는 괴로워했다.\n별을 노래하는 마음으로\n모든 죽어가는 것을 사랑해야지\n' \
# '그리고 나한테 주어진 길을\n걸어가야겠다.\n오늘 밤에도 별이 바람에 스치운다.'

# poem = """\n죽는 날까지 하늘을 우러러
# 한점 부끄럼이 없기를,
# 잎새에 이는 바람에도
# 나는 괴로워했다.
# 별을 노래하는 마음으로
# 모든 죽어가는 것을 사랑해야지
# 그리고 나한테 주어진 길을
# 걸어가야겠다.
# 오늘 밤에도 별이 바람에 스치운다."""

# print(poem1)
# print(poem)

# book = '안나 카레니나, Leo Tolsoy'
# book.count('나') # 나가 몇 번 나오는지 세기
# print(book.count('나'))
# book.find('카레') # 카레가 처음 등장하는 위치 찾기
# print(book.find('카레'))
# book.find('카레라이스') # 찾는 문자열이 없으면 -1 반환
# print(book.find('카레라이스')) 
# book.rfind('나') # 나가 마지막으로 등장하는 위치 찾기
# print(book.rfind('나'))

# print('%d' %(3.14)) # 정수로 변환하여 출력
# print('%f' %(3.14)) # 실수로 변환하여 출력
# print('%.2f' %(3.14)) # 소수점 둘째 자리까지 출력

# print(1+2 == 3)
# 1+2 != 4
# 1<2
# 1>2
# 1<2<3<4

# import math as m
# print(m.pi)

# a = int(input('숫자를 입력하세요: '))
# if a > 10:
#     print('10 초과')
# elif a < 10:
#     print('10 미만')
# else:
#     print('10')

# marks = [90, 45, 67, 80, 25]
# number = 0

# for i in marks:
#     number += 1
#     if i >= 60:
#         continue
#     print('%d번째 학생은 합격입니다.' % number)

# coffee = 5

# while True:
#     money = int(input('돈을 넣어주세요: (커피한잔 300원)'))
#     if money == 300:
#         print('커피를 드립니다.')
#         coffee -= 1
#     elif money > 300:
#         print('커피를 드리고, 거스름돈 %d원을 드립니다.' % (money - 300))
#         coffee -= 1
#     else:
#         print('돈을 다시 돌려주고 커피를 드리지 않습니다.')

#     print('남은 커피의 양은 %d개 입니다.' % coffee)

#     if coffee == 0:
#         print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
#         break

# import numpy as np

# np.sin(np.array((0., 30., 45., 60., 90.)) *np.pi/180.)
# print(np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))

import numpy as np
import cv2

# image = cv2.imread('C:\\2024vacation\\image111\\sample1.jpg', cv2.IMREAD_UNCHANGED)

# cv2.namedWindow("AutoMoon", cv2.WINDOW_NORMAL)
# cv2.imshow("AutoMoon", image)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()  

cap = cv2.VideoCapture(0)

while True:
    _,frame=cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('real', frame)
    cv2.imshow('video', gray)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
