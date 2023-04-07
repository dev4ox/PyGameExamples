import pygame

#Настройки окна
set_screen = (800, 800) #Разрешение экрана
bg_color = 'gray'


#Инициализация параметров
pygame.init() #Инициализация базового класса
screen = pygame.display.set_mode(set_screen) #Установка разршения для pygame
screen.fill(color=bg_color) #Цвет заднему фону
