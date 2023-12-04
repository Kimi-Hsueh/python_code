'''
Homework(circle_s.py)
使用者輸入圓柱體的半徑及高，程式會計算圓柱體的體積
圓柱體體積的公式為「圓週率乘以半徑平方再乘以高」。
'''
a=int(input('請給我圓柱體的半徑'))
b=int(input('請給我圓柱體的高'))
pi=3.14
y=pi*a**2*b
print('圓柱體的半徑',a)
print('圓柱體的高',b)
print('圓柱體的體積',y)

'''
高中數學
Homework(degree.py)
讓使用者輸入直角三角形的對邊
讓使用者輸入直角三角形的斜邊
計算角度
公式:
sin(x) = 對邊 / 斜邊
x是radian(弧度)
'''
a=int(input('請輸入直角三角形的對邊'))
b=int(input('請輸入直角三角形的斜邊'))
import math
c=a/b

rou
print('三角形的角度為',deg)