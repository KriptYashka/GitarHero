import pygame

from controllers.tab_controller import TabController as TC
from objects.base import BaseObject
from objects.draw_tool import get_gradient
from settings import Settings


class TabLineClickArea(BaseObject):
    def __init__(self, pos: list):
        super().__init__(pos)
        self._x += TC.CLICK_LINE_LEFT_MARGIN
        self._y += TC.LINE_PADDING
        self.width, self.height = TC.CLICK_LINE_WIDTH, TC.HEIGHT // 4
        self.body_l = get_gradient(TC.CLICK_LINE_COLOR, [self.width // 2, self.height], True)
        self.body_r = get_gradient(TC.CLICK_LINE_COLOR[::-1], [self.width // 2, self.height], True)

        self.border_color = list(map(lambda x: max(0, x - 50), (TC.CLICK_LINE_COLOR[1])))
        self.border_width = 5

    def draw(self, screen: pygame.Surface):
        screen.blit(self.body_l, [self._x, self._y])
        screen.blit(self.body_r, [self._x + self.width // 2, self._y])
        # Borders
        pygame.draw.rect(screen, self.border_color, [self._x, self._y, self.border_width, self.height])
        pygame.draw.rect(screen, self.border_color,
                         [self._x - self.border_width + self.width, self._y, self.border_width, self.height])


class TabLine(BaseObject):
    def __init__(self, pos: list, height: int):
        super().__init__(pos)
        self.width = Settings.WINDOW_WIDTH
        self.height = height
        self.v_padding = TC.LINE_PADDING
        self.l_margin = TC.CLICK_LINE_LEFT_MARGIN
        self.hor_line_color = TC.HOR_LINE_COLOR

        self.body = get_gradient(TC.LINE_COLOR,
                                 [self.width, self.height])
        self.click_area = TabLineClickArea(pos)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [0] * 3, [self._x, self._y, self.width, self.height])
        screen.blit(self.body, [self._x, self._y + self.v_padding, self.width, self.height - self.v_padding])
        self.click_area.draw(screen)
        pygame.draw.rect(screen, self.hor_line_color, [self._x, self._y + (self.height + self.v_padding) // 2,
                                                       self.width, 3])


class Tab(BaseObject):
    def __init__(self, pos: list = None):
        pos = pos or [0, 0]
        super().__init__(pos)
        self.lines = [TabLine([pos[0], TC.HEIGHT // 4 * _], TC.HEIGHT // 4) for _ in range(4)]
        click_line_width = 5
        self.click_line_rect = (
            pygame.Rect(self._x + TC.CLICK_LINE_LEFT_MARGIN + TC.CLICK_LINE_WIDTH // 2 - click_line_width // 2,
                        self._y, click_line_width, TC.HEIGHT + TC.LINE_PADDING)
        )
        self.click_line_color = TC.HOR_LINE_COLOR

    def draw(self, screen: pygame.Surface):
        for line in self.lines:
            line.draw(screen)
        pygame.draw.rect(screen, self.click_line_color, self.click_line_rect)
