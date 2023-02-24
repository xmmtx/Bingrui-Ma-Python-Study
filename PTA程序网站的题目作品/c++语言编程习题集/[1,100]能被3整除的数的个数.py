k=0
a=1
b=0
c=0
d=0
for i in range(0,100):
    b+=1
    c=a*(b)
    if c%3==0:
        d+=1
print(d)