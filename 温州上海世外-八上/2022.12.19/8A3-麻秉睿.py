a=int(input('请输㵘棋盘的格数：'))
p=1
s=0
for i in range(1,a+1):
    s+=p
    p*=2
    print("麦粒总数：",s,sep="")
print("㵘棋盘的格数：",a,"麦粒总数：",s,sep="")
print("水仙花数：")
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
