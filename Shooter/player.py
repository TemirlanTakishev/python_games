import pygame
from pygame.math import Vector2

snd_dir = 'media/snd/'  # Путь до папки со звуками
img_dir = 'media/img/'  # Путь до папки со спрайтами
width = 1366                            # ширина игрового окна
height = 768                            # высота игрового окна

# Создаем класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):  # Специальная функция, где указываем что будет у игрока
        pygame.sprite.Sprite.__init__(self)  # Игрок - спрайт

        self.image = pygame.image.load(img_dir + 'player/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = width/2 - self.image.get_width()/2
        self.rect.y = height/2 - self.image.get_height()/2

        self.speed = 5
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0

        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl.mp3")
        self.snd_expl.set_volume(0.1)
        self.snd_shoot = pygame.mixer.Sound(snd_dir + "shoot.mp3")
        self.snd_shoot.set_volume(0.1)
        self.snd_scratch = pygame.mixer.Sound(snd_dir + "scratch.mp3")
        self.snd_scratch.set_volume(0.1)

        self.hp = 500

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)       # Изменяем направление взгляда
        self.angle += rotate_speed                    # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)     # Изменение рамки

    def update(self):

        keystate = pygame.key.get_pressed()     # Сохраняем нажатие на кнопку (любую)
        if keystate[pygame.K_RIGHT]:            # Если нажата кнопка стрелка вправо
            self.rotate(-5)                     # Вращаемся на 5 градусов по часовой стрелке
        if keystate[pygame.K_LEFT]:             # Если нажата кнопка стрелка влево
            self.rotate(5)                      # Вращаемся на 5 градусов против часовой стрелки
        if keystate[pygame.K_UP]:               # Если нажата кнопка стрелка вправо
            self.position += self.speed * self.direction          # Изменяем координату Х на 5
            self.rect.center = self.position
        if keystate[pygame.K_DOWN]:             # Если нажата кнопка стрелка влево
            self.position -= self.speed * self.direction          # Изменяем координату Х на -5
            self.rect.center = self.position

