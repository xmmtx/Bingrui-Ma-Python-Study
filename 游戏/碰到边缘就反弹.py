import pygame
pygame.init()
screen=pygame.display.set_mode([640,500])
pic=pygame.image.load("D:\\ball\\CrazySmile.bmp")
timer=pygame.time.Clock()
x=270
y=200
speedX=5
speedY=5
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.set_caption('圆心坐标：('+str(x)+','+str(y)+')')
    if y>500-100:
        speedY=-5
    if x>640-100:
        speedX=-5
    if y<0:
        speedY=5
    if x<0:
        speedX=5
    x=x+speedX
    y=y+speedY
    print(x,y)
    screen.blit(pic,(x,y))
    timer.tick(9999999999999999999)
    pygame.display.update()
pygame.quit()