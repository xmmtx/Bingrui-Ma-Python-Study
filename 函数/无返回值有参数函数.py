import turtle
def drawLine(color,r):
    t=turtle.Pen()
    t.pencolor(color)
    t.pensize(2)
    t.circle(r)
drawLine('red',50)
drawLine('blue',80)
turtle.done()