#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/20 18:39
# @File : 程序的循环结构.py
# for i in range(1,6,2):
#     print(i)
# for i in "python123":
#     print(i,end=",")

# for item in ["ssfs",23,"cs"]:
#     print(item)

# fl=open("./作业一.txt",encoding="utf-8")
# for i in fl:
#     print(i)

# a=3;
# while a>0:
#     a=a-1
#     print(a)

# s="python"
# while s!="":
#     for c in s:
#         if c=="t":
#             break
#         print(c,end="")
#     print("@",s)
#     s=s[:-1]
#     print("----",s)
# print(s)

for c in "python":
    if c=="t":
        continue
    print(c,end="")
else:
    print("退出")

for c in "python":
    if c=="t":
        break
    print(c,end="")
else:
    print("退出")