class Snake(object):
    """description of class"""


    def __init__(self, posx, posy, size: int = 3):
        self.body = list()
        self.size = size
        self.next_move = None
        self.next_move_value = None
        for i in range(size):
            self.body.insert(0, (posx - i, posy))


    def auto_move(self):
        self.body.append(self.next_move)
        del self.body[0]
        self.next_move = None
        self.next_move_value = None


    def manual_move(self, posx, posy):
        if (posx, posy) in self.body:
            print('Invalid move: Already there')
        else:
            self.body.append((posx, posy))


    def smell(self, map):
        pos_head = self.body[-1]

        around = set()

        around.add((pos_head[0], pos_head[1] - 1))
        around.add((pos_head[0], pos_head[1] + 1))
        around.add((pos_head[0] - 1, pos_head[1]))
        around.add((pos_head[0] + 1, pos_head[1]))

        around -= set(self.body)

        for dir in around:
            if not self.next_move or self.next_move_value > map[dir[1]][dir[0]]:
                self.next_move = dir
                self.next_move_value = map[dir[1]][dir[0]]
        if not self.next_move:
            self.next_move = around.pop()