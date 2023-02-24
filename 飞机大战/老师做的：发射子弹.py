import pygame
import time
from pygame.locals import *  #pygame使用的各种常量
class HeroPlane:
    #把控制键盘的代码封装成函数，
    def __init__(self, screen_temp):
        self.x = 200  #x,y,用于显示飞机的坐标
        self.y = 400
        self.screen = screen_temp #screen保存到
        self.image = pygame.image.load("./images/me.png")  #设置飞机的显示图片

        self.bullet_list = [] #用一个列表存储发射出去的子弹
         #设置开火的声音文件
        self.fireMusic=pygame.mixer.Sound("./music/hero_fire.wav")
 
    def display(self): 
        #''' 绘制玩家到窗口中，进行绘制飞机和飞机存放的子弹 '''

        #遍历移动子弹，即显示飞机发射的子弹，列表bullet_list存放的子弹
        for bullet in self.bullet_list: #循环变量子弹，显示子弹，
            bullet.display()  #显示子弹
            #移动子弹，越过边界返回True,否则返回False
            isOverBorder=bullet.move()
            if  isOverBorder:#如果越界了，从子弹列表中删除子弹
                self.bullet_list.remove(bullet)

        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        #''' 左移动,并判断防止越界 '''
        self.x -= 5
        if self.x<0:
            self.x=0

    def move_right(self):
        #''' 右移动,并判断防止越界 '''
        self.x += 5
        if self.x > 406:
            self.x = 406
    def move_up(self):
        #''' 上移动,并判断防止越界 '''
        self.y -= 5
        if self.y<100:
            self.y=100

    def move_down(self):
        #''' 下移动,并判断防止越界 '''
        self.y += 5
        if self.y > 450:
            self.y = 450

    #下面fire方法，用于存放子弹
    def fire(self):
        #创建一个子弹对象
        bullet=Bullet(self.screen, self.x, self.y)
        #将子弹存放到列表中
        self.bullet_list.append(bullet)
        print(len(self.bullet_list)) #测试打印输出子弹的个数
        self.fireMusic.play()  #开火时发出开火声音
    
#定义子弹类
class Bullet:
    ''' 玩家子弹类,x,y是飞机显示的坐标 '''
    def __init__(self, screen_temp, x, y):
        self.x = x+51 #子弹在飞机的正中间
        self.y = y
        self.screen = screen_temp
        #设置子弹图片
        self.image = pygame.image.load("./images/pd.png")
    #显示子弹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 10 #子弹往上运动
        if self.y<-20: #如果子弹越过了窗口的上边界
            return True 
        else:
            return False

def key_control(hero_temp):
    ''' 键盘控制函数 '''
    #获取按下的键(返回的是元组值)
    pressed_keys = pygame.key.get_pressed()
    #检测是否按下a或者left键
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        # x=x-5
        hero_temp.move_left()
        print('left')    
    #检测是否按下d或者right键
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        # x=x+5
        hero_temp.move_right()
        print('right')
    #检测是否按下x或者down键
    elif pressed_keys[K_x] or pressed_keys[K_DOWN]:
        # y=y+5
        hero_temp.move_down()
        print('down')
    ##检测是否按下w或者up键
    elif pressed_keys[K_UP] or pressed_keys[K_w]:
        # y=y-5
        hero_temp.move_up()
        print('up')
                
    #检查是否是空格键
    if pressed_keys[K_SPACE]:
        print('space')
        hero_temp.fire()

def main():
    pygame.init() #pygame初始化
    #1. 创建窗口:set_mode(宽和高分别是512像素和568像素)
    screen = pygame.display.set_mode((512,568)) 
    #2. 创建一个游戏背景图片(512*1536),background是一个变量名，中文含义是背景
    background = pygame.image.load("./images/bg2.jpg") #background可以取其他变量名

    #下面两行代码用于播放背景音乐做准备 
    pygame.mixer.init() #必须有该行代码，否则下面一行代码会报错
    #加载要播放的音乐，如果要更换播放的音乐，下面load后小括号中变换音乐文件，
    pygame.mixer.music.load("./music/PlaneWarsBackgroundMusic.mp3") 

    m=-(1536-568)  

    hero=HeroPlane(screen) 
    while True:
        for event in pygame.event.get():   #pygame.event.get()获取事件列表 
            if event.type==pygame.QUIT: #type：
                exit()
        m=m+2
        if m>=0: #如果背景图片恰好移动到窗口上边界，让背景重新显示在上方
            m=-968
        screen.blit(background,(0,m)) #在窗口的左上角位置显示背景，左上角坐标(0,m)
        
        # 调用键盘函数控制飞机运动
        key_control(hero)  #hero是实际参数，说明用键盘控制hero这个飞机对象
    
        hero.display() #显示飞机

        #播放背景音乐，如果没有播放音乐，pygame.mixer.music.get_busy() 的值是假的，否则就是真的 
        if pygame.mixer.music.get_busy() == False:#没有播放音乐，
            pygame.mixer.music.play() #重新播放

        pygame.display.update()
        time.sleep(0.05) #程序暂停执行，休息0.05秒
    pygame.quit()  #pygame退出，即关闭窗口
if __name__ == "__main__":
    main()