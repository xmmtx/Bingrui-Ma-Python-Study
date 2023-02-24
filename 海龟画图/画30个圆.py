import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.speed(0) #可变速度
# t.width(3)
n=30
jd=360/n
t.pencolor('#FFFFFF')
for x in range(n):
  t.circle(100)
  t.left(jd)

t.pencolor('#FFFF00')
for x in range(n):
  t.circle(90)
  t.left(jd)

t.pencolor('red')
for x in range(n):
  t.circle(80)
  t.left(jd)

t.pencolor('#00ff00')
for x in range(n):
  t.circle(70)
  t.left(jd)

t.pencolor('#FFFF00')
for x in range(n):
  t.circle(60)
  t.left(jd)

t.pencolor('#7FFF00')
for x in range(n):
  t.circle(50)
  t.left(jd)

t.pencolor('#436EEE')
for x in range(n):
  t.circle(40)
  t.left(jd)

t.pencolor('#00EE00')
for x in range(n):
  t.circle(30)
  t.left(jd)

t.pencolor('#ABABAB')
for x in range(n):
  t.circle(20)
  t.left(jd)

t.pencolor('#B03060')
for x in range(n):
  t.circle(10)
  t.left(jd)

turtle.done()