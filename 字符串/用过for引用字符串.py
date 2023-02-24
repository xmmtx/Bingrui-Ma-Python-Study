str1=input('请输入一个字符串：')
dx=0
xx=0
qt=0
for x in str1:
    if x>='A' and x<='Z':
        dx+=1
    elif x>='a' and x<'z':
        xx+=1
    else:
        qt+=1
print('大写字母有',dx,'个；',sep='')
print('小写字母有',xx,'个；',sep='')
print('其他字母有',qt,'个。',sep='')