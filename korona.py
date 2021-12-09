import turtle
t = turtle.Turtle()
s = turtle.Screen()

t.speed(13)
t.pencolor('cyan') #fuchsia
s.bgcolor('black')
t.write('Virus',align='left', font=('Verdana', 30, 'normal'))
t.forward(-50)

for i in reversed(range(200)):
    t.right(i)
    t.forward(i)
s.exitonclick()