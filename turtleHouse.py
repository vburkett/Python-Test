import turtle
import time

def draw_side(size,angle):
    my_turtle.forward(size)
    my_turtle.right(angle)

def draw_regular_polygon(size, sides):
    angle = 360/sides
    i=1
    while i<=sides:
        draw_side(size, angle)
        i=i+1

def draw_rectangle(size1, size2):
    i=1
    while i<=2:
        my_turtle.forward(size1)
        my_turtle.right(90)
        my_turtle.forward(size2)
        my_turtle.right(90)
        i=i+1

def draw_triangle(size1, angle1, size2, angle2, size3, angle3):
    i=1
    while i<=1:
        my_turtle.right(angle1)
        my_turtle.forward(size1)
        my_turtle.right(180-angle2)
        my_turtle.forward(size2)
        my_turtle.right(180-angle3)
        my_turtle.forward(size3)
        i=i+1

def draw_quadrilateral(angle1, size1, angle2, size2, angle3, size3, angle4, size4):
    i=1
    while i<=1:
        my_turtle.right(angle1)
        my_turtle.forward(size1)
        my_turtle.right(180-angle2)
        my_turtle.forward(size2)
        my_turtle.right(180-angle3)
        my_turtle.forward(size3)
        my_turtle.right(180-angle4)
        my_turtle.forward(size4)
        i=i+1

my_turtle=turtle.Turtle()

my_turtle.teleport(-200,100)
draw_rectangle(400,300)

my_turtle.teleport(-50,-60)
draw_rectangle(90,140)

my_turtle.teleport(-210,100)
draw_triangle(245,-30,245,120,425,30)

my_turtle.teleport(75,250)
draw_quadrilateral(180,50,90,98,60,58,120,70)

my_turtle.teleport(0,0)

time.sleep(5)