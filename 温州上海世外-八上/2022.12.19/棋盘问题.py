a=int(input('请输㵘棋盘的格数：'))
p=1
s=0
for i in range(1,a+1):
    s+=p
    p*=2
    print("麦粒总数：",s,sep="")
print("㵘棋盘的格数：",a,"麦粒总数：",s,sep="")