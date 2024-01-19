import datetime
from typing import List, Optional, Union

import pygame

from handlers.song_reader import read_song
from handlers.song_structure import AccordData, ArrowData
from objects.tab_moving_items.arrow import Arrow
from objects.base import BaseObject
from objects.tab_moving_items.empty import EmptyArrow
from settings.arrow import ArrowSettings
from settings.tab import TabSettings
from settings.common import Common


class SongController(BaseObject):
    @staticmethod
    def get_lines_coord(tab_pos_y: int = 0):
        step = TabSettings.HEIGHT / 4
        lines_y = [int(tab_pos_y + step / 2 + step * i) for i in range(4)]
        return lines_y

    class Recorder:
        def __init__(self, path: str = "test.txt", in_file=True):
            self.keys = {
                pygame.K_UP: "W",
                pygame.K_LEFT: "A",
                pygame.K_DOWN: "S",
                pygame.K_RIGHT: "D",
            }
            self.timer = SongController.Timer()
            self.in_file = in_file
            if self.in_file:
                self.file = open(f"record/{path}", "w")

        def __del__(self):
            if self.in_file:
                self.file.close()

        def start(self):
            self.timer.reset()

        def event(self, event: pygame.event.Event):
            if not event.type == pygame.KEYDOWN:
                return
            if not (event.key in self.keys):
                return
            time = self.timer.get_time_from_start()
            text_line = f"{self.keys[event.key]} - {time.minute:02}:{time.second:02}:{time.microsecond // 1000:03}\n"
            self.file.write(text_line) if self.in_file else print(text_line)

    class Timer:
        def __init__(self):
            self.tick_start = pygame.time.get_ticks()

        def reset(self):
            self.__init__()

        def get_time_from_start(self):
            secs = (pygame.time.get_ticks() - self.tick_start) / 1000
            return datetime.time(minute=int(secs) // 60, second=int(secs) % 60,
                                 microsecond=int((secs - int(secs)) * 1_000_000))

    class Song:
        def __init__(self):
            self.sound: Optional[pygame.mixer.Sound] = None
            self.is_playing = False
            self.timer = SongController.Timer()

        def start(self):
            self.sound.play()
            self.timer.reset()
            self.is_playing = True

    def __init__(self):
        super().__init__([0, 0])
        self.data_items: List[Union[AccordData, ArrowData]] = []
        self.index_data_items = 0
        self.items: List[BaseObject] = []
        self.game_started = False
        self.song = self.Song()
        self.recorder = self.Recorder()

        self.timer = self.Timer()

        self.lines_y = self.get_lines_coord(0)
        self.spawn_x = Common.WINDOW_WIDTH + ArrowSettings.SIZE
        self.empty = EmptyArrow([self.spawn_x, self.lines_y[0]])

    def start(self, name="02_DC_Besporyadok"):
        self.song.sound, self.data_items = read_song(name)
        self.timer.reset()
        self.empty.start()
        self.recorder.start()
        self.items.append(self.empty)
        self.index_data_items = 0
        self.game_started = True

    def check_start_sound(self):
        if not self.song.is_playing and self.empty.is_reached:
            self.song.start()

    def event(self, event: pygame.event.Event):
        self.recorder.event(event)

    def logic(self):
        if not self.game_started or self.index_data_items >= len(self.data_items):
            return None
        next_data_item = self.data_items[self.index_data_items]
        self.check_start_sound()
        curr_time = self.timer.get_time_from_start()
        if curr_time >= next_data_item.time_start:
            if isinstance(next_data_item, ArrowData):
                direct = next_data_item.direction
                self.items.append(Arrow([self.spawn_x, self.lines_y[direct]], direct))
            elif isinstance(next_data_item, AccordData):
                pass
            self.index_data_items += 1
