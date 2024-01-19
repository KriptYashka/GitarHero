import pygame

from objects.base import BaseObject
from objects.draw_tool import get_gradient
from objects.tab.click_area import ClickArea
from settings.tab import TabSettings
from settings.common import Common


class Line(BaseObject):
    def __init__(self, pos: list, height: int):
        super().__init__(pos)
        self.width = Common.WINDOW_WIDTH
        self.height = height
        self.v_padding = TabSettings.LINE_PADDING
        self.l_margin = TabSettings.CLICK_LINE_LEFT_MARGIN
        self.hor_line_color = TabSettings.HOR_LINE_COLOR

        self.body = get_gradient(TabSettings.LINE_COLOR,
                                 [self.width, self.height])
        self.click_area = ClickArea(pos)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [0] * 3, [self._x, self._y, self.width, self.height])
        screen.blit(self.body, [self._x, self._y + self.v_padding, self.width, self.height - self.v_padding])
        self.click_area.draw(screen)
        pygame.draw.rect(screen, self.hor_line_color, [self._x, self._y + (self.height + self.v_padding) // 2,
                                                       self.width, 3])
