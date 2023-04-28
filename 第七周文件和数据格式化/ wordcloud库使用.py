#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/6 20:49
# @File :  wordcloud库使用.py
# import wordcloud
# c=wordcloud.WordCloud()
# c.generate('wordCloud by python')
# c.to_file('pyword.png')
# import wordcloud
# txt = "life is short, you need python"
# w = wordcloud.WordCloud(background_color = "white")
# w.generate(txt)
# w.to_file("pywcloud.png")

import jieba
import wordcloud
txt = "程序设计语言是计算机能够理解和\
识别用户操作意图的一种交互体系，它按照\
特定规则组织计算机指令，使计算机能够自\
动进行各种运算处理。"
w = wordcloud.WordCloud( width=1000,\
font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")