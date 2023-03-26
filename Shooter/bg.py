import pygame
from pygame.math import Vector2

snd_dir = 'media/snd/'            # Путь до папки со звуками
img_dir = 'media/img/' 
width = 1366
height = 768

class Bg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_dir + 'bg.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = [width/2,height/2]
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0,-1)
        self.angle = 0
    def rotate(self,rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed
        self.image = pygame.transform.rotate(self.copy,self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    def update(self):
        self.rotate(-0.07)