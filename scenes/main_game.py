import random

import pygame

from objects.arrow import Arrow
from objects.tab import Tab
from scenes.base import BaseScene


class MainGameScene(BaseScene):
    def __init__(self):
        super().__init__()

    def _set_up_objects(self):
        self._objects = [
            Tab([0, 0]),
        ]

    # def additional_process_event(self, event):
    #     keys = {
    #         pygame.K_w: "W",
    #         pygame.K_a: "A",
    #         pygame.K_s: "S",
    #         pygame.K_d: "D",
    #     }

