import pygame
import random
from pygame.math import Vector2

snd_dir = 'media/snd/'  # Путь до папки со звуками
img_dir = 'media/img/'  # Путь до папки со спрайтами
width = 1366                            # ширина игрового окна
height = 768                            # высота игрового окна

# Создаем класс игрока
class EnemyLeft(pygame.sprite.Sprite):
    def __init__(self):  # Специальная функция, где указываем что будет у игрока
        pygame.sprite.Sprite.__init__(self)  # Игрок - спрайт

        self.image = pygame.image.load(img_dir + 'enemy_left/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(0, height)
        self.speedx = random.randint(1, 5)
        self.speedy = random.randint(-5, 5)

        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0

        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl.mp3")
        self.hp = 100


    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)       # Изменяем направление взгляда
        self.angle += rotate_speed                    # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)     # Изменение рамки

    def update(self):
        self.rotate(5)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x > width or self.rect.y > height or self.rect.bottom < 0:
            self.rect.x = 0
            self.rect.y = random.randint(0, height)
            self.speedx = random.randint(1, 5)
            self.speedy = random.randint(-5, 5)
