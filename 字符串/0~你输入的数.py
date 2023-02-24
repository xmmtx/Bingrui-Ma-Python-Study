def sum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
a=eval(input('请输入一个整数：'))
b=sum(a)
print('1+2+3+...+',a,'=',b,sep='')