import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('cyan')
t.speed(0)
for i in range(50):
    t.circle(150-1,90)
    t.lt(98)
    t.circle(150-1,90)
    t.lt(18)
s.exitonclick()