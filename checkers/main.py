import pygame       #Библиотека для использования графических изображений и триггеров
import sys          #Системная библиотека, позволяет выйти без ошибок
import module       #Готовые модули
import setting
# import example      #Примеры использования для разрешения экрана 800x800

if __name__ == "__main__":
    #Здесь можно вызывать функции
    w_ch_1 = module.Figure_checker('white', (50, 650), 90)
    w_ch_2 = module.Figure_checker('white', (150, 550), 90)
    w_ch_3 = module.Figure_checker('white', (150, 750), 90)
    w_ch_4 = module.Figure_checker('white', (250, 650), 90)
    w_ch_5 = module.Figure_checker('white', (350, 550), 90)
    w_ch_6 = module.Figure_checker('white', (350, 750), 90)
    w_ch_7 = module.Figure_checker('white', (450, 650), 90)
    w_ch_8 = module.Figure_checker('white', (550, 550), 90)
    w_ch_9 = module.Figure_checker('white', (550, 750), 90)
    w_ch_10 = module.Figure_checker('white', (650, 650), 90)
    w_ch_11 = module.Figure_checker('white', (750, 550), 90)
    w_ch_12 = module.Figure_checker('white', (750, 750), 90)
    b_ch_1 = module.Figure_checker('black', (50, 50), 90)
    b_ch_2 = module.Figure_checker('black', (50, 250), 90)
    b_ch_3 = module.Figure_checker('black', (150, 150), 90)
    b_ch_4 = module.Figure_checker('black', (250, 50), 90)
    b_ch_5 = module.Figure_checker('black', (250, 250), 90)
    b_ch_6 = module.Figure_checker('black', (350, 150), 90)
    b_ch_7 = module.Figure_checker('black', (450, 50), 90)
    b_ch_8 = module.Figure_checker('black', (450, 250), 90)
    b_ch_9 = module.Figure_checker('black', (550, 150), 90)
    b_ch_10 = module.Figure_checker('black', (650, 50), 90)
    b_ch_11 = module.Figure_checker('black', (650, 250), 90)
    b_ch_12 = module.Figure_checker('black', (750, 150), 90)
    checker_list = [w_ch_1, w_ch_2, w_ch_3, w_ch_4, w_ch_5, w_ch_6, w_ch_7, w_ch_8, w_ch_9, w_ch_10, w_ch_11, w_ch_12,
                    b_ch_1, b_ch_2, b_ch_3, b_ch_4, b_ch_5, b_ch_6, b_ch_7, b_ch_8, b_ch_9, b_ch_10, b_ch_11, b_ch_12]


    # Инициализация графического интерфейса
    while True:
        setting.screen.fill(setting.bg_color)
        module.draw_plate()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

        module.out_checkers(checker_list)
        pygame.display.flip()


