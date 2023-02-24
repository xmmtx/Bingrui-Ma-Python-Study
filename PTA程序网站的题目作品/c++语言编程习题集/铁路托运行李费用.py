a=eval(input())
if a<=10:
    b=a*1.3
else:
    if a>10 and a<=50:
        b=a*1.8
    else:
        if a>50 and a<=200:
            b=a*2.4
        else:
            b=a*4.5
if b<0:
    print('Error')
print(b)