import pygame


class BaseObject:
    def __init__(self, pos: list):
        if len(pos) != 2:
            raise AttributeError("Параметр pos должен иметь 2 элемента")
        self._x, self._y = pos

    def get_position(self):
        return self._x, self._y

    def set_position(self, x: int, y: int):
        self._x, self._y = x, y

    def activate(self):
        pass

    def event(self, event: pygame.event.Event):
        pass

    def logic(self):
        pass

    def draw(self, screen: pygame.Surface):
        pass
