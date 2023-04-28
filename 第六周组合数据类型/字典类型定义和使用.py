#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/28 18:18
# @File : 字典类型定义和使用.py
# d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
# print(d)
# print(d['中国'])
# de={}
# print(de)
# d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
# print("中国" in d)
# print(d.keys())
# print(d.values())

# d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
# print(d.get("中国","不在就返回我"))
# print(d.get("俄罗斯","不在就返回我"))
# print(d.popitem())

# 定义空字典d
d={}
# 向d新增2个键值对元素
d[0]=1
d[1]=2
# 修改第2个元素
d[1]=3
# 判断字符"c"是否是d的键
"c" in d
# 计算d的长度
len(d)
# 清空d
d.clear()