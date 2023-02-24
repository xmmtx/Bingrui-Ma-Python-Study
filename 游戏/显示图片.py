import pygame
pygame.init()
screen=pygame.display.set_mode([640,500])
pic=pygame.image.load("d:\\ball\\CrazySmile.bmp")
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(pic,(100,200))
    screen.blit(pic,(300,100))
    pygame.display.update()
pygame.quit()