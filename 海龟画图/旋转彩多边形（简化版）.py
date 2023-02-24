import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
colors=['red','yellow','green','blue','orange','purple']
n=int(turtle.numinput('输入框','请输入一个1~360的数：',360))
for i in range(1,201):
    color=colors[i%6]
    t.pencolor(color)
    t.forward(i)
    t.left(360/n+1)
turtle.done()