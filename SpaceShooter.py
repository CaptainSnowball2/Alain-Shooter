import pygame
import random
pygame.init()
HEIGHT=800
WIDTH=430
FPS = 60
screen= pygame.display.set_mode((WIDTH,HEIGHT))
Shooter=pygame.image.load("space shooter/images/SpaceShip.png")
Alian=pygame.image.load("space shooter/images/AleinSpaceship.png")
Space=pygame.image.load("space shooter/images/space.png")
heart=pygame.image.load("space shooter/images/Heart.png")
font1=pygame.font.SysFont("segoeuiemoji",30)
S=pygame.Rect(200,700,60,61)
deadaliens=[]
def spawnA():
    x=random.randint(0,370)
    reckt=pygame.Rect(x,100,60,39)
    deadaliens.append(reckt)
def SS():
    if keys_pressed[pygame.K_a] and S.x>0:
        S.x-=3
    if keys_pressed[pygame.K_d] and S.x<370:
        S.x+=3
spawnAtimer=0
clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    screen.blit(Space,(0,0))
    spawnAtimer+=1
    if spawnAtimer>30:
        spawnA()
        spawnAtimer=0
    for a in deadaliens:
        a.y+=2
    for a in deadaliens:
        screen.blit(Alian,a)
    screen.blit(Shooter,S)
    screen.blit(heart,(0,0))
    screen.blit(heart,(80,0))
    screen.blit(heart,(160,0))
    keys_pressed = pygame.key.get_pressed()
    SS()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()