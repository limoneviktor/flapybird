import pygame
import Bird
import tube1
from config import *

pygame.init()
gamedisplay = pygame.display.set_mode((W,H),pygame.FULLSCREEN)
clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load('background.jpg')

bird = Bird.Bird()
tube = tube1.Tube(1400,-20)
tube2 = tube1.Tube(1100,760)
tube3 = tube1.Tube(809,-25)
tube4 = tube1.Tube(669,790)

game = True
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
            if event.key == pygame.K_SPACE:
                bird.jump()

    gamedisplay.blit(background,(0,0))
    gamedisplay.blit(bird.image,bird.rect)
    gamedisplay.blit(tube.image,tube.rect)
    gamedisplay.blit(tube2.image,tube2.rect)
    gamedisplay.blit(tube3.image, tube3.rect)
    gamedisplay.blit(tube4.image, tube4.rect)
    pygame.display.update()
    tube.update(bird)
    tube2.update(bird)
    tube3.update(bird)
    tube4.update(bird)
    bird.update()