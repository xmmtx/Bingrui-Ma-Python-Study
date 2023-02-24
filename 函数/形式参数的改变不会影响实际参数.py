def change(a):
    a*=2
    print('调用函数时，形参a的值发送了改变，a=',a,sep='')
n=5
print('调用函数前，n的值是：',n,sep='')
change(n)
print('调用函数后，n的值是：',n,sep='')