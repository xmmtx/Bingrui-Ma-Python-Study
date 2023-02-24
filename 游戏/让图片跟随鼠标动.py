import pygame
pygame.init()
screen=pygame.display.set_mode([640,500])
picDangBan=pygame.image.load("d:\\ball\\挡板3.png")
picDangBan=pygame.transform.scale(picDangBan,(200,30))
picDangBanW=picDangBan.get_width()
BLACK=(0,0,0)
x=100
y=400
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
    pygame.display.update()
pygame.quit()