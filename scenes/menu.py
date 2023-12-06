import pygame

from objects.arrow import Arrow
from objects.tab import Tab
from scenes.base import BaseScene
from settings import Settings

from objects.buttons import Button
from objects.buttons import ButtonSetup as bs


class MenuScene(BaseScene):
    def __init__(self):
        super().__init__()

    def _set_up_objects(self):

        self._objects = [
            Tab([0, 0]),
            # Button("Начать", [100, 100], bs.MENU_DEFAULT,
            #        print, 1),
            # Button("Выйти", [100, 160], bs.MENU_DEFAULT,
            #        pygame.event.post, pygame.event.Event(pygame.QUIT)),
            Arrow([300, 225], 0),
            Arrow([400, 75], 1),
            Arrow([500, 75], 2),
            Arrow([600, 375], 3),
        ]

    def additional_process_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            Settings.set_scene(1)
