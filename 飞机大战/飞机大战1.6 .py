import pygame
import time
from pygame.locals import *
sd=5
class HeroPlane:
    def __init__(self,screen_temp):
        self.x = 200
        self.y = 400
        self.screen = screen_temp
        self.image = pygame.image.load('./images/me.png')
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move_left(self):
        self.x-=sd
        if self.x<0:
            self.x=0
    def move_right(self):
        self.x+=sd
        if self.x>406:
            self.x=406
    def move_up(self):
        self.y-=sd
        if self.y<0:
            self.y=0
    def move_down(self):
        self.y+=sd
        if self.y>568-76:
            self.y=568-76
def main():
    pygame.init()
    screen = pygame.display.set_mode((512,568))
    background = pygame.image.load('./images/bg2.jpg')
    plane=pygame.image.load('./images/me.png')
    m=-(1536-568)
    # x=200
    # y=568-76
    hero=HeroPlane(screen)
    # sd=5
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
            # x=x-sd
            hero.move_left()
            print('←')
            # if x<=0 :
            #     x=x+sd
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            # x=x+sd
            hero.move_right()
            print('→')
            # if x>=512-106 :
            #     x=x-sd
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            # y=y+sd
            hero.move_down()
            print('↓')
            # if y>=568-76 :
            #     y=y-sd
        elif pressed_keys[K_UP] or pressed_keys[K_w]:
            # y=y-sd
            hero.move_up()
            print('↑')
            # if y<=0 :
            #     y=y+sd
        elif pressed_keys[K_SPACE]:
            print('空格')
        # screen.blit(plane,(x,y))
        hero.display()
        pygame.display.update()
        time.sleep(0.05)
    pygame.quit()
if __name__ =='__main__':
    main()