#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/22 21:44
# @File : 蒙特卡罗方法求圆面积.py
# 蒙特卡罗方法是一种通过随机取样来估计数学问题的方法。我们可以用蒙特卡罗方法来估计圆周率。
#
# 假设我们有一个边长为 2 的正方形，以及一个内切于该正方形的圆形。圆的半径为 1。
#
# 现在我们从正方形中随机取样若干个点，并计算它们与圆心的距离。如果距离小于等于 1，则该点在圆内，否则在圆外。
#
# 我们可以用这些采样点的比例来估计圆的面积与正方形面积之比。这个比例等于圆周率除以 4。
#
# 因为圆的面积为 πr²，而正方形面积为 4r²，所以它们的比例为 π/4。
#
# 因此，我们可以通过采样点的比例乘以 4 来估计圆周率。
#
# 具体的做法是，随机生成大量的点，计算在圆内的点的数量，然后用这个数量除以总的采样点数，再乘以 4，就可以得到圆周率的近似值。
#
# 需要注意的是，采样点数量越多，估计的圆周率就越精确。
from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
    pi = 4 * (hits/DARTS)
print("圆周率值是: {}".format(pi))
print("运行时间是: {:.5f}s".format(perf_counter()-start))
