import pygame

from objects.base import BaseObject
from objects.draw_tool import get_gradient
from settings.tab import TabSettings


class ClickArea(BaseObject):
    def __init__(self, pos: list):
        super().__init__(pos)
        self._x += TabSettings.CLICK_LINE_LEFT_MARGIN
        self._y += TabSettings.LINE_PADDING
        self.width, self.height = TabSettings.CLICK_LINE_WIDTH, TabSettings.HEIGHT // 4
        self.body_l = get_gradient(TabSettings.CLICK_LINE_COLOR, [self.width // 2, self.height], True)
        self.body_r = get_gradient(TabSettings.CLICK_LINE_COLOR[::-1], [self.width // 2, self.height], True)

        self.border_color = list(map(lambda x: max(0, x - 50), (TabSettings.CLICK_LINE_COLOR[1])))
        self.border_width = 5

    def draw(self, screen: pygame.Surface):
        screen.blit(self.body_l, [self._x, self._y])
        screen.blit(self.body_r, [self._x + self.width // 2, self._y])
        # Borders
        pygame.draw.rect(screen, self.border_color, [self._x, self._y, self.border_width, self.height])
        pygame.draw.rect(screen, self.border_color,
                         [self._x - self.border_width + self.width, self._y, self.border_width, self.height])
