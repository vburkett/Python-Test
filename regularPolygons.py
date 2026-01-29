from turtle import Turtle

my_turtle = Turtle()

def draw_side(my_turtle, size, angle):
    my_turtle.forward(size)
    my_turtle.right(angle)

def draw_square(my_turtle,size):
    i=1
    while i<=4:
        draw_side(my_turtle, size, 90)
        i=i+1

def draw_regular_polygon(my_turtle,size, sides):
    angle = 360/sides
    i=1
    while i<=sides:
        draw_side(my_turtle, size, angle)
        i=i+1