import pygame
import time
from pygame.locals import *
sd=5
class HeroPlane:
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 400
        self.screen = screen_temp
        self.image = pygame.image.load("./images/me.png")
        self.bullet_list = []
        self.fireMusic=pygame.mixer.Sound("./music/hero_fire.wav")
    def display(self): 
        for bullet in self.bullet_list:
            bullet.display()
            isOverBorder=bullet.move()
            if  isOverBorder:
                self.bullet_list.remove(bullet)
        self.screen.blit(self.image, (self.x, self.y))
    def move_left(self):
        self.x -=sd
        if self.x<0:
            self.x=0
    def move_right(self):
        self.x +=sd
        if self.x > 406:
            self.x = 406
    def move_up(self):
        self.y -=sd
        if self.y<0:
            self.y=0
    def move_down(self):
        self.y +=sd
        if self.y >568-76:
            self.y =568-76
    def fire(self):
        bullet=Bullet(self.screen, self.x, self.y)
        self.bullet_list.append(bullet)
        print(len(self.bullet_list))
        self.fireMusic.play()
class Bullet:
    def __init__(self, screen_temp, x, y):
        self.x = x+51
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load("./images/pd.png")
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y -= 10
        if self.y<-20:
            return True 
        else:
            return False
def key_control(hero_temp):
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        hero_temp.move_left()
        print('left')    
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        hero_temp.move_right()
        print('right')
    elif pressed_keys[K_x] or pressed_keys[K_DOWN]:
        hero_temp.move_down()
        print('down')
    elif pressed_keys[K_UP] or pressed_keys[K_w]:
        hero_temp.move_up()
        print('up')
    if pressed_keys[K_SPACE]:
        print('space')
        hero_temp.fire()
def main():
    pygame.init()
    screen = pygame.display.set_mode((512,568)) 
    background = pygame.image.load("./images/bg2.jpg")
    pygame.mixer.init()
    pygame.mixer.music.load("./music/PlaneWarsBackgroundMusic.mp3") 
    m=-(1536-568)  
    hero=HeroPlane(screen) 
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        m=m+2
        if m>=0:
            m=-968
        screen.blit(background,(0,m))
        key_control(hero)
        hero.display()
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
        pygame.display.update()
        time.sleep(0.05)
    pygame.quit()
if __name__ == "__main__":
    main()