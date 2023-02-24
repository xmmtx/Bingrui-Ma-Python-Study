a=float(input("请输入行驶路程："))
if a>3:
    b=10+(a-3)*2
    if not b%1==0:
        b=b-(b%1)
        b+=2
    print('需要支付',b,'元！',sep='')
else:
    print('需要支付10.0元！')