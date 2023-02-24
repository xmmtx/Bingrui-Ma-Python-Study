def ff():
    c=d+40
    print('函数内部使用了全局变量，c=',c,sep='')
d=40
ff()
f=d+100
print('f=',f,sep='')