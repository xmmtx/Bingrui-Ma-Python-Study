# str1='abcd uvwxyz'
str1=input('兄dei，亲，请输入一个该死的字符串：')
list1=[]
for x in str1:
    list1.append(x)
n=len(list1)
for i in range(n):
    if list1[i]>='A' and list1[i]<='Z':
        n1=ord(list1[i])
        list1[i]=chr(n1+32)
    elif list1[i]>='a' and list1[i]<='z':
        n1=ord(list1[i])
        list1[i]=chr(n1-32)
print(str1)
str2=''.join(list1)
print(str2)