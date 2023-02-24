n=0
for gb in range(0,23):
    for qb in range(0,46):
        qx=100-(gb+qb)
        n+=1
        if gb*4+qb*2+qx*0.5==90:
            print('钢笔：',gb,'支，铅笔：',qb,'枝，铅芯：',qx,'根。',sep='')
print('总共循环了',n,'次。')