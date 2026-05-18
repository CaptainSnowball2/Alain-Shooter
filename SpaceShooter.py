import pygame
pygame.init()
HEIGHT=800
WIDTH=430
FPS = 60
screen= pygame.display.set_mode((WIDTH,HEIGHT))
Shooter=pygame.image.load("space shooter/images/SpaceShip.png")
Alian=pygame.image.load("space shooter/images/AlainShooter2.png")
Space=pygame.image.load("space shooter/images/space.png")
font1=pygame.font.SysFont("segoeuiemoji",30)
S=pygame.Rect(215,700,60,61)
while True:
    screen.blit(Space,(0,0))
    screen.blit(Alian,(215,100))
    screen.blit(Shooter,S)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()