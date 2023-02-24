import pygame
pygame.init()
screen=pygame.display.set_mode([640,500])
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                print('向上，按了上键……')
            if event.key==pygame.K_DOWN:
                print('向下，按了下键……')
            if event.key==pygame.K_LEFT:
                print('向左，按了左键……')
            if event.key==pygame.K_RIGHT:
                print('向右，按了右键……')
            if event.key==pygame.K_a:
                print('按下了A键……')
            if event.key==pygame.K_b:
                print('按下了B键……')
            if event.key==pygame.K_c:
                print('按下了C键……')
            if event.key==pygame.K_d:
                print('按下了D键……')
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
                print('按下了S键……')
            if event.key==pygame.K_t:
                print('按下了T键……')
            if event.key==pygame.K_u:
                print('按下了U键……')
            if event.key==pygame.K_v:
                print('按下了V键……')
            if event.key==pygame.K_w:
                print('按下了W键……')
            if event.key==pygame.K_x:
                print('按下了X键……')
            if event.key==pygame.K_y:
                print('按下了Y键……')
            if event.key==pygame.K_z:
                print('按下了Z键……')
pygame.quit()