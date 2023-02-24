s=input('请输入一个小写字符：')
if s=='z':
    c2='a'
else:
    n=ord(s)
    c2=chr(n+1)
print(c2)