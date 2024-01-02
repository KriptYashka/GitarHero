import pygame

from application import Application
from settings import Settings


def main():
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
    app = Application(screen)
    app.run()


if __name__ == '__main__':
    main()
