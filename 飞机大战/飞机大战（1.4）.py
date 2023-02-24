import pygame
import time
from pygame.locals import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((512,568))
    background = pygame.image.load('./images/bg2.jpg')
    plane=pygame.image.load('./images/me.png')
    m=-(1536-568)
    x=200
    y=568-76
    sd=5
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        m=m+2
        if m>=0:
            m=-968
        screen.blit(background,(0,m))
        # screen.blit(plane,(300,100))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            x=x-sd
            print('←')
            if x<=0 :
                x=x+sd
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            x=x+sd
            print('→')
            if x>=512-106 :
                x=x-sd
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            y=y+sd
            print('↓')
            if y>=568-76 :
                y=y-sd
        elif pressed_keys[K_UP] or pressed_keys[K_w]:
            y=y-sd
            print('↑')
            if y<=0 :
                y=y+sd
        elif pressed_keys[K_SPACE]:
            print('空格')
        screen.blit(plane,(x,y))
        pygame.display.update()
        time.sleep(0.05)
    pygame.quit()
if __name__ =='__main__':
    main()