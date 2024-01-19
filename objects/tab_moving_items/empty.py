from settings.arrow import ArrowSettings
from objects.base import BaseObject
from settings.tab import TabSettings


class EmptyArrow(BaseObject):
    def __init__(self, pos: list):
        super().__init__(pos)
        self.is_reached = False
        self.is_enable = False

    def start(self):
        self.is_enable = True

    def logic(self):
        if not self.is_enable:
            return None
        self._x -= ArrowSettings.SPEED
        if self._x <= TabSettings.CLICK_LINE_LEFT_MARGIN + TabSettings.CLICK_LINE_WIDTH // 2:
            self.is_reached = True
            self.is_enable = False
