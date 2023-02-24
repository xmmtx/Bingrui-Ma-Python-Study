str1=input('请输入一个字符串：')
dx=0
xx=0
sz=0
kg=0
ssfh=0
zwfh=0
qt=0
for x in str1:
    if x>='A' and x<='Z':
        dx+=1
    elif x>='a' and x<'z':
        xx+=1
    elif x>='0' and x<'9':
        sz+=1
    elif x==' ':
        kg+=1
    elif x=='+' or x=='-' or x=='*' or x=='/' or x=='=' or x=='<' or x=='>':
        ssfh+=1
    elif x=='，' or x=='。' or x=='！' or x=='？' or x=='……' or x=='——' or x=='、' or x=='（' or x=='）' or x=='‘' or x=='’' or x=='“' or x=='”' or x=='：' or x=='；':
        zwfh+=1
    else:
        qt+=1
print('大写字母有',dx,'个；',sep='')
print('小写字母有',xx,'个；',sep='')
print('数字有',sz,'个；',sep='')
print('空格有',kg,'个；',sep='')
print('数学符号有',ssfh,'个；',sep='')
print('中文符号有',zwfh,'个；',sep='')
print('中文和其他字符有',qt,'个。',sep='')