import pygame       #Библиотека для использования графических изображений и триггеров
import sys          #Системная библиотека, позволяет выйти без ошибок
import module       #Готовые модули
# import example      #Примеры использования для разрешения экрана 800x800

if __name__ == "__main__":
    #Здесь можно вызывать функции
    module.cheess_plate()


    # module.draw_circle([150, 50], 50, [200, 0], 4, [200, 100, 0])
    # module.Figure_checker()


    # Инициализация графического интерфейса
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

