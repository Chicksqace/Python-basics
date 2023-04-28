#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/28 16:05
# @File :  列表类型及操作.py
# ls = ["cat", "dog","tiger", 1024]
# ls[1:2]=[1,2,3,4]
# print(ls)
# del ls[::3]
# print(ls)
# ls=ls*2
# print(ls)
# ls = ["cat", "dog","tiger", 1024]
# ls.append(1234)
# print(ls)
# ls.insert(3,"human")
# print(ls)
# ls.reverse()
# print(ls)

# 定义空列表lt 
lt=[]
# 向lt新增5个元素
lt+=[1,2,3,4,5]
# 修改lt中第2个元素
lt[2]=6
# 向lt中第2个位置增加一个元素
lt.insert(2,7)
# 从lt中第1个位置删除一个元素
del lt[1]
# 删除lt中第1-3位置元素
del lt[1:4]
# 判断lt中是否包含数字0
0 in lt
# 向lt新增数字0
lt.append(0)
# 返回数字0所在lt中的索引
lt.index(0)
# lt的长度
#
len(lt)
# lt中最大元素
max(lt)
# 清空lt
lt.clear()