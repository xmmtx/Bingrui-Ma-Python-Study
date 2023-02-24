a=eval(input("请输入第一个数："))
b=eval(input("请输入第二个数："))
c=a*a+b*b
if c>=100:
    c//100
    print(c)
else:
    c=a+b
    print(c)