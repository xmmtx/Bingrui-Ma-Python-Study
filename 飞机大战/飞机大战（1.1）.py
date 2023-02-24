import pygame
pygame.init()
screen = pygame.display.set_mode((512,568))
background = pygame.image.load('./images/bg2.jpg')
plane=pygame.image.load('./images/me.png')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(background,(0,0))
    screen.blit(plane,(100,200))
    screen.blit(plane,(300,100))
    pygame.display.update()
pygame.quit()