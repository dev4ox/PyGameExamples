import pygame
import pygame as pg
import settings
from random import randint
import pymunk.pygame_util


class Men(pg.sprite.Sprite):
    def __init__(self, name: str, pos: list[int, int], team: int):
        pg.sprite.Sprite.__init__(self)
        self._name = name
        self._pos = pos
        self._team = team
        self.speed = 1



    def draw(self):
        path = f'texture/{self._name}/'
        body_dict = {'head': ['Head.png', (self._pos[0] - 20, self._pos[1] - 80)],
                     'body': ['Body.png', (self._pos[0] - 20, self._pos[1] - 40)],
                     'arml': ['ArmL.png', (self._pos[0] - 40, self._pos[1] - 40)],
                     'armr': ['ArmR.png', (self._pos[0] + 20, self._pos[1] - 40)],
                     'legl': ['LegL.png', (self._pos[0] - 20, self._pos[1] + 20)],
                     'legr': ['LegR.png', (self._pos[0], self._pos[1] + 20)]
                     }
        for i in body_dict.values():
            settings.surface.blit(pg.image.load(path + i[0]).convert_alpha(), i[1])

    def walk(self, arrow: int):
        if self._pos[0] < settings.WIDTH and self._pos[0] >= 0 and self._pos[1] < settings.HEIGHT and self._pos[1] >= 0:
            if arrow == 1:
                self._pos[1] -= self.speed
            elif arrow == 2:
                self._pos[1] += self.speed
            elif arrow == 3:
                self._pos[0] -= self.speed
            elif arrow == 4:
                self._pos[0] += self.speed
        else:
            self._pos[0] = randint(50, settings.SCREEN[1] - 100)
            self._pos[1] = randint(50, settings.SCREEN[1] - 100)


def create_circle(pos, mass: int = 1, size: int = 10, color: str = 'blue'):
    moment = pymunk.moment_for_circle(mass, 0, size)
    body = pymunk.Body(mass, moment)
    body.position = pos
    shape = pymunk.Circle(body, size)
    shape.elasticity = 0.8
    shape.friction = 1.0
    shape.color = pygame.Color(color)
    return body, shape

def create_location_1(space):
    segment = pymunk.Segment(space.static_body, (1, settings.HEIGHT), settings.SCREEN, 20)
    segment.friction = 1.0
    segment.elasticity = 0.1
    return segment


