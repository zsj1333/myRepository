import math


# 类定义
class Calculate:
    # 定义基本属性
    a = 0
    b = 0
    c = 0

    # 定义构造方法
    def __init__(self, a1, b1, c1):
        self.a = a1
        self.b = b1
        self.c = c1

    def equation(self):
        h = self.b * self.b - 4 * self.a * self.c  # 一元二次方程的解
        if h >= 0:
            x1 = (-self.b + math.sqrt(h)) / 2 * self.a  # sqrt函数求平方根
            x2 = (-self.b - math.sqrt(h)) / 2 * self.a
            print('x1 = %.2f' % x1, 'x2 = %.2f' % x2)
        else:
            print('方程无解')


# 实例化类
x = int(input("请输入a："))
y = int(input("请输入b："))
z = int(input("请输入c："))
p = Calculate(x, y, z)
p.equation()
