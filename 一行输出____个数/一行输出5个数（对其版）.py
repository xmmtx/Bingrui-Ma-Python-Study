n=0  #用于统计输出了几个数
for i in range(4,100):
    print('%-2d'%i,end=' ')
    n+=1
    if n%5==0:    #判断n如果能被5整除
        print()    #   输出换行
print('\n总共输出了',n,'个数。')
print('over')