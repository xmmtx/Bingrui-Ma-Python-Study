'''
大于等于90分为A；
小于90且大于等于80为B；
小于80且大于等于70为C；
小于70且大于等于60为D；
小于60为E。
'''
a=eval(input())
if a>=90:
    print('A')
else:
    if a>=80:
        print('B')
    else:
        if a>=70:
            print('C')
        else:
            if a>=60:
                print('D')
            else:
                print('E')