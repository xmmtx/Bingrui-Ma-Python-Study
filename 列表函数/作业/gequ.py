list1=[]
for i in range(0,10):
    str1=str(i+1)
    n=eval(input('请输入第'+str1+'个数：'))
    list1.append(n)
print('输入的10个数分别是：')
for m in list1:
    print(m,end=' ')
s=0
for x in list1:
    s=s+x
zgf=max(list1)
zdf=min(list1)
s=s-(zgf+zdf)
s=s/8
print('\n这位歌手的平均分是:',s,sep='')