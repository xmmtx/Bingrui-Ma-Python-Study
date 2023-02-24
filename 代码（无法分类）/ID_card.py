weight_list=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ID_number_list=[]
IDnumber_17=input()
the_sum=0
for i in IDnumber_17:
	ID_number_list.append(i)
for i in range(17):
	the_sum+=int(ID_number_list[i])*weight_list[i]
remainder=the_sum%11
#check
check_code_list=['1','0','X','9','8','7','6','5','4','3','2']
check_code=check_code_list[remainder]
# print('身份证校验码是：'+check_code)
print(IDnumber_17+check_code)






























# C++代码
# #include<iostream>
# #include<stdio.h>
# using namespace std;
# int main()
# {
# 	char a[18];
# 	int c[17]={7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2};
# 	char b[11]={'1','0','X','9','8','7','6','5','4','3','2'};
# 	int sum=0,i,j;
# 	gets(a);
# 	for(i=0;i<17;i++)
# 	{
# 		sum+=(a[i]-'0')*c[i];
# 	}
# 	j=sum%11;
# //printf("%c",b[j]);
# 	for(int i=0;i<17;i++)
# 		cout<<a[i];
# 	cout<<b[j]<<endl;
# 	return 0;
# }