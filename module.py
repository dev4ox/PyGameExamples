import pygame
import w_setting

#Рисуем прямоугольники через цикл
def draw_rect(start_pos=(0, 0), length_d_r=(50, 50), step_pos=(0, 0), num_repeat=1, color=(0, 0, 0)):
    pos = start_pos
    for i in range(num_repeat):
        if i == 0:
            pygame.draw.rect(w_setting.screen, color, (start_pos, length_d_r[0], length_d_r[1]))
            continue
        pos[0] += step_pos[0]
        pos[1] += step_pos[1]
        pygame.draw.rect(w_setting.screen, color, (pos[0], pos[1], length_d_r[0], length_d_r[1]))

#Рисуем окружности через цикл
def draw_circle(start_pos=(0, 0), radius=50, step_pos=(0, 0), num_repeat=1, color=(0, 0, 0)):
    pos = start_pos
    for i in range(num_repeat):
        if i == 0:
            pygame.draw.circle(w_setting.screen, color, start_pos, radius)
            continue
        pos[0] += step_pos[0]
        pos[1] += step_pos[1]
        pygame.draw.circle(w_setting.screen, color, (pos[0], pos[1]), radius)

#Рисуем многоугольники через цикл (Surface, color, pointlist, width=0)
def draw_polygon():
    pass



#Шахматная доска
def cheess_plate(num_rect=4, num_row=8):
    y_start_pos = 0         #Изменяемая позиция по вертикали (ось Y)
    # right_repeat = 4      #Количество черных квадратов по диагонали (ось X)
    for i in range(num_row):
        if i == 0:
            draw_rect([0, y_start_pos], [100, 100], [200, 0], num_rect)
            continue
        y_start_pos += 100

        if i % 2 == 0:
            draw_rect([0, y_start_pos], [100, 100], [200, 0], num_rect)
        else:
            draw_rect([100, y_start_pos], [100, 100], [200, 0], num_rect)
            
class Figure_checker:
    def __init__(self, pos=(0, 0), size=80, color='white'):
        """

        :type color: object
        """
        self.center = pos[0] + (100 - size) // 2 + (size // 2), pos[1] + (100 - size) // 2 + size // 2
        self.radius = size // 2
        self.color = color


    def draw(self):
        pass
        # if self.color == 'white':
        #     pygame.draw.circle(w_setting.screen, (color[0], color[1], color[2]), center, radius)
        #     pygame.draw.circle(w_setting.screen, (color[0], color[1], color[2]), center, radius)
        #     pygame.draw.circle(w_setting.screen, (color[0], color[1], color[2]), center, radius)
        #     pygame.draw.circle(w_setting.screen, (color[0], color[1], color[2]), center, radius)
        # elif self.color == 'black':
        #     pass
        # else:
        #     pass