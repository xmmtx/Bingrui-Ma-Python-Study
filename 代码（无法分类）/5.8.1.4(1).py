a = eval(input("请输入第一个整数："))
b = eval(input("请输入第二个整数："))
c = eval(input("请输入第三个整数："))
if a>b:
    t=a
    a=b
    b=t
if b>c:
    t=c
    c=b
    b=t
if a>b:
    t=a
    a=b
    b=t
print(a,b,c)