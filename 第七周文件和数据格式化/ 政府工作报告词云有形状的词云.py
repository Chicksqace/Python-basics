#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/6 19:57
# @File :  政府工作报告词云 .py
import jieba
import wordcloud
from imageio import imread
mask = imread("bitlogo.png")
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud( font_path = "msyh.ttc", mask = mask,\
width = 1000, height = 700, background_color = "white",\
)
w.generate(txt)
w.to_file("grwordcloud.png")