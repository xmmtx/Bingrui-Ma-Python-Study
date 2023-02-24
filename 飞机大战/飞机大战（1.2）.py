import pygame
import time
pygame.init()
screen = pygame.display.set_mode((512,568))
background = pygame.image.load('./images/bg2.jpg')
plane=pygame.image.load('./images/me.png')
m=-(1536-568)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    m=m+2
    if m>=0:
        m=-968
    screen.blit(background,(0,m))
    screen.blit(plane,(100,200))
    screen.blit(plane,(300,100))
    pygame.display.update()
    time.sleep(0.05)
pygame.quit()