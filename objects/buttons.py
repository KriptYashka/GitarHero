import pygame
from objects.base import BaseObject


class ButtonSettings:
    def __init__(self, size: list, color, outline):
        self.width, self.height = size
        self.color = color
        self.outline = outline


class ButtonSetup:
    MENU_DEFAULT = ButtonSettings([100, 50], [255, 0, 0], False)


class Button(BaseObject):
    def __init__(self, text: str, pos: list, settings: ButtonSettings, action, *args):
        super().__init__(pos)
        self.__width, self.__height = settings.width, settings.height
        self.__rect = pygame.Rect(pos[0], pos[1], settings.width, settings.height)
        self.__color = settings.color
        self.__text = text
        self.__action = action
        self.__args = args

    def __set_text(self, text: str):
        self.__text = text

    def event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__rect.collidepoint(*pygame.mouse.get_pos()):
                self.__action(*self.__args)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.__color, self.__rect)
