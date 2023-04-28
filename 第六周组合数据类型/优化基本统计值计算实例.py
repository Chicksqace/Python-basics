#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/3/28 17:44
# @File : 基本统计值计算实例.py

def getNum():
    """
    获取用户输入的数字，返回一个列表
    """
    nums = []
    while True:
        try:
            iNumStr = input("请输入数字(回车退出): ")
            if iNumStr == "":
                break
            nums.append(float(iNumStr))
        except:
            print("输入错误，请重新输入！")
    return nums

def mean(numbers):
    """
    计算平均值
    """
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)

def dev(numbers, mean):
    """
    计算方差
    """
    sdev = 0.0
    for num in numbers:
        sdev += (num - mean) ** 2
    return (sdev / (len(numbers) - 1)) ** 0.5

def median(numbers):
    """
    计算中位数
    """
    numbers.sort()
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med

if __name__ == '__main__':
    n = getNum()
    m = mean(n)
    d = dev(n, m)
    md = median(n)
    print("平均值:{:.2f}, 方差:{:.2f}, 中位数:{:.2f}.".format(m, d, md))