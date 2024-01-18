from settings.arrow_settings import ArrowSettings
from objects.base import BaseObject
from settings.tab_settings import TabSettings


class EmptyArrow(BaseObject):
    def __init__(self, pos: list):
        super().__init__(pos)
        self.is_reached = False

    def logic(self):
        self._x -= ArrowSettings.SPEED
        if self._x <= TabSettings.CLICK_LINE_LEFT_MARGIN + TabSettings.CLICK_LINE_WIDTH // 2:
            self.is_reached = True
