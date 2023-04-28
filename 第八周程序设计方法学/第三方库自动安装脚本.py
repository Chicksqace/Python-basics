#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/15 16:34
# @File : 第三方库自动安装脚本.py
#BatchInstall.py
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
"jieba","beautifulsoup4","wheel","networkx","sympy",\
"pyinstaller","django","flask","werobot","pyqt5",\
"pandas","pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful")
except:
    print("Failed Somehow")
