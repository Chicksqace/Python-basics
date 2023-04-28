#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/25 13:14
# @File : 递归的实现.py
# 字符串反转
# def rvs(s):
#     if s=="":
#         return s
#     else:
#         return rvs(s[1:])+s[0]
# print(rvs('abscs'))
# 斐波那契数列
# def f(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# print(f(6))
# 汉诺塔问题
# 第一个参数是圆盘的数量 第二个参数是源柱子 第三个参数是目的柱子 第四个是中间过渡柱子
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1 :
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1, mid, dst, src)
hanoi(3, "A", "C", "B")
print(count)
