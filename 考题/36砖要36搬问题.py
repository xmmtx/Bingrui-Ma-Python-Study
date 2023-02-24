n=0
for n1 in range(0,10):
    for n2 in range(0,19):
        xh=36-(n1+n2)
        n+=1
        if n1*4+n2*3+xh/2==36:
            print('男生：',n1,'人搬，女生：',n2,'人搬，小孩：',xh,'人搬。',sep='')
print('总共循环了',n,'次。')