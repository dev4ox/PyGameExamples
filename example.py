# import w_setting
# import module
import time
import pygame
from pygame.locals import *
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна игры
WIDTH = 800
HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKYBLUE = (0, 150, 250)
LIGHTORANGE = (255, 223, 196)
BARDO = (200, 60, 0)

# Создание окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя первая игра на Pygame")


# Функция для рисования персонажа
def draw_character(x, y):
    # Голова
    pygame.draw.circle(screen, LIGHTORANGE, (x, y), 20)
    # Глаза
    pygame.draw.ellipse(screen, WHITE, (x - 11, y - 4, 8, 6))
    pygame.draw.rect(screen, BLACK, (x - 7, y - 2, 2, 2))

    pygame.draw.ellipse(screen, WHITE, (x + 3, y - 4, 8, 6))
    pygame.draw.rect(screen, BLACK, (x + 7, y - 2, 2, 2))
    # Руки
    pygame.draw.rect(screen, BARDO, (x - 35, y + 20, 68, 18))
    # Ноги
    pygame.draw.rect(screen, SKYBLUE, (x - 20, y + 80, 10, 60))
    pygame.draw.rect(screen, SKYBLUE, (x + 10, y + 80, 10, 60))
    # Тело
    pygame.draw.rect(screen, BLACK, (x - 20, y + 20, 40, 60))
    # pygame.draw.circle(screen, BLACK, (x, y), 1)
    # pygame.draw.rect(screen, BLACK, )


#Начальные координаты персонажа
character_x = 400
character_y = 300

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        character_x -= 0.1
    if keys[K_RIGHT]:
        character_x += 0.1
    if keys[K_UP]:
        character_y -= 0.1
    if keys[K_DOWN]:
        character_y += 0.1
    print(keys)
    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка персонажа с использованием функции draw_character
    draw_character(character_x, character_y)

    # Обновление экрана
    pygame.display.update()
