import random
import pygame
 
def draw_text(screen,text,size,x,y,color):         # Функция для текста на экране
   font_name = pygame.font.match_font('arial')     # Выбираем тип шрифта для текста
   font = pygame.font.Font(font_name, size)        # Шрифт выбранного типа и размера
   text_image = font.render(text, True, color)     # Превращаем текст в картинку
   text_rect = text_image.get_rect()               # Задаем рамку картинки с текстом
   text_rect.center = (x,y)                        # Переносим текст в координаты
   screen.blit(text_image, text_rect)              # Рисуем текст на экране
 
pygame.init()                           # Инициализируем модуль pygame
 
width = 1200                            # ширина игрового окна
height = 700                            # высота игрового окна
fps = 30                                # частота кадров в секунду
game_name = "Ping Pong"                  # название нашей игры
 
# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"
YELLOW = "#FFFF00"
 
#Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)   # Заголовок окна
 
icon = pygame.image.load('Desktop/python_game/ping pong/materials/icon.png')    # Загружаем файл с иконкой
pygame.display.set_icon(icon)           # Устанавливаем иконку в окно
 
timer = pygame.time.Clock()             # Создаем таймер pygame
run = True
 
pic = pygame.image.load('Desktop/python_game/ping pong/materials/Enderpearl.webp')             # Загружаем спрайт
pic = pygame.transform.scale(pic, (100,100))     # Указываем размеры
pic_rect = pic.get_rect()                        # Получаем рамку спрайта
 
bg = pygame.image.load('Desktop/python_game/ping pong/materials/minecraft.jpg')      # Загружаем задний фон
bg_rect = bg.get_rect()               # Получаем рамку фона
 
speedx = 10
speedy = 10
lives = 3
lives2 = 3
 
racket = pygame.image.load('Desktop/python_game/ping pong/materials/racket.png')  # Загружаем спрайт игрока
racket_rect = racket.get_rect()           # Получаем рамку спрайта игрока
racket_rect.x = width / 2 - racket.get_width()/2
racket_rect.y = height - 50

racket2 = pygame.image.load('Desktop/python_game/ping pong/materials/racket.png')  # Загружаем спрайт игрока
racket_rect2 = racket.get_rect()           # Получаем рамку спрайта игрока
racket_rect2.x = width / 2 - racket.get_width()/2
racket_rect2.y = height - 650
 
ping = pygame.mixer.Sound('Desktop/python_game/ping pong/materials/ping.mp3')    # Звук отскока
loose = pygame.mixer.Sound('Desktop/python_game/ping pong/materials/loose.mp3')  # Звук проигрыша
 
pygame.mixer.music.load('Desktop/python_game/ping pong/materials/8-bit.mp3')     # Загружаем музыку
pygame.mixer.music.set_volume(0.1)      # Громкость 10%
pygame.mixer.music.play(-1)             # Бесконечный повтор
 
while run:                              # Начинаем бесконечный цикл
   timer.tick(fps)                      # Контроль времени (обновление игры)
   for event in pygame.event.get():     # Обработка ввода (события)
      if event.type == pygame.QUIT:    # Проверить закрытие окна
          run = False                  # Завершаем игровой цикл
   key = pygame.key.get_pressed()  # Считываем нажатия на клавиши
   if key[pygame.K_LEFT] and racket_rect.left > 0:   # Движение влево
       racket_rect.x -=15
   if key[pygame.K_RIGHT] and racket_rect.right < width:  # Движение вправо
       racket_rect.x +=15
   if key[pygame.K_a] and racket_rect2.left > 0:   # Движение влево
       racket_rect2.x -=15
   if key[pygame.K_d] and racket_rect2.right < width:  # Движение вправо
       racket_rect2.x +=15
   # Рендеринг (прорисовка)
   # screen.fill(CYAN)                     # Заливка заднего фона (больше не нужна)
   screen.blit(bg,bg_rect)               # Отрисовываем картинку для заднего фона
 
   screen.blit(pic, pic_rect)            # Отрисовываем смайлик
   screen.blit(racket, racket_rect)      # Отрисовываем ракетку
   screen.blit(racket2, racket_rect2)
   draw_text(screen, "Lives: " + str(lives), 30, width//2, 670, YELLOW) # текст
   draw_text(screen, "Lives: " + str(lives2), 30, width//2, 30, YELLOW)
 
   pic_rect.x += speedx
   pic_rect.y += speedy
 
   bg_rect.x -= 2                       # Фон плывет влево
   if bg_rect.x <= -width:              # Если дошли до середины
       bg_rect.x = 0                    # Вовзращаем фон
 
   if pic_rect.top > height:                   # Если зашли за нижнюю границу экрана
       lives -= 1                              # Уменьшаем количество жизней на 1
       loose.play()                            # Звук проигрыша
       pic_rect.y = 350                          # Поднимаем смайлик вверх
       pic_rect.x = random.randint(10, width-10)   # Случайное по горизонтали
       if lives == 0:
           run = False                                 # Завершаем игровой цикл
           print('Game Over')
           print(f'player1 wins')                          # Выводим надпись на экран
   if pic_rect.right > width or pic_rect.left < 0:     # Если прав или лев граница
       speedx = -speedx
       ping.play()
   if pic_rect.top < 0:  # Если достигли верха экрана
       lives2 -= 1                              # Уменьшаем количество жизней на 1
       loose.play()                            # Звук проигрыша
       pic_rect.y = 350                         # Поднимаем смайлик вверх
       pic_rect.x = random.randint(10, width-10)
       if lives2 == 0:
           run = False                                 # Завершаем игровой цикл
           print('Game Over')
           print('player2 wins')  
 
 
 
   # Если столкнулись с ракеткой         и      смайлик выше ракетки
   if pic_rect.colliderect(racket_rect) and pic_rect.bottom < racket_rect.bottom:
       speedy = -speedy
       ping.play()
   if pic_rect.colliderect(racket_rect2) and pic_rect.top < racket_rect2.top:
       speedy = -speedy
       ping.play()
       
   pygame.display.update()