s=input()
nums=s.split()
a=eval(nums[0])
b=eval(nums[1])
if b<=40:
    if a>=5:
        n=b*50
    else:
        n=b*30
else:
    if a>=5:
        n=40*50+(b-40)*1.5*50
    else:
        n=40*30+(b-40)*1.5*30
print("***************************************************************")
print('%.2f'%n)