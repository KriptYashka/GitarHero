import pygame


class BaseScene:
    def __init__(self):
        self._objects = []
        self._set_up_objects()

    def _set_up_objects(self):
        pass

    def activate(self):
        for item in self._objects:
            item.activate()
        self.additional_activate()

    def additional_activate(self):
        pass

    def process_event(self, event):
        for item in self._objects:
            item.event(event)
        self.additional_process_event(event)

    def additional_process_event(self, event):
        pass

    def process_logic(self):
        for item in self._objects:
            item.logic()
        self.process_additional_logic()

    def process_additional_logic(self):
        pass

    def process_draw(self, screen: pygame.Surface):
        for item in self._objects:
            item.draw(screen)
        self.process_additional_draw(screen)

    def process_additional_draw(self, screen):
        pass
