# -*- coding:utf-8 -*-
#2017/12/25
#version 1.0
'''
    Happy Christmas to you!
    These code create a Chritmas Tree
'''

import turtle

screen = turtle.Screen()
screen.setup(800,600)
circle = turtle
circle.speed('fastest')
circle.shape('circle')
circle.color('red')
circle.up()
circle.goto(0,280)
circle.stamp()

square = turtle
square.speed('fastest')
square.shape('square')
square.color('green')
square.up()
square.goto(0,250)
square.stamp()
k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
    if i % 4 == 0:
        x = 30*(j+1)
        circle.color('red')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
        k += 2
        circle.color('green')
    if i % 4 == 3:
        x = 30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
        circle.color('green')

square.color('brown')

for i in range(17,20):
    y = 30*i
    for j in range(3):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()

turtle.exitonclick()


