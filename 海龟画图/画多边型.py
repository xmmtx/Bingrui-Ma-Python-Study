import turtle
t=turtle.Pen()
n=6 #可变边数
jd=360/n
for x in range(n):
    t.forward(100)
    t.left(jd)
turtle.done()