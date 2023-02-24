scores=[90,82,95,98,88]
n=len(scores)
s=0
for score in scores:
    s=s+score
zgf=max(scores)
zdf=min(scores)
pjf=s/n
print('总分：',s,'；平均分：',pjf,sep='')
print('最高分：',zgf,'；最低分：',zdf,sep='')