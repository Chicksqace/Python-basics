#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/19 19:38
# @File : time库的使用.py
import time as t
# print(t.time())
# print(t.ctime())
# print(t.gmtime())

# f=t.gmtime()
# print(t.strftime("%Y-%m-%d %H:%M:%S",f))
#
# timeStr="2023-03-19 12:04:53"
# print(t.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))
start=t.perf_counter()
print(start)
t.sleep(3)
end=t.perf_counter()
print(end)
print("最终的时间",end-start)

