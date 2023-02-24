import pygame
import time
from pygame.locals import *
zjsd=100
djsd=4
import random
class EnemyPlane:
    def display(self):
        self.move()
        if self.hit==True:
            bombpicture=self.bomb_picture_list[self.image_index]
            self.screen.blit(bombpicture,(self.x,self.y))
            self.image_index+=1
            if self.image_index>self.bomb_picture_num-1:
                self.image_index=self.bomb_picture_num-1
                self.isValid=False
    def isHitted(self,plane):
        width=self.image.get_width()
        height=self.image.get_height()
        for bullet in plane.bullet_list:
            if bullet.x>=self.x and bullet.x<=self.x+width and bullet.y<=self.y+height:
                plane.bullet_list.remove(bullet)
                self.hit=True
                print('击中了敌机')
                self.bomb=pygame.mixer.Sound("./music/bomb.wav")
                self.bomb.play()
def main():
    pygame.init()
    screen = pygame.display.set_mode((512,568)) 
    background = pygame.image.load("./images/bg2.jpg")
    pygame.mixer.init()
    pygame.mixer.music.load("./music/PlaneWarsBackgroundMusic.mp3") 
    m=-(1536-568)  
    hero=HeroPlane(screen)
    enemy=EnemyPlane(screen)
    enemyList=[]
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
        n=random.randint(1,10)
        if n==10:
            enemy_plane=EnemyPlane(screen)
            enemyList.append(enemy_plane)
        for enemy in enemyList:
            enemy.display()
            enemy.isHitted(hero)
            if enemy.isValid==False or enemy.y>568:
                enemyList.remove(enemy)
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
        pygame.display.update()
        time.sleep(0.05)
    pygame.quit()
if __name__ == "__main__":
    main()