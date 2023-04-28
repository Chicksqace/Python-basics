#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/19 23:38
# @File : 文本进度条.py
# import time
# scale=10
# print("----------执行开始----------")
# for i in range(scale+1):
#     a='*'*i
#     b='.'*(scale-i)
#     c=(i/scale)*100
#     print("{:^3.0f}%[{}->{}]".format(c,a,b))
#     time.sleep(0.1)
# print("----------执行结束----------")

# import time
# for i in range(101):
#     print("\r{:3}%".format(i),end="")
#     time.sleep(0.1)

import time
scale=50
print("执行开始".center(scale//2,"-"))
# // 取整除 - 返回商的整数部分
# 使用字符串处理中的.center方法将，将一个“-”字符填充在执行开始
start=time.perf_counter()
# 调用perf_counter()函数,记录开始时间
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    # dur变量记录每一次，需要打印文本进度条时所消耗的时间  用当前时间减去star最开始的时间
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,"-"))