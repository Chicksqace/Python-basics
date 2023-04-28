#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/5 16:24
# @File : 数据的文件写入.py
# f=open("f.txt",'w+',encoding='utf-8')
# ls=['中国','日本','韩国']
# f.writelines(ls)
# f.close()
fo = open("output.txt","w+",encoding='utf-8')
ls = ["中国","法国","美国"]
fo.writelines(ls)
print('1')
fo.seek(0)
for line in fo:
    print(line,',')
    print('end')
fo.close()