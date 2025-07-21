from circleshape import *
from constants import *
import pygame

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.add(*Shot.containers)
        
    def update(self,dt):
        self.position += self.velocity * dt
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)