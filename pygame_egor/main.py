import pygame
from pygame.locals import *
import settings
import person
import pymunk.pygame_util

pygame.init()
clock = pygame.time.Clock()
pymunk.pygame_util.positive_y_is_up = False
options = pymunk.pygame_util.DrawOptions(settings.surface)

space = pymunk.Space()
space.gravity = 1, 500
space.add(person.create_location_1(space))

# Персонажи
steve = person.Men('steve', [400, 400], 0)
steve.speed = 5
fireman = person.Men('fireman', [100, 100], 1)
# segment1 = py


while True:
    settings.surface.fill(settings.bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    if keys[K_UP]:
        steve.walk(1)
    if keys[K_DOWN]:
        steve.walk(2)
    if keys[K_LEFT]:
        steve.walk(3)
    if keys[K_RIGHT]:
        steve.walk(4)
    if keys[K_0]:
        space = pymunk.Space()
        space.gravity = 1, 500
        space.add(person.create_location_1(space))
    if mouse[0]:
        circle = person.create_circle(mouse_pos)
        space.add(circle[0], circle[1])
    if mouse[2]:
        circle = person.create_circle(mouse_pos, 10, 50, 'red')
        space.add(circle[0], circle[1])

    space.step(1 / settings.FPS)
    space.debug_draw(options)

    fireman.draw()
    steve.draw()

    pygame.display.flip()
    clock.tick(settings.FPS)

