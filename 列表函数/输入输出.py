list1=[]
for i in range(0,5):
    str1=str(i+1)
    n=eval(input('请输入第'+str1+'个数：'))
    list1.append(n)
print('输入的5个数分别是：')
for m in list1:
    print(m,end=' ')