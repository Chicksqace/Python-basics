#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/25 16:35
# @File : 康托尔集.py
import turtle

def cantor(length, depth):
    if depth == 0:
        turtle.fd(length)
    else:
        turtle.down()
        cantor(length/3, depth-1)
        turtle.up()
        turtle.fd(length/3)
        turtle.down()
        cantor(length/3, depth-1)
        turtle.up()
        turtle.fd(length/3)
        turtle.down()
        cantor(length/3, depth-1)
        turtle.up()

def main():
    turtle.setup(800, 400)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-350, 0)
    turtle.pendown()
    turtle.pensize(2)
    cantor(700, 5)
    turtle.hideturtle()
    turtle.done()

main()