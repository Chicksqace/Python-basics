#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/25 12:49
# @File : 刷新倒计时.py
import turtle
import time

def drawGap():
    # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):
    # 绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(d):
    # 根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))

def drawCountdown(countdown):
    # 绘制时间倒计时
    turtle.clear() # 清空画布
    turtle.pencolor("black")
    # 分别获取时分秒的值
    hour = countdown // 3600
    minute = countdown % 3600 // 60
    second = countdown % 60
    # 绘制时分秒的七段数码管
    drawDigit(hour // 10)
    drawDigit(hour % 10)
    turtle.write(':', font=("Arial", 18, "normal"))
    drawDigit(minute // 10)
    drawDigit(minute % 10)
    turtle.write(':', font=("Arial", 18, "normal"))
    drawDigit(second // 10)
    drawDigit(second % 10)

def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    # 绘制当前时间
    # drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    # turtle.hideturtle()
    # 设置倒计时时间
    countdown = 60
    while countdown > 0:
        drawCountdown(countdown)
        time.sleep(1) # 暂停1秒
        countdown -= 1

    turtle.done()


if __name__ == '__main__':
    main()
