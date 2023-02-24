def scope():
    global a
    a=1
    print('函数脮脮中，a,b的值是：a=',a,' b=',b,sep='')
a=10
b=20
scope()
print('函数爽歪歪中，a,b的值是：a=',a,' b=',b,sep='')