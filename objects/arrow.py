import random

import pygame

from controllers.arrow_controller import ArrowController
from objects.base import BaseObject


class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class ArrowData:
    color = {
        Direction.UP: [200, 0, 0],
        Direction.RIGHT: [50, 200, 50],
        Direction.DOWN: [0, 0, 200],
        Direction.LEFT: [200, 100, 200],
    }


class Arrow(BaseObject):
    def __init__(self, pos: list, direction: int):
        super().__init__(pos)
        self.direction = direction
        self.width = self.height = ArrowController.SIZE
        self.body = []
        self.outline = []
        self.color_body = ArrowData.color[self.direction]
        self.color_outline = [100] * 3

    def activate(self):
        arrow_body = self.get_arrow_points()
        arrow_outline = self.get_arrow_points(2)
        self.process_rotate(arrow_body)
        self.process_rotate(arrow_outline)
        self.body, self.outline = arrow_body, arrow_outline

    def logic(self):
        self._x -= 1
        self.activate()

    def process_rotate(self, items):
        for i in range(len(items)):
            for j in range(len(items[i])):
                if self.direction == Direction.UP:
                    items[i][j][1] *= -1
                elif self.direction == Direction.RIGHT:
                    items[i][j][0], items[i][j][1] = items[i][j][1], items[i][j][0]
                elif self.direction == Direction.LEFT:
                    items[i][j][0], items[i][j][1] = -items[i][j][1], items[i][j][0]
                items[i][j][0] += self._x
                items[i][j][1] += self._y

    def get_arrow_points(self, shadow=0):
        self.width += shadow * 2
        self.height += shadow * 2
        height_cup = -self.height // 8 - shadow // 2
        width_base = self.width // 4
        triangle = [
            [0, self.height // 2],
            [-self.width // 2, height_cup],
            [self.width // 2, height_cup],
        ]
        base = [
            [-width_base, height_cup],
            [width_base, height_cup],
            [width_base, -self.height // 2],
            [-width_base, -self.height // 2],
        ]
        self.width -= shadow * 2
        self.height -= shadow * 2
        return [base, triangle]

    def draw(self, screen: pygame.Surface):
        for item in self.outline:
            pygame.draw.polygon(screen, self.color_outline, item)
        for item in self.body:
            pygame.draw.polygon(screen, self.color_body, item)
