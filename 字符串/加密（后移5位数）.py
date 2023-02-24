# str1='abcd uvwxyz'
str1=input('兄dei，亲，请输入一个字符串：')
list1=[]
for x in str1:
    list1.append(x)
n=len(list1)
for i in range(n):
    if list1[i]>='a' and list1[i]<='z':
        if list1[i]>='v' and list1[i]<='z':
            n=ord('v')
            n1=ord(list1[i])
            list1[i]=chr(97+n1-n)
        else:
            nn=ord(list1[i])
            list1[i]=chr(nn+5)
print(str1)
str2=''.join(list1)
print(str2)