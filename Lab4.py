import turtle

nate = turtle.Turtle()
i=0
while i<=17:
    nate.right(90)
    nate.forward(5*i+10)
    nate.right(90)
    nate.forward(5*i+10)
    i=i+1

turtle.done()