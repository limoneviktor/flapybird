import pygame

class Bird:
    #конструкто класса
    def __init__(self):
        self.image = pygame.image.load('bird1.png')
        #self.image = pygame.Surface((100,100))
        #self.image.fill((247, 241, 121))
        self.rect = self.image.get_rect(x = 100,y = 299)
        self.speedy = 0
        self.grav = 1
        self.how_many_tubes = 0

    def update(self):
        self.speedy += self.grav
        self.rect.centery+=self.speedy
        #if self.rect.left>W:
         #   self.rect.right=0
    def jump(self):
        self.speedy -= 36.6
