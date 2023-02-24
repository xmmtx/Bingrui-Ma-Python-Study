import pygame
import time
from pygame.locals import *
zjsd=100
djsd=4
import random
class HeroPlane:
    def __init__(self, screen_temp):
        self.bomb_picture_num=4
        self.image_index=0
        self.x = 200
        self.y = 400
        self.screen = screen_temp
        self.image = pygame.image.load("./images/me.png")
        self.bullet_list = []
        self.fireMusic=pygame.mixer.Sound("./music/hero_fire.wav")
        self.image_num=0
        self.image_picture_num=4
        self.hit=False
        self.isValid=True
        self.bomb_picture_list=[]
        for i in range(1,5):
            herolmg=pygame.image.load('./images/me_down'+str(i)+'.png')
            self.bomb_picture_list.append(herolmg)
        self.bomMusic=pygame.mixer.Sound('./music/bomb.wav')
        self.lives=5
    def display(self):
        for bullet in self.bullet_list:
            bullet.display()
            isOverBorder=bullet.move()
            if  isOverBorder:
                self.bullet_list.remove(bullet)
        if self.hit==True:
            print("image_index=",self.image_index)
            heroBomblmg=self.bomb_picture_list[self.image_index]
            
            self.screen.blit(heroBomblmg,(self.x,self.y))
            self.image_num+=1
            if self.image_num==7:
                self.image_num=0
                self.image_index+=1
            if self.image_index>self.bomb_picture_num-1:
                self.image_index=self.bomb_picture_num-1
                self.isValid=False
        else:
            self.screen.blit(self.image, (self.x, self.y))
    def move_left(self):
        self.x -=zjsd
        if self.x<0:
            self.x=0
    def move_right(self):
        self.x +=zjsd
        if self.x > 406:
            self.x = 406
    def move_up(self):
        self.y -=zjsd
        if self.y<0:
            self.y=0
    def move_down(self):
        self.y +=zjsd
        if self.y >568-76:
            self.y =568-76
    def fire(self):
        bullet=Bullet(self.screen, self.x, self.y)
        self.bullet_list.append(bullet)
        print(len(self.bullet_list))
        self.fireMusic.play()
    def isHitted(self,enemyPlaneList):
        width=self.image.get_width()
        height=self.image.get_height()
        for enemyPlane in enemyPlaneList:
            for bullet in enemyPlane.bullet_list:
                if bullet.x>self.x and bullet.x<self.x+width and bullet.y>self.y and bullet.y<self.y+height:
                    enemyPlane.bullet_list.remove(bullet)
                    self.hit=True
                    self.bomMusic.play()
    def startHero(self):
        self.x=200
        self.y=400
        self.bullet_list=[]
        self.image_num=0
        self.image_index=0
        self.hit=False
        self.isValid=True
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
class EnemyBullet:
    def __init__(self,screen_temp,x,y):
        self.x=x+49
        self.y=y+74
        self.screen=screen_temp
        self.image=pygame.image.load('./images/bullet.png')
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y+=10
        if self.y>568:
            return True
class EnemyPlane:
    def __init__(self, screen_temp):
        self.x=random.randint(0,512-114)
        self.y=-68
        self.screen = screen_temp
        m=random.randint(0,2)
        enemyName='e'+str(m)+'.png'
        self.image=pygame.image.load('images/'+enemyName)
        self.bomb=pygame.mixer.Sound("./music/bomb.wav")
        self.bullet_list=[]
        self.hit=False
        self.isValid=True
        self.image_index=0
        self.bomb_picture_num=11
        self.bomb_picture_list=[]
        for i in range(1,12):
            enlmg=pygame.image.load('./images/b'+str(i)+'.gif')
            enlmg=pygame.transform.scale(enlmg,(116,82))
            self.bomb_picture_list.append(enlmg)
    def display(self):
        self.move()
        if self.hit==True:
            bombpicture=self.bomb_picture_list[self.image_index]
            self.screen.blit(bombpicture,(self.x,self.y))
            self.image_index+=1
            if self.image_index>self.bomb_picture_num-1:
                self.image_index=self.bomb_picture_num-1
                self.isValid=False
        else:
            self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            if bullet.move():
                self.bullet_list.remove(bullet)
        self.fire()
        
    def move(self):
        self.y+=djsd
    def isHitted(self,plane):
        width=self.image.get_width()
        height=self.image.get_height()
        for bullet in plane.bullet_list:
            if bullet.x>=self.x and bullet.x<=self.x+width and bullet.y<=self.y+height:
                plane.bullet_list.remove(bullet)
                self.hit=True
                print('击中了敌机')
                self.bomb.play()
    def fire(self):
        random_num=random.randint(1,100)
        if random_num==8 or random_num==20:
            enemyBullet=EnemyBullet(self.screen,self.x,self.y)
            self.bullet_list.append(enemyBullet)
            print('敌机子弹数量',len(self.bomb_picture_list))
    def initEnemy(self):
        self.x=random.randint(0,512-114)
        self.y=-68
        self.hit=False
        self.isValid=True
        self.image_index=0
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
    enemy=EnemyPlane(screen)
    enemyList=[]
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                # exit()
                run=False
        m=m+2
        if m>=0:
            m=-968
        screen.blit(background,(0,m))
        key_control(hero)
        hero.display()
        hero.isHitted(enemyList)
        if hero.isValid==False:
            hero.lives-=1
            if hero.lives>0:
                hero.startHero()
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