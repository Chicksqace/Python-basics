#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/28 12:47
# @File : 集合类型及操作.py
# B=set("python123")
# print(B)
# 运算符
# A={'P','Y',123}
# B=set("python123")
# print(A|B)
# print(B-A)
# 集合处理方法
# A=set("python")
# try:
#     while True:
#         print(A.pop())
# except:
#     pass
# 数据去重
A={'P',"s","P",1,2,3,4,5,6,1,2,4}
B=set(A)
# lt=list(B)
print(list(B))