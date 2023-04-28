#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/20 17:40
# @File : 程序分支.py
# guess=eval(input())
# print("猜{}了".format("对" if guess==99 else "错"))

# score=eval(input())
# if score>=90:
#     grade="A"
# elif score>=80:
#     grade="B"
# elif score>=70:
#     grade="c"
# else:
#     grade="D"
# print("成绩等级属于{}".format(grade))

# 异常
try:
    num=eval(input("请输入一个整数"))
    print(num**2)
except NameError:
    print('输入整数')
