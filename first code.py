#Basic

print (5*5)
print("Hello")
print("Hello2")


'''
This is a multiline
comment.

(Make sure to indent the leading quotes appropriately to avoid an IndentationError.)
-------------------- Turtle -------------------
''' 



import turtle
import math
import random

t = turtle.Turtle()
t.color('blue')
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)


#-------------------- Variables -------------------

bob  = "aaaaaa"
print (bob)


#-------------------- Functions -------------------
t.forward(100)

def square():
    import turtle
    import math
    import random

    t = turtle.Turtle()
    t.color('blue')
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

square()


#-------------------- loops -------------------

for i in range(4):
    print(i)
    t.left(60)
    t.forward(100)
    square()
  
  



