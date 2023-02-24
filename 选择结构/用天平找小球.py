s=input()
nums=s.split()
a=eval(nums[0])
b=eval(nums[1])
c=eval(nums[2])
if a!=b and a==c:
    print('b')
if a==b and a!=c:
    print('c')
if a!=b and a!=c:
    print('a')