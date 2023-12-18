import pygame

from objects.base import BaseObject
from objects.draw_tool import get_gradient
from settings import Settings


class TabLineClickArea(BaseObject):
    def __init__(self, rect: list):
        super().__init__(rect[:2])
        self.width, self.height = rect[2:]


class TabLine(BaseObject):
    def __init__(self, pos: list, height: int):
        super().__init__(pos)
        self.width = Settings.WINDOW_WIDTH
        self.height = height
        self.v_padding = 5
        background_color = [[150, 50, 0], [200, 100, 30]]
        click_line_color = [[150, 50, 0], [0, 100, 30]]
        self.hor_line_color = [100, 0, 0]

        self.body = get_gradient(background_color, [self.width, self.height])
        self.click_line = get_gradient(click_line_color, [100, self.height], True)  # Вынести в отдельный класс

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [0] * 3, [self._x, self._y, self.width, self.height])
        screen.blit(self.body, [self._x, self._y + self.v_padding, self.width, self.height - self.v_padding])
        # screen.blit(self.click_line, [self._x, self._y + self.v_padding, self.width, self.height - self.v_padding])
        pygame.draw.rect(screen, self.hor_line_color, [self._x, self._y + self.height // 2, self.width, 3])


class Tab(BaseObject):
    def __init__(self, pos: list):
        super().__init__(pos)
        self.height = 400  # TODO: Вынести в глобальную переменную (контроллер?)
        self.lines = [TabLine([0, self.height // 4 * _], self.height // 4) for _ in range(4)]

    def draw(self, screen: pygame.Surface):
        for line in self.lines:
            line.draw(screen)
