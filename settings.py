import pygame


class Settings:
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    BACKGROUND_COLOR = [0] * 3
    scene_changed = True
    scene_index = 0

    @staticmethod
    def set_scene(index):
        Settings.scene_changed = True
        Settings.scene_index = index

    @staticmethod
    def set_menu_scene():
        Settings.set_scene(0)
