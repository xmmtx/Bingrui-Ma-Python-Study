roles=['机器猫','孙悟空','葫芦娃','变形金刚','白雪公主']
role=input('请输入你需要查找的姓名：')
if role in roles:
    print('恭喜，在列表中存在‘',role,'’的昵称！',sep='')
else:
    print('抱歉，在列表中不存在‘',role,'’的名字！')