#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/27 22:09
# @File : 微信.py
import werobot
robot = werobot.WeRoBot(token='tokenhere')
@robot.handler
def hello(message):
    return 'Hello World!'