import gameex
import item
import settings

class Snake(object):
    """description of class"""


    def __init__(self, posx, posy, size: int = 3):
        self.body = list()
        self.size = size
        self.next_move = None
        self.next_move_value = None
        for i in range(size):
            self.body.insert(0, (posx - i, posy))


    def is_gonna_eat(self):
        return self.next_move_value == 0


    def eat(self, items: list):
        # TODO: server send EAT

        for i in range(len(items)):
            if items[i].pos == self.next_move:
                del items[i]
                break

        self.body.append(self.next_move)
        self.next_move = None
        self.next_move_value = None

        # TODO: delete item


    def auto_move(self):

        self.body.append(self.next_move)
        del self.body[0]
        self.next_move = None
        self.next_move_value = None


    def manual_move(self, posx, posy) -> bool:
        if (posx, posy) in self.body:
            print('Invalid move: Already there')
            return False
        else:
            self.body.append((posx, posy))
        return True


    def smell(self, map) -> None:
        pos_head = self.body[-1]

        around = set()

        # OUT OF BOUND Y
        if pos_head[1] > 0:
            around.add((pos_head[0], pos_head[1] - 1))

        if pos_head[1] < settings.CELLS_Y - 1:
            around.add((pos_head[0], pos_head[1] + 1))

        # OUT OF BOUND X
        if pos_head[0] > 0:
            around.add((pos_head[0] - 1, pos_head[1]))

        if pos_head[0] < settings.CELLS_X - 1:
            around.add((pos_head[0] + 1, pos_head[1]))

        around -= set(self.body)

        if len(around) == 0:
            raise gameex.GameOver("Cannot move")
        for dir in around:
            if not self.next_move or self.next_move_value > map[dir[1]][dir[0]]:
                # Seek the lowest value (closest to the food)
                self.next_move = dir
                self.next_move_value = map[dir[1]][dir[0]]

