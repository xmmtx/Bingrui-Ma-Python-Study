n=eval(input('请输入一个整数：'))
if n<=1:
    print('1或者负数不是素数。')
elif n==2:
    print('2是素数。')
else:
    for i in range(2,n):
        if n % i == 0:
            break
    if i >=n-1:
        print(n,'是素数。',sep='')
    else:
        print(n,'不是素数。',sep='')