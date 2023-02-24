'''
当运算符为+、-、*、/、%时，在一行输出相应的运算结果。若输入是非法符号（即除了加、减、乘、除和求余五种运算符以外
的其他符号）则输出ERROR。
'''
s=input()
nums=s.split()
s1=eval(nums[0])
f=eval(nums[1])
s2=eval(nums[2])
if f=='-':
    d=s1-s2
elif f=='+':
    d=s1+s2
elif f=='*':
    d=s1*s2
elif f=='/':
    d=s1/s2
elif f=='%':
    d=s1/s2
else:
    print("ERROR")
print(d)