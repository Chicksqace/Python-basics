#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/23 22:58
# @File : 函数的定义与使用.py
# def fact(n):
#     s=1
#     for i in range(1,n+1):
#         s*=i
#     return s
# print(fact(3))

# def fact(n,m=2):
#     s=1
#     for i in range(1,n+1):
#         s*=i
#     return s*m
# print(fact(3))

# def fact(n,*m):
#     s=1
#     for i in range(1,n+1):
#         s*=i
#     for item in m:
#         s*=item
#     return s,m
# print(fact(3,2,3,2))

f=lambda x,y:x+y
print(f(10,15))
f1=lambda : "lambda函数"
print(f1())