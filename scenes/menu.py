import pygame

from settings.scene_settings import SceneController
from scenes.base import BaseScene

from objects.buttons import Button
from objects.buttons import ButtonSetup as bs


class MenuScene(BaseScene):
    def __init__(self):
        super().__init__()

    def _set_up_objects(self):
        self._objects = [
            Button("Начать", [100, 100], bs.MENU_DEFAULT,
                   SceneController.set_scene, "MainGame"),
            Button("Выйти", [100, 160], bs.MENU_DEFAULT,
                   pygame.event.post, pygame.event.Event(pygame.QUIT)),
        ]
