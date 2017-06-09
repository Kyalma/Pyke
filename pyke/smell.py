#####################
#    
#      - - x - >
#    0 0 0 0 0 0 0
#  | 0 0 0 0 0 0 0
#  | 0 0 0 0 0 0 0
#  y 0 0 0 0 0 0 0
#  | 0 0 0 0 0 0 0
#  v 0 0 0 0 0 0 0
#    0 0 0 0 0 0 0
#
#####################

import concurrent.futures

slave_direction = {
    # the key is the direction of the mother
    # key:      (x, y)
    "up":       (1, 0),     # Slave goes right
    "right":    (0, -1),    # Slave goes down
    "down":     (-1, 0),    # Slave goes left
    "left":     (0, 1)      # Slave goes up
    }

mother_direction = {
    "up":       (0, 1),
    "right":    (1, 0),
    "down":     (0, -1),
    "left":     (-1, 0)
    }


class Smell(object):
    """description of class"""

    def __init__(self, start_pos: tuple, size: tuple, **kwargs):
        self.size_x = size[0]
        self.size_y = size[1]
        self.intensity = kwargs.get('intensity', self.size_x + self.size_y)
        
        tmp = [self.size_x + self.size_y for x in range(self.size_x)]
        self.map = [list(tmp) for y in range(self.size_y)]

        # Distance 0 to the item
        self.map[start_pos[1]][start_pos[0]] = 0

        diffuser = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        next_mother = [
            ("up", start_pos[0], start_pos[1] + 1),
            ("right", start_pos[0] + 1, start_pos[1]),
            ("down", start_pos[0], start_pos[1] - 1),
            ("left", start_pos[0] - 1, start_pos[1])
            ]
        current_intensity = 1
        while next_mother and current_intensity <= self.intensity:
            tasks = [
                diffuser.submit(self._create_mother, mother, current_intensity)   \
                    for mother in next_mother
                ]
            next_mother.clear()
            for task in concurrent.futures.as_completed(tasks):
                if task._result:
                    next_mother.append(task._result)
                print(task)
                pass
            current_intensity += 1


    def _create_mother(self, data: tuple, base_intensity):
        # data[0] is where the mother id headed
        # data[1] is her current position in x
        # data[2] is her current position in y

        self.map[data[2]][data[1]] = base_intensity

        dir = slave_direction[data[0]]
        next_x = data[1] + dir[0]
        next_y = data[2] + dir[1]
        next_intensity = base_intensity + 1

        while next_x >= 0 and next_x < self.size_x   \
            and next_y >= 0 and next_y < self.size_y \
            and next_intensity <= self.intensity:

            self.map[next_y][next_x] = next_intensity
            next_x = next_x + dir[0]
            next_y = next_y + dir[1]
            next_intensity = next_intensity + 1

        next_mother_dir = mother_direction[data[0]]
        next_mother_x = data[1] + next_mother_dir[0]
        next_mother_y = data[2] + next_mother_dir[1]

        if next_mother_x >= 0 and next_mother_x < self.size_x    \
            and next_mother_y >= 0 and next_mother_y < self.size_y:
            return (data[0], next_mother_x, next_mother_y)
        return None