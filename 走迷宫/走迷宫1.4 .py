import pygame
pygame.mixer.init()
pygame.mixer.music.load("./music/迷宫配乐2.mp3")
if pygame.mixer.music.get_busy() == False:
    pygame.mixer.music.play()
map=[
        [1,1,1,1,1,1,1,1,1,1,1],
        [1,2,0,1,0,0,0,0,0,0,1],
        [1,0,1,1,0,1,1,1,0,1,1],
        [1,0,0,1,0,1,0,0,0,0,1],
        [1,1,0,0,0,1,1,1,1,0,0],
        [1,1,1,1,1,1,1,1,1,1,1]
    ]
m=len(map)
m1=len(map[0])
x=1
y=1
def move_left():
    global map,x,y
    if map[x][y-1]!=1:
        map[x][y]=0
        y-=1
        map[x][y]=2
def move_right():
    global map,x,y
    if map[x][y+1]!=1:
        map[x][y]=0
        y+=1
        map[x][y]=2
def move_up():
    global map,x,y
    if map[x-1][y]!=1:
        map[x][y]=0
        x-=1
        map[x][y]=2
def move_down():
    global map,x,y
    if map[x+1][y]!=1:
        map[x][y]=0
        x+=1
        map[x][y]=2
def main():
    global map,x,y
    pygame.init()
    screen = pygame.display.set_mode((720,500)) 
    background = pygame.image.load("./images/背景3.jpg") 
    w=40
    h=40
    background=pygame.transform.scale(background,(720,500))
    background = pygame.image.load("./images/背景3.jpg")  
    background=pygame.transform.scale(background,(720,500))
    bgmg = pygame.image.load("./images/墙4.jpg")   
    bgmg=pygame.transform.scale(bgmg,(w,h))
    td = pygame.image.load("./images/通道1.jpg")   
    td=pygame.transform.scale(td,(w,h))
    mouse = pygame.image.load("./images/人物2.jpg")    
    mouse=pygame.transform.scale(mouse,(w,h))
    while True:
        for event in pygame.event.get():   
            if event.type==pygame.QUIT: 
                exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT: 
                    move_left()
                elif event.key==pygame.K_RIGHT: 
                    move_right()
                elif event.key==pygame.K_UP: 
                    move_up()
                elif event.key==pygame.K_DOWN: 
                    move_down()
                print("x:",x,"y:",y)
        screen.blit(background,(0,0))
        for x1 in range(m):
            for y1 in range(m1):
                if map[x1][y1]==1:
                    screen.blit(bgmg,(100+y1*w,100+x1*h))
                elif map[x1][y1]==0:
                    screen.blit(td,(100+y1*w,100+x1*h))
                else:
                    screen.blit(mouse,(100+y1*w,100+x1*h))        
        if x==4 and y==10:
            print("\n恭喜，你走出了迷宫")
            break
        pygame.display.update()
    pygame.quit()
if  __name__ == "__main__":
    main()