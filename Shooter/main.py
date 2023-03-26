import pygame
from player import Player               # Из файла player подключаем класс Player
from bullet import Bullet
from explosion import Explosion
from enemy_left import EnemyLeft
from enemy_right import EnemyRight
from enemy_top import EnemyTop
from enemy_bottom import EnemyBottom
from bg import Bg
pygame.init()                           # Инициализируем модуль pygame

width = 1366                            # ширина игрового окна
height = 768                            # высота игрового окна
fps = 30                                # частота кадров в секунду
game_name = "Shooter"                   # название нашей игры

def get_hit_sprite(hits_dict):
    for hit in hits_dict.values():
        return hit[0]

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"

all_sprites = pygame.sprite.Group()    # Создаем группу для всех спрайтов
mobs_sprites = pygame.sprite.Group()   # Создаем группу для спрайтов мобов
bullets_sprites = pygame.sprite.Group()   # Создаем группу для спрайтов пуль
players_sprites = pygame.sprite.Group()   # Создаем группу для спрайтов игроков

snd_dir = 'media/snd/'            # Путь до папки со звуками
img_dir = 'media/img/'            # Путь до папки со спрайтами

icon = pygame.image.load(img_dir + 'icon.png')         # Загружаем файл с иконкой
pygame.display.set_icon(icon)                # Устанавливаем иконку в окно

#Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)   # Заголовок окна


player = Player()                       # Создаем игрока класса Player
enemy_left = EnemyLeft()
enemy_right = EnemyRight()
enemy_top = EnemyTop()
enemy_bottom = EnemyBottom()
bg = Bg()


all_sprites.add(player)                 # Добавляем игрока в группу спрайтов
players_sprites.add(player)             # Добавляем игрока в группу игроков
all_sprites.add([enemy_left, enemy_right, enemy_top, enemy_bottom])
mobs_sprites.add([enemy_left, enemy_right, enemy_top, enemy_bottom])
all_sprites.add(bg)

timer = pygame.time.Clock()             # Создаем таймер pygame
run = True

level = 1

pygame.mixer.music.load(snd_dir + "music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

def draw_text(screen,text,size,x,y,color):
    font_name= pygame.font.match_font('arial')
    font = pygame.font.Font(font_name,size)
    text_image = font.render(text,True,color)
    text_rect = text_image.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_image,text_rect)

def draw_hp(screen, x, y, hp, hp_width, hp_height):
    color = '#32CD32'
    white = '#FFFFFF'
    rect = pygame.Rect(x, y, hp_width, hp_height)
    fill = (hp / player.hp) * hp_width
    fill_rect = pygame.Rect(x, y, fill, hp_height)


    pygame.draw.rect(screen, color, fill_rect)
    pygame.draw.rect(screen, white, rect, 1)

def new_mobs(count):
    for i in range(count):
        el = EnemyLeft()
        er = EnemyRight()
        et = EnemyTop()
        eb = EnemyBottom()
        all_sprites.add([el,er,et,eb])
        mobs_sprites.add([el,er,et,eb])

def menu():
    screen.blit(bg.image,bg.rect)
    draw_text(screen,game_name,128,width/2,height/4,WHITE)
    draw_text(screen,'Arrows for move, space - fire',44,width/2,height/2,WHITE)
    draw_text(screen,'Press any key to start',36,width/2,height*3/4,WHITE)
    pygame.display.flip()
    run = True
    while run:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                run = False
game_over = True
while run:  
    if game_over:
        level = 1
        player.__init__()
        for sprite in mobs_sprites:
            sprite.kill()
        new_mobs(level)
        game_over = False
        menu()
    timer.tick(fps)			            # Контроль времени (обновление игры)
    all_sprites.update()                 # Выполняем действия всех спрайтов в группе
    for event in pygame.event.get():     # Обработка ввода (события)
        if event.type == pygame.QUIT:    # Проверить закрытие окна
            run = False                  # Завершаем игровой цикл
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.snd_shoot.play()
                bullet = Bullet(player)     # Создаем пулю передавая внутрь информацию об игроке
                all_sprites.add(bullet)     # Добавляем пулю ко всем спрайтам
                bullets_sprites.add(bullet) # Добавляем пулю ко всем пулям

    shots = pygame.sprite.groupcollide(bullets_sprites, mobs_sprites, True, False)

    if shots:
        sprite = get_hit_sprite(shots)  # Получаем спрайт из второй группы
        sprite.hp -= 30

        if sprite.hp <= 0:    
            sprite.snd_expl.play()  # Воспроизводим звук скрежета
            expl = Explosion(sprite.rect.center)
            all_sprites.add(expl)
            sprite.kill()
    if len(mobs_sprites) == 0:
        level += 1
        new_mobs(level)

    scratch = pygame.sprite.groupcollide(mobs_sprites, players_sprites, False, False)
    if scratch:
        sprite = get_hit_sprite(scratch)
        sprite.snd_scratch.play()
        player.hp -=1
        if player.hp <=0:
            game_over = True
    # Рендеринг (прорисовка)
    screen.fill(CYAN)                     # Заливка заднего фона
    all_sprites.draw(screen)
    draw_hp(screen,50, 50, player.hp, 200, 20)                                   # Отрисовываем все спрайты
    pygame.display.update()               # Обновляем экран

pygame.quit()