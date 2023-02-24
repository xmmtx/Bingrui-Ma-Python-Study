import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
for i in range(1,201):
    if i%4==0:
        t.pencolor('red')
    elif i%4==1:
        t.pencolor('yellow')
    elif i%4==2:
        t.pencolor('green')
    else:
        t.pencolor('blue')
    t.forward(i)
    t.left(19)
turtle.done()