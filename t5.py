from turtle import Turtle, Screen
t = Turtle()
s = Screen()

s.bgcolor('white')
t.pencolor('blue')
t.speed(100)
for i in range(150):
    t.circle(100,5)
    t.lt(1)
    t.circle(100)
    t.lt(1)
s.exitonclick()