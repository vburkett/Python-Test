import regularPolygons
from time import *
from turtle import Turtle

myname = input("Enter your name: ")
print("Hello " + myname+"!")

boxsize = input("Enter the size of the box: ")
boxsize = int(boxsize)

my_turtle=Turtle()
regularPolygons.draw_regular_polygon(my_turtle, boxsize, 4)

sleep(10)