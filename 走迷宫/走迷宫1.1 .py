map=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,2,0,1,0,0,0,0,0,0,1,0,1,0,0],
        [1,0,1,1,0,1,1,1,0,1,1,0,0,0,1],
        [1,0,0,1,0,1,0,0,0,0,1,0,1,1,1],
        [1,1,0,0,0,1,1,1,1,0,0,0,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
print("初始地图如下:")
for i in range(6):
    print(map[i])
x=1 
y=1
while True:
    s=input("输入方向键(a-左移，d-右移，s-下移，w-上移：)")
    if s=="a": 
        if map[x][y-1]!=1:
            map[x][y]=0
            y-=1
            map[x][y]=2
        else:
            print("左侧是墙壁，不能左移了")
    else:
        if s=='d':
            if map[x][y+1]!=1:
                map[x][y]=0
                y+=1
                map[x][y]=2
            else:
                print('右侧是墙壁，不能右移了')
        else:
            if s=='w':
                if map[x-1][y]!=1: #左侧不是墙壁
                    map[x][y]=0
                    x-=1
                    map[x][y]=2
                else:
                    print("上边是墙壁，不能上移了")
            else:
                if s=='s':
                    if map[x+1][y]!=1: #左侧不是墙壁
                        map[x][y]=0
                        x+=1
                        map[x][y]=2
                    else:
                        print("下边是墙壁，不能下移了")
    print("x:",x,"y:",y)
    print("移动后的内容是:")
    for i in range(6):
        print(map[i])
    if x==1 and y==14:
        print("恭喜，你走出了迷宫")
        break
