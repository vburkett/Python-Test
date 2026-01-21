# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import turtle

from turtle import *

#triangle creation
teleport(-250,0)
forward(100)
left(120)
forward(100)
left(120)
forward(100)

#reset forward
left(120)

#octagon creation
teleport(-13,0)
forward(36)
left(45)
forward(36)
left(45)
forward(36)
left(45)
forward(36)
left(45)
forward(36)
left(45)
forward(36)
left(45)
forward(36)
left(45)
forward(36)

#reset forward
left(45)

#hexagon creation
teleport(175,0)
forward(50)
left(60)
forward(50)
left(60)
forward(50)
left(60)
forward(50)
left(60)
forward(50)
left(60)
forward(50)
left(60)

#stay on screen after drawing
turtle.done()