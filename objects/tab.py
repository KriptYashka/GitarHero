import pygame

from objects.base import BaseObject
from settings import Settings


class TabLine(BaseObject):
    def __init__(self, pos: list, height: int):
        super().__init__(pos)
        self.width = Settings.WINDOW_WIDTH
        self.height = height
        self.v_padding = 5
        background_color = [[150, 50, 0], [200, 100, 30]]
        click_line_color = [[150, 50, 0], [200, 100, 30]]
        self.line_color = [100, 0, 0]

        self.body = self.get_v_gradient_surface(*background_color)
        self.click_line = self.get_v_gradient_surface(*click_line_color)

    def get_v_gradient_surface(self, left_color: list, right_color: list) -> pygame.Surface:
        colour_rect = pygame.Surface((2, 2))
        pygame.draw.line(colour_rect, left_color, (0, 0), (0, 1))
        pygame.draw.line(colour_rect, right_color, (1, 0), (1, 1))
        return pygame.transform.smoothscale(colour_rect, (self.width, self.height))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [0] * 3, [self._x, self._y, self.width, self.height])
        screen.blit(self.body, [self._x, self._y + self.v_padding, self.width, self.height - self.v_padding])
        pygame.draw.rect(screen, self.line_color, [self._x, self._y + self.height // 2, self.width, 3])


class Tab(BaseObject):
    def __init__(self, pos: list):
        super().__init__(pos)
        self.height = 400
        self.lines = [TabLine([0, self.height // 4 * _], self.height // 4) for _ in range(4)]

    def draw(self, screen: pygame.Surface):
        for line in self.lines:
            line.draw(screen)
