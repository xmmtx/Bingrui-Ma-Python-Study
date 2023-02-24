list1=[]
for i in range(0,10):
    str1=str(i+1)
    n=eval(input('请输入第'+str1+'个数：'))
    list1.append(n)
print('输入的10个数分别是：')
for m in list1:
    print(m,end=' ')
for i in range(0,10):
    if list1[i]%2==0:
        list1[i]=list1[i]/2
    else:
        list1[i]=list1[i]*2

print(list1)