import pygame

from objects.base import BaseObject
from objects.tab.line import Line
from objects.tab.song_controller import SongController
from settings.tab import TabSettings


class Tab(BaseObject):
    def __init__(self, pos: list = None):
        pos = pos or [0, 0]
        super().__init__(pos)

        self.song_controller = SongController()

        self.lines = [Line([pos[0], TabSettings.HEIGHT // 4 * _], TabSettings.HEIGHT // 4) for _ in range(4)]
        click_line_width = 5
        self.click_line_rect = (
            pygame.Rect(
                self._x + TabSettings.CLICK_LINE_LEFT_MARGIN + TabSettings.CLICK_LINE_WIDTH // 2 - click_line_width // 2,
                self._y, click_line_width, TabSettings.HEIGHT + TabSettings.LINE_PADDING)
        )
        self.click_line_color = TabSettings.HOR_LINE_COLOR

    def activate(self):
        self.song_controller.start()

    def event(self, event: pygame.event.Event):
        self.song_controller.event(event)

    def logic(self):
        self.song_controller.logic()
        for item in self.song_controller.items:
            item.logic()

    def draw(self, screen: pygame.Surface):
        for line in self.lines:
            line.draw(screen)
        pygame.draw.rect(screen, self.click_line_color, self.click_line_rect)
        for item in self.song_controller.items:
            item.draw(screen)
