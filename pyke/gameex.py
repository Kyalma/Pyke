

class GameOver(Exception):
    """description of class"""

    def __init__(self, message):
        self.why = message
