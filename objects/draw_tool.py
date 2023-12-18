import pygame


def get_gradient(colors: list, size: list, is_vertical: bool = True):
    """
    Возвращает поверхность с градиентом.

    :param colors: Список с двумя цветами
    :param size: Размеры прямоугольника
    :param is_vertical: Вертикальный или горизонтальный градиент
    :return: Поверхность с градиентом
    """
    start_color, end_color = colors
    colour_rect = pygame.Surface((2, 2))
    if is_vertical:
        pygame.draw.line(colour_rect, start_color, (0, 0), (0, 1))
        pygame.draw.line(colour_rect, end_color, (1, 0), (1, 1))
    else:
        pygame.draw.line(colour_rect, start_color, (0, 0), (1, 0))
        pygame.draw.line(colour_rect, end_color, (0, 1), (1, 1))
    return pygame.transform.smoothscale(colour_rect, size)


def get_center_gradient(colors: list, size: list, is_vertical: bool = True):
    """
    Возвращает поверхность с градиентом от центральной линии

    :param colors: Список с двумя цветами. Первый цвет - центр.
    :param size: Размеры прямоугольника
    :param is_vertical: Вертикальный или горизонтальный градиент
    :return: Поверхность с градиентом от центральной линии
    """
    half_size = [size[0] + size[1] // 2] if is_vertical else [size[0] // 2 + size[1]]

    surface = get_gradient(colors, size, is_vertical)
    mirror = pygame.transform.flip(surface, 1, -1) if is_vertical else pygame.transform.flip(surface, -1, 1)
    res = pygame.Surface(size, pygame.SRCALPHA)
    res.blit(surface, [0, 0])
    pos = [0, surface.get_height()] if is_vertical else [surface.get_width(), 0]
    res.blit(mirror, pos)  # Только для горизонтальной
    return res
