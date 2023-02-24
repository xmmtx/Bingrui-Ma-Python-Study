scores=[89,90,85,66,98,72]
n=len(scores)
for i in range(0,n):
    scores[i]=scores[i]+10
print('改变列表值后的情况：')
for score in scores:
    print(score,end=' ')