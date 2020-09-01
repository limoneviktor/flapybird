import pygame
from config import *

class Tube:
    #конструкто класса
    def __init__(self,x,y):
        self.image = pygame.image.load('tube2.png')
        #self.image = pygame.Surface((100,100))
        #self.image.fill((247, 241, 121))
        self.rect = self.image.get_rect(x = x,y = y)
        self.speedx = 5
        #self.grav = 0

    def update(self,bird):
        #self.speedy += self.grav
        self.rect.centerx-=self.speedx
        if self.rect.right<0:
            self.rect.left=W
            bird.how_many_tubes+=1
            print(bird.how_many_tubes)
        if self.rect.colliderect(bird.rect):
            bird.image.fill((255,0,0))


