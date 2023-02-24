def sxh(n):
    gw=n%10
    sw=n//10%10
    bw=n//100%10
    if n==gw*gw*gw+sw*sw*sw+bw*bw*bw:
        return 1
    else:
        return 0
for i in range(100,1000):
    if sxh(i)==1:
        print(i)