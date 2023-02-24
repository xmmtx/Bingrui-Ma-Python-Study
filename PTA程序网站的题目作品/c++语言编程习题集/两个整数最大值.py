s=input()
nums=s.split()
a=eval(nums[0])
b=eval(nums[1])
max=a
if max < b:
    max=b
else:
    max=a
print('max=',max,sep='')