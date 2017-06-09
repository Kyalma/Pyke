import time
import pygame

import item
import settings
import snake

FOR_EVER_AND_EVER = True

def clear_screen():
    pygame.draw.rect(screen,
                     0x0,
                     (0, 0, settings.WIN_SIZE_X, settings.WIN_SIZE_Y))


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


def draw_point(point_pos):
    pygame.draw.rect(screen,
                     0xFFFFFF,
                     (point_pos[0] * settings.CELL_SIZE, point_pos[1] * settings.CELL_SIZE,
                      settings.CELL_SIZE, settings.CELL_SIZE))
    pygame.display.update()


def dump_item_map(map):
    for y in map:
        print(
            " ".join("{:>3}".format(x) for x in y)
            )
    
def add_points_to_map(map, points):
    for point in points:
        map[point[1]][point[0]] = 1


def main():

    fruit = item.Item((5, 12), (settings.CELLS_X, settings.CELLS_Y))

    #tmp = [0 for i in range(settings.CELLS_X)]
    #map = [list(tmp) for i in range(settings.CELLS_Y)]
    
    ia = snake.Snake(20, 20)
    
    draw_snake(ia.body)
    draw_point(fruit.pos)
    dump_item_map(fruit.smell.map)

    while FOR_EVER_AND_EVER:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ia.smell(fruit.smell.map)
        ia.auto_move()

        clear_screen()
        draw_snake(ia.body)
        draw_point(fruit.pos)

        time.sleep(0.5)


if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode((settings.WIN_SIZE_X, settings.WIN_SIZE_Y))

    main()

    pygame.quit()