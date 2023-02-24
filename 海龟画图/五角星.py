import turtle
t=turtle.Pen()
j=5
turtle.bgcolor('blue')
t.pencolor('red')
t.begin_fill()
t.fillcolor('red')
t.left(36)
for sdftgy in range(j):
    t.forward(150)
    t.left(180-36)
t.end_fill()
turtle.done()