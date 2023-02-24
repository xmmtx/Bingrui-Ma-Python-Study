import pygame
import time
def main():
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
        screen.blit(plane,(100,0))
        screen.blit(plane,(0,100))
        screen.blit(plane,(512-206,300))
        screen.blit(plane,(300,512-206))
        pygame.display.update()
        time.sleep(0.05)
    pygame.quit()
if __name__ =='__main__':
    main()