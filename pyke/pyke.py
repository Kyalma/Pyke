import time
import pygame
import random

import item
import settings
import snake

FOR_EVER_AND_EVER = True

def clear_screen():
    screen.fill(0x0)


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


def draw_debug_tile(map):
    for y in range(settings.CELLS_Y):
        for x in range(settings.CELLS_X):
            screen.blit(value_tile[map[y][x]], (x * settings.CELL_SIZE, y * settings.CELL_SIZE))
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

    items = list()
    fruit = item.Item((5, 12), (settings.CELLS_X, settings.CELLS_Y))

    items.append(fruit)

    #tmp = [0 for i in range(settings.CELLS_X)]
    #map = [list(tmp) for i in range(settings.CELLS_Y)]
    
    ia = snake.Snake(20, 20)
    
    draw_snake(ia.body)
    draw_point(fruit.pos)
    
    #dump_item_map(fruit.smell.map)
    draw_debug_tile(fruit.smell.map)

    while FOR_EVER_AND_EVER:

        if len(items) == 0:
            random.seed()
            items.append(
                item.Item(
                    (random.randint(0, settings.CELLS_X - 1), random.randint(0, settings.CELLS_Y)),
                    (settings.CELLS_X, settings.CELLS_Y)
                    )
                )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for _item in items:
            ia.smell(_item.smell.map)

        if ia.is_gonna_eat():
            ia.eat(items)
        else:
            ia.auto_move()

        clear_screen()

        for _item in items:
            draw_debug_tile(_item.smell.map)
            draw_point(_item.pos)
        
        draw_snake(ia.body)

        #time.sleep(0.3)


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont("monospace", int(settings.CELL_SIZE * 2 / 3))

    value_tile = dict()
    for value in range(settings.CELLS_X + settings.CELLS_Y):
        value_tile[value] = font.render("{}".format(value), True, (255, 255, 255))
    
    screen = pygame.display.set_mode((settings.WIN_SIZE_X, settings.WIN_SIZE_Y))

    main()

    pygame.font.quit()
    pygame.quit()