jd1=eval(input("请输入1斤鸡蛋的价格："))
ny1=eval(input("请输入1斤奶油的价格："))
mf1=eval(input("请输入1斤面粉的价格："))

jd2=eval(input("请输入要买鸡蛋的数量："))
ny2=eval(input("请输入要买奶油的数量："))
mf2=eval(input("请输入要买面粉的数量："))

jd3=jd1*jd2
ny3=ny1*ny2
mf3=mf1*mf2

n=jd3+ny3+mf3
print("zhr需要带",n,"元。")