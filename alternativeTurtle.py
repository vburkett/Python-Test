import turtle
screen = turtle.Screen()
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

my_turtle=turtle.Turtle()

draw_regular_polygon(100,4)

my_turtle.penup()
my_turtle.setpos(200,0)
my_turtle.pendown()

draw_regular_polygon(50,8)

time.sleep(5)