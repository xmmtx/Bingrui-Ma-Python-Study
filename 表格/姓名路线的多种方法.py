#第一种方法：
names=['张三','李四','王五','赵六','唐七']
i=0
while i<5:
    print(names[i],end=' ')
    i=i+1
print('\n程序执行完毕')

#第二种方法：
for name in ['张三','李四','王五','赵六','唐七']:
    print(name,end=' ')
print('\n程序执行完毕')

#第三种方法：
names=['张三','李四','王五','赵六','唐七']
for name in names:
    print(name,end=' ')
print('\n程序执行完毕')

#第四种方法：
names=['张三','李四','王五','赵六','唐七']
for i in [0,1,2,3,4]:
    print(names[i],end=' ')
print('\n程序执行完毕')