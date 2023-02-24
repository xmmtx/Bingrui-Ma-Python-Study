import pygame
pygame.init()
screen=pygame.display.set_mode([640,500])
picDangBan=pygame.image.load("d:\\ball\\挡板3.png")
picDangBan=pygame.transform.scale(picDangBan,(200,30))
picDangBanW=picDangBan.get_width()
BLACK=(0,0,0)
x=100
y=400
pop=pygame.mixer.Sound('D:\\ball\\pop2.wav')
blap=pygame.mixer.Sound('D:\\ball\\blap.wav')
pic=pygame.image.load('D:\\ball\\CrazySmile.bmp')
pic=pygame.transform.scale(pic,(60,60))
picW=pic.get_width()
picH=pic.get_height()
picX=100
picY=100
speedX=5
speedY=5
timer=pygame.time.Clock()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill(BLACK)
    pos=pygame.mouse.get_pos()
    x=pos[0]
    y=pos[1]
    x=x-picDangBanW/2
    screen.blit(picDangBan,(x,400))
    pygame.display.set_caption('('+str(x)+','+str(y)+')')
    if picY<=0:
        speedY=-speedY
    if picX>=640-picW or picX<=0:
        speedX=-speedX
    if picY>=500-picH:
        blap.play()
        speedY=-speedY
    picX+=speedX
    picY+=speedY
    screen.blit(pic,(picX,picY))
    timer.tick(60)
    pygame.display.update()
pygame.quit()