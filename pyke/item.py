import smell

class Item(object):
    """description of class"""

    def __init__(self, pos: tuple, map_size: tuple, **kwargs):
        self.pos = pos
        self.value = kwargs.get('value', 1)
        self.smell = smell.Smell(pos, map_size, **kwargs)
