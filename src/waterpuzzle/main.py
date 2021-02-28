from enum import Enum, auto


class Glass:
    def __init__(self, colors=[]):
        self.colors = colors
        self.size = len(colors)

    def pop(self, to):
        pass

    def is_full(self):
        return self.size == 4

    def is_complete(self):
        return self.size == 4 and len(set(self.colors)) == 1
