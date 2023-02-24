#第一种方法：
i=1
sum=0
while i<=20:
    sum=sum+i
    i=i+2
print("1+2+...+19=",sum)

#第二种方法：
i=1
sum=0
while i<=20:
    if i%2==1:
        sum=sum+i
    i=i+1
print("1+2+...+19=",sum)