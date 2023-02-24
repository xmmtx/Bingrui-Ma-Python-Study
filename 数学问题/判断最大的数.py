a1=eval(input("请输入第一个数："))
a2=eval(input("请输入第二个数："))
a3=eval(input("请输入第三个数："))
a4=eval(input("请输入第四个数："))
max=a1
if max < a2:
    max=a2
if max < a3:
    max=a3
if max < a4:
    max=a4
print(max)