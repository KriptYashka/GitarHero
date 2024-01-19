import pygame

from application import Application
from settings.common import Common


def main():
    pygame.display.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Common.WINDOW_WIDTH, Common.WINDOW_HEIGHT])
    app = Application(screen)
    app.run()


if __name__ == '__main__':
    main()
