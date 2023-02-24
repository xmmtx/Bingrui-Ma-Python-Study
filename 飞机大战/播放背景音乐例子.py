import pygame
pygame.init()
screen = pygame.display.set_mode((512,568)) 
background = pygame.image.load("./images/bg2.jpg")
plane=pygame.image.load("./images/me.png")
pygame.mixer.init()
pygame.mixer.music.load("./music/PlaneWarsBackgroundMusic.mp3") 
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(background,(0,0))
    screen.blit(plane,(100,200))
    screen.blit(plane,(300,100))
    if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
    pygame.display.update()
pygame.quit()