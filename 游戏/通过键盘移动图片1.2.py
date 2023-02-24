import pygame
pygame.init()
screen=pygame.display.set_mode([640,500])
pic=pygame.image.load("d:\\ball\\CrazySmile.bmp")
x=100
y=200
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if y<=0:
                    y=0
                    print('图片到顶了！')
                else:
                    y=y-10
            if event.key==pygame.K_DOWN:
                if y>=400:
                    y=400
                    print('图片到底了！')
                else:
                    y=y+10
            if event.key==pygame.K_LEFT:
                if x<=0:
                    x=0
                    print('图片到边了！')
                else:
                    x=x-10
            if event.key==pygame.K_RIGHT:
                if x>=540:
                    x=540
                    print('图片到边了！')
                else:
                    x=x+10
            if event.key==pygame.K_a:
                if x<=0:
                    x=0
                    print('图片到边了！')
                else:
                    x=x-10
            if event.key==pygame.K_b:
                print('按下了B键……')
            if event.key==pygame.K_c:
                print('按下了C键……')
            if event.key==pygame.K_d:
                if x>=540:
                    x=540
                    print('图片到边了！')
                else:
                    x=x+10
            if event.key==pygame.K_e:
                print('按下了E键……')
            if event.key==pygame.K_f:
                print('按下了F键……')
            if event.key==pygame.K_g:
                print('按下了G键……')
            if event.key==pygame.K_h:
                print('按下了H键……')
            if event.key==pygame.K_i:
                print('按下了I键……')
            if event.key==pygame.K_j:
                print('按下了J键……')
            if event.key==pygame.K_k:
                print('按下了K键……')
            if event.key==pygame.K_l:
                print('按下了L键……')
            if event.key==pygame.K_m:
                print('按下了M键……')
            if event.key==pygame.K_n:
                print('按下了N键……')
            if event.key==pygame.K_o:
                print('按下了O键……')
            if event.key==pygame.K_p:
                print('按下了P键……')
            if event.key==pygame.K_q:
                print('按下了Q键……')
            if event.key==pygame.K_r:
                print('按下了R键……')
            if event.key==pygame.K_s:
                if y>=400:
                    y=400
                    print('图片到底了！')
                else:
                    y=y+10
            if event.key==pygame.K_t:
                print('按下了T键……')
            if event.key==pygame.K_u:
                print('按下了U键……')
            if event.key==pygame.K_v:
                print('按下了V键……')
            if event.key==pygame.K_w:
                if y<=0:
                    y=0
                    print('图片到顶了！')
                else:
                    y=y-10
            if event.key==pygame.K_x:
                print('按下了X键……')
            if event.key==pygame.K_y:
                print('按下了Y键……')
            if event.key==pygame.K_z:
                print('按下了Z键……')
            print('图片的坐标位置是：（',x,'，',y,'）。',sep='')
    screen.blit(pic,(x,y))
    pygame.display.update()
pygame.quit()