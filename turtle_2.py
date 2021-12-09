import turtle

k = turtle.Screen()
turtle.bgcolor('black')
turtle.shape("turtle")
t5 = turtle.Turtle()
t5.speed(0)

for i in range(10):
    for i in range(4):
        t5.pu()
        t5.goto(50,50)
        t5.pd()
        t5.color("cyan")
        t5.pensize(3)
        t5.circle(100,steps=6)
        t5.right(100)
k.exitonclick()