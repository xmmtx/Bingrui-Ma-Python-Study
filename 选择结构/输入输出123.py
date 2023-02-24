a=eval(input("请输入第一个数："))
b=eval(input("请输入第二个数："))
c=eval(input("请输入第三个数："))
max=a
if max < b:
    max=b
if max < c:
    max=c
print(max)