#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/27 22:03
# @File : web网站开发flask.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello world'