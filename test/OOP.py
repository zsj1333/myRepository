import math


a = int(input("请输入a："))
b = int(input("请输入b："))
c = int(input("请输入c："))
h = b * b - 4 * a * c  # 一元二次方程的解
if h >= 0:
    x1 = (-b + math.sqrt(h)) / 2 * a  # sqrt函数求平方根
    x2 = (-b - math.sqrt(h)) / 2 * a
    print('x1 = %.2f' % x1, 'x2 = %.2f' % x2)
else:
    print('方程无解')


