import turtle

s = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')

for i in range(180):
    t.pencolor(colors[i%6])
    t.width(i // 100 + 1)
    t.forward(i)
    t.left(59)
s.exitonclick()