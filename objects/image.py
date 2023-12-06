import pygame

from objects.base import BaseObject


class Image(BaseObject):
    def __init__(self, path: str, rect: pygame.Rect, rotation: int = 0):
        super().__init__([rect.x, rect.y])
        self.__rect = rect
        self.__img = pygame.image.load(path)
        if rotation != 0:
            self.__img = pygame.transform.rotate(self.__img, rotation)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.__img, self.__rect)
