import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

height = [155.3, 157.5, 156.5, 163.9, 169.3, 170.5, 195.5, 175.1, 173.8, 177.7, 182.6, 180.7, 186.7, 189.9, 189.2]
foot_size = [220, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 300]

# 데이터 전처리
# 극단치 데이터 제거
foot_size = foot_size[0:6] + foot_size[7:]
height = height[0:6] + height[7:]

# numpy 배열로 변환
x = np.array(foot_size)
y = np.array(height)

# 최소제곱법 구현
a = np.sum((y-np.mean(y))*(x-np.mean(x))) # a(기울기)의 분자
a = a/np.sum((x-np.mean(x))**2) # a(기울기)의 분모를 구현하고 분자로 나눔
b = np.mean(y)-a*np.mean(x) # b(절편)

# print(f'a(기울기) : {a}, b(절편) : {b}')


# 회귀선 구하기
line_x = np.arange(min(x), max(x), 1) # x축 데이터의 최솟값부터 최댓값까지 1(cm)간격으로 line_x에 저장
line_y = a*line_x + b # 저장된 line_x를 통해 line_y에 저장


# 회귀선 시각화
plt.plot(line_x, line_y, color = 'r')
plt.scatter(x, y)
# 데이터를 그래프로 시각화
# plt.scatter(foot_size, height) # scatter(x, y)
plt.xlabel('Foot Size') # x축 데이터 명칭
plt.ylabel('Height') # y축 데이터 명칭


plt.show()
