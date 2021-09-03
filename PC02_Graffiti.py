#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle as t #import the library of commands that you'd like to use

t.colormode(255)

# Create a panel to draw on. 
panel = t.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here=====
def draw_rect(w,h,fill):
    #func to call rectangle drawing
    if fill == True:
        t.begin_fill()
        t.setheading(0)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.end_fill()
    elif fill == False:
        t.setheading(0)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h) 
def draw_oct(r,fill):
    #func to draw and 8-sided polygon
    t.setheading(0)
    if fill == True:
        t.begin_fill()
        for i in range(1,9):
            t.left(45)
            t.forward(r)
        t.end_fill()
    elif fill == False:
        for i in range(1,r):
            t.left(45)
            t.forward(25)

def turtleTeleport(x,y):
    #easily move turtle to different points
    t.up()
    t.goto(x,y)
    t.down()
def draw_triangle(r,fill):
    #draws an equilateral triangle
    if fill == True:
        t.begin_fill()
        t.setheading(0)
        t.forward(r)
        t.left(120)
        t.forward(r)
        t.left(120)
        t.forward(r)
        t.end_fill()
    else:
        t.setheading(0)
        t.forward(r)
        t.left(120)
        t.forward(r)
        t.left(120)
        t.forward(r)
turtleTeleport(100,100)
t.pensize(15)
draw_rect(50,50, False)
turtleTeleport(-200,-150)
t.pensize(3)
t.fillcolor(100,100,100)
draw_oct(25, True)
turtleTeleport(-100,150)
#rgb color
t.color(100,75,250)
t.pensize(0.5)
t.setheading(0)
t.forward(100)
turtleTeleport(75,-150)
t.pensize(5)
t.fillcolor(175,0,175)
draw_triangle(50,True)

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
