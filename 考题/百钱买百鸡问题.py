n=0
for gj in range(0,101):
    for mj in range(0,101):
        for xj in range(0,101):
            n+=1
            if gj+mj+xj==100 and gj*5+mj*3+xj/3==100:
                print('公鸡：',gj,'只，母鸡：',mj,'只，小鸡：',xj,'只。',sep='')
print('总共循环了',n,'次。')