import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.speed(0) #可变速度
t.width(2) #可变宽度
n=100
jd=360/n
t.pencolor('white')
for x in range(25):
  t.circle(100)
  t.left(jd)
  t.pencolor('red')
  t.circle(100)
  t.left(jd)
  t.pencolor('white')
  t.circle(100)
  t.left(jd)
  t.pencolor('blue')
  t.circle(100)
  t.left(jd)
  t.pencolor('white')
t1=turtle.Pen()
t1.speed(0) #可变速度
t1.width(2) #可变宽度
for x in range(25):
  t.circle(50)
  t.left(jd)
  t.pencolor('red')
  t.circle(50)
  t.left(jd)
  t.pencolor('white')
  t.circle(50)
  t.left(jd)
  t.pencolor('blue')
  t.circle(50)
  t.left(jd)
  t.pencolor('white')
turtle.done()