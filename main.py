import pygame       #Библиотека для использования графических изображений и триггеров
import sys          #Системная библиотека, позволяет выйти без ошибок
import module       #Готовые модули
# import example      #Примеры использования для разрешения экрана 800x800

if __name__ == "__main__":
    #Здесь можно вызывать функции
    module.cheess_plate()

    w_ch_1 = module.Figure_checker('white', (0, 600), 90)
    w_ch_2 = module.Figure_checker('white', (100, 500), 90)
    w_ch_3 = module.Figure_checker('white', (100, 700), 90)
    w_ch_4 = module.Figure_checker('white', (200, 600), 90)
    w_ch_5 = module.Figure_checker('white', (300, 500), 90)
    w_ch_6 = module.Figure_checker('white', (300, 700), 90)
    w_ch_7 = module.Figure_checker('white', (400, 600), 90)
    w_ch_8 = module.Figure_checker('white', (500, 500), 90)
    w_ch_9 = module.Figure_checker('white', (500, 700), 90)
    w_ch_10 = module.Figure_checker('white', (600, 600), 90)
    w_ch_11 = module.Figure_checker('white', (700, 500), 90)
    w_ch_12 = module.Figure_checker('white', (700, 700), 90)
    w_checkers = [w_ch_1, w_ch_2, w_ch_3, w_ch_4, w_ch_5, w_ch_6,
                  w_ch_7, w_ch_8, w_ch_9, w_ch_10, w_ch_11, w_ch_12]
    b_ch_1 = module.Figure_checker('black', (0, 0), 90)
    b_ch_2 = module.Figure_checker('black', (0, 200), 90)
    b_ch_3 = module.Figure_checker('black', (100, 100), 90)
    b_ch_4 = module.Figure_checker('black', (200, 0), 90)
    b_ch_5 = module.Figure_checker('black', (200, 200), 90)
    b_ch_6 = module.Figure_checker('black', (300, 100), 90)
    b_ch_7 = module.Figure_checker('black', (400, 0), 90)
    b_ch_8 = module.Figure_checker('black', (400, 200), 90)
    b_ch_9 = module.Figure_checker('black', (500, 100), 90)
    b_ch_10 = module.Figure_checker('black', (600, 0), 90)
    b_ch_11 = module.Figure_checker('black', (600, 200), 90)
    b_ch_12 = module.Figure_checker('black', (700, 100), 90)
    b_checkers = [b_ch_1, b_ch_2, b_ch_3, b_ch_4, b_ch_5, b_ch_6,
                  b_ch_7, b_ch_8, b_ch_9, b_ch_10, b_ch_11, b_ch_12]

    for w_ch in w_checkers:
        w_ch.draw()
    for b_ch in b_checkers:
        b_ch.draw()


    # Инициализация графического интерфейса
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

