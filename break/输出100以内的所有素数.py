print(2,end=' ')
for n in range(3,101):
    for i in range(2,n):
        if n % i == 0:
            break
    if i >=n-1:
        print(n,end=' ')