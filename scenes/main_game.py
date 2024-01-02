import random

import pygame

from controllers.scene_controller import SceneController
from objects.arrow import Arrow, Direction
from objects.tab import Tab
from scenes.base import BaseScene

from objects.buttons import Button
from objects.buttons import ButtonSetup as bs


class MainGameScene(BaseScene):
    def __init__(self):
        super().__init__()

    def _set_up_objects(self):
        self._objects = [
            Tab([0, 0]),
            # Arrow([400, 75], Direction.LEFT),
            # Arrow([500, 75], Direction.RIGHT),
            # Arrow([600, 375], Direction.DOWN),
        ]

    def process_additional_logic(self):
        if random.randint(0, 50) == 0:
            y = random.choice([i + 50 for i in range(0, 400, 100)])
            self._objects.append(Arrow([1200, y], y // 100))
