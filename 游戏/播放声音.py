import pygame
pygame.init()
screen=pygame.display.set_mode([640,500])
pop=pygame.mixer.Sound('D:\\ball\\pop2.wav')
blap=pygame.mixer.Sound('D:\\ball\\blap.wav')
dzj=pygame.mixer.Sound('D:\\ball\\打字机.wav')
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                pop.play()
            elif event.key==pygame.K_d:
                blap.play()
            elif event.key==pygame.K_w:
                dzj.play()
    pygame.display.update()
pygame.quit()