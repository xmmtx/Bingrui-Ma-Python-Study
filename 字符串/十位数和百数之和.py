def digitSu(a):
    gw=a%10
    sw=a//10%10
    bw=a//100%10
    s=gw+sw+bw
    print(a,'的各位数之和是：',s,sep='')
n=eval(input('请输入一个三位数：'))
digitSu(n)