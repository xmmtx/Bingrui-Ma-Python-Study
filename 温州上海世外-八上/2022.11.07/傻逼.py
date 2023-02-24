a=float(input("请输入三角形第一边长："))
b=float(input("请输入三角形第二边长："))
c=float(input("请输入三角形第三边长："))
if a>=b+c or b>=a+c or c>=a+b:
    print('不能组成三角形')
else:
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print('三角形的面积为：',s,sep='')
    print('三角形的周长为：',a+b+c,sep='')