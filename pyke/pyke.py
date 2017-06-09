import time
import pygame

import item
import settings
import snake

FOR_EVER_AND_EVER = True


def update_snake_display(body):
    pygame.draw.rect(screen,
                     0xFFFF00,
                     (body[-1][0] * settings.CELL_SIZE, body[-1][1] * settings.CELL_SIZE,
                     settings.CELL_SIZE, settings.CELL_SIZE),
                     0)
    pygame.draw.rect(screen,
                     0x0,
                     (body[0][0] * settings.CELL_SIZE, body[0][1] * settings.CELL_SIZE,
                     settings.CELL_SIZE, settings.CELL_SIZE),
                     0)
    pygame.display.update()



def draw_snake(body):
    for body_part in body:
        pygame.draw.rect(screen,
                         0xFFFF00,
                         (body_part[0] * settings.CELL_SIZE, body_part[1] * settings.CELL_SIZE,
                          settings.CELL_SIZE, settings.CELL_SIZE),
                          0)
    pygame.display.update()


def draw_points(points):
    for point in points:
        pygame.draw.rect(screen,
                         0xFFFFFF,
                         (point[0] * settings.CELL_SIZE, point[1] * settings.CELL_SIZE,
                         settings.CELL_SIZE, settings.CELL_SIZE),
                         0)

def add_points_to_map(map, points):
    for point in points:
        map[point[1]][point[0]] = 1


def main():

    fruit = item.Item((5, 12), (settings.CELLS_X, settings.CELLS_Y), intensity=10)

    tmp = [0 for i in range(settings.CELLS_X)]
    map = [list(tmp) for i in range(settings.CELLS_Y)]
    
    ia = snake.Snake(int(settings.CELLS_X / 2), int(settings.CELLS_Y / 2))
    


    #draw_points(points)
    
    draw_snake(ia.body)



    #for i in range(int(settings.CELLS_X / 2) + 1, int(settings.CELLS_X), 1):

    while FOR_EVER_AND_EVER:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #ia.move(i, int(settings.CELLS_Y / 2))
        ia.smell(map)
        ia.auto_move()
        update_snake_display(ia.body)
        ia._cut_tail()

        time.sleep(0.5)


if __name__ == "__main__":
    #pygame.init()
    
    #screen = pygame.display.set_mode((settings.WIN_SIZE_X, settings.WIN_SIZE_Y))

    main()

    pygame.quit()