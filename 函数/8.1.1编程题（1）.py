def sum(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
m=eval(input())
d=sum(m)
print('1*...*m=',d)