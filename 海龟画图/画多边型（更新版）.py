import turtle
t=turtle.Pen()
t.pencolor('white')
t.right(90)
t.forward(100)
n=int(turtle.numinput("输入框","请输入一个整数："))
t.left(90)
t.pencolor('black')
jd=360/n
for x in range(n):
    t.forward(100)
    t.left(jd)
turtle.done()