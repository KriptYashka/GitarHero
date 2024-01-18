import pygame

from scenes.main_game import MainGameScene
from scenes.menu import MenuScene
from settings.window_settings import Settings
from settings.scene_settings import SceneController


class Application:
    def __init__(self, screen):
        self.screen = screen
        self.game_over = False
        self.scenes = {
            "Menu": MenuScene(),
            "MainGame": MainGameScene(),
        }

    def scene_activate(self):
        SceneController.scene_changed = False
        self.scenes[SceneController.scene_name].activate()

    def scene_event(self):
        for event in pygame.event.get():
            self.process_application_exit(event)
            self.scenes[SceneController.scene_name].process_event(event)

    def process_application_exit(self, event):
        if event.type != pygame.QUIT:
            return
        self.game_over = True

    def scene_logic(self):
        self.scenes[SceneController.scene_name].process_logic()

    def scene_draw(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.scenes[SceneController.scene_name].process_draw(self.screen)
        pygame.display.flip()

    def process_frame(self):
        if SceneController.scene_changed:
            self.scene_activate()
            return

        self.scene_event()
        self.scene_logic()
        self.scene_draw()
        pygame.time.wait(1000//60)

    def run(self):
        while not self.game_over:
            self.process_frame()
