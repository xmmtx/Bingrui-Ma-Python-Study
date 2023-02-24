import pygame
pygame.init()
screen=pygame.display.set_mode([640,500])
pic=pygame.image.load("D:\\ball\\CrazySmile.bmp")
timer=pygame.time.Clock()
x=270
y=200
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.set_caption('圆心坐标：('+str(x)+','+str(y)+')')
    x-=5
    y+=5
    screen.blit(pic,(x,y))
    timer.tick(60)
    pygame.display.update()
pygame.quit()