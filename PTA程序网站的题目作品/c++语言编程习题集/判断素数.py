n=eval(input())
if n<=1:
    print('NO')
elif n==2:
    print('YES')
else:
    for i in range(2,n):
        if n % i == 0:
            break
    if i >=n-1:
        print('YES')
    else:
        print('NO')