import datetime
from typing import List, Optional

import pygame

from handlers.song_reader import read_song
from handlers.song_structure import ArrowData, AccordData
from objects.base import BaseObject
from objects.draw_tool import get_gradient
from objects.arrow import Arrow
from objects.empty import EmptyArrow
from settings.arrow_settings import ArrowSettings
from settings.tab_settings import TabSettings
from settings.window_settings import Settings


class TabLineClickArea(BaseObject):
    def __init__(self, pos: list):
        super().__init__(pos)
        self._x += TabSettings.CLICK_LINE_LEFT_MARGIN
        self._y += TabSettings.LINE_PADDING
        self.width, self.height = TabSettings.CLICK_LINE_WIDTH, TabSettings.HEIGHT // 4
        self.body_l = get_gradient(TabSettings.CLICK_LINE_COLOR, [self.width // 2, self.height], True)
        self.body_r = get_gradient(TabSettings.CLICK_LINE_COLOR[::-1], [self.width // 2, self.height], True)

        self.border_color = list(map(lambda x: max(0, x - 50), (TabSettings.CLICK_LINE_COLOR[1])))
        self.border_width = 5

    def draw(self, screen: pygame.Surface):
        screen.blit(self.body_l, [self._x, self._y])
        screen.blit(self.body_r, [self._x + self.width // 2, self._y])
        # Borders
        pygame.draw.rect(screen, self.border_color, [self._x, self._y, self.border_width, self.height])
        pygame.draw.rect(screen, self.border_color,
                         [self._x - self.border_width + self.width, self._y, self.border_width, self.height])


class TabLine(BaseObject):
    def __init__(self, pos: list, height: int):
        super().__init__(pos)
        self.width = Settings.WINDOW_WIDTH
        self.height = height
        self.v_padding = TabSettings.LINE_PADDING
        self.l_margin = TabSettings.CLICK_LINE_LEFT_MARGIN
        self.hor_line_color = TabSettings.HOR_LINE_COLOR

        self.body = get_gradient(TabSettings.LINE_COLOR,
                                 [self.width, self.height])
        self.click_area = TabLineClickArea(pos)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [0] * 3, [self._x, self._y, self.width, self.height])
        screen.blit(self.body, [self._x, self._y + self.v_padding, self.width, self.height - self.v_padding])
        self.click_area.draw(screen)
        pygame.draw.rect(screen, self.hor_line_color, [self._x, self._y + (self.height + self.v_padding) // 2,
                                                       self.width, 3])


class TabSongController(BaseObject):
    @staticmethod
    def get_lines_coord(tab_pos_y: int = 0):
        step = TabSettings.HEIGHT / 4
        lines_y = [int(tab_pos_y + step / 2 + step * i) for i in range(4)]
        return lines_y

    class Timer:
        def __init__(self):
            self.time_start = self.time_current = None
            self.reset()

        def reset(self):
            self.time_start = self.time_current = pygame.time.get_ticks()

        def get_time_from_start(self, flag=False):
            ticks = pygame.time.get_ticks()
            secs = (ticks - self.time_start) / 1000
            dt = datetime.time(minute=int(secs) // 60, second=int(secs) % 60,
                               microsecond=int((secs - int(secs)) * 1_000_000))
            return dt

    def __init__(self):
        super().__init__([0, 0])
        self.data_items: List[Optional[AccordData, ArrowData]] = []
        self.items: List[BaseObject] = []
        self.is_playing: bool = False
        self.song: Optional[pygame.mixer.Sound] = None
        self.is_song_playing = False

        self.timer = self.Timer()
        self.shift_timer = self.Timer()
        self.req_time_start_song = datetime.time()
        self.iter = None
        self.next_elem = None
        self.lines_y = self.get_lines_coord(0)
        self.pos_left = TabSettings.CLICK_LINE_LEFT_MARGIN + TabSettings.CLICK_LINE_WIDTH // 2
        self.pos_right = Settings.WINDOW_WIDTH + ArrowSettings.SIZE
        self.empty: Optional[EmptyArrow] = None

        self.fout = open("record/rec1.txt", "w")

    def __del__(self):
        self.fout.close()

    def read_song(self, name: str = "01_test"):
        self.song, self.data_items = read_song(name)
        self.iter = iter(self.data_items)

    def start(self):
        self.read_song("02_DC_Besporyadok")
        self.is_playing = True
        self.timer.reset()
        self.empty = EmptyArrow([self.pos_right, self.lines_y[0]])
        self.items.append(self.empty)
        secs = (self.pos_right - self.pos_left + ArrowSettings.SIZE) / (
                ArrowSettings.SPEED * 60)  # Умножаем на время кадра
        self.req_time_start_song = datetime.time(second=int(secs), microsecond=int((secs - int(secs)) * 1_000_000))
        self.next_elem = next(self.iter)

    def event(self, event: pygame.event.Event):
        keys = {
            pygame.K_UP: "W",
            pygame.K_LEFT: "A",
            pygame.K_DOWN: "S",
            pygame.K_RIGHT: "D",
        }
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                time = self.shift_timer.get_time_from_start(True)
                self.fout.write(
                    keys[event.key] + " - " + f"{time.minute:02}:{time.second:02}:{time.microsecond//1000:03}\n")
                print(keys[event.key] + " - " + f"{time.minute:02}:{time.second:02}:{time.microsecond//1000:03}")

    def logic(self):
        # print(pygame.time.get_ticks())
        if not self.is_playing:
            return None
        if not self.is_song_playing and self.empty.is_reached:
            self.song.play()
            self.is_song_playing = True
            self.shift_timer.reset()
        if self.next_elem is None:
            return None
        if self.timer.get_time_from_start() >= self.next_elem.time_start:
            if isinstance(self.next_elem, ArrowData):
                direct = self.next_elem.direction
                self.items.append(Arrow([self.pos_right, self.lines_y[direct]], direct))
            elif isinstance(self.next_elem, AccordData):
                pass

            # print(self.next_elem)
            try:
                self.next_elem = next(self.iter)
            except StopIteration:
                self.next_elem = None


class Tab(BaseObject):
    def __init__(self, pos: list = None):
        pos = pos or [0, 0]
        super().__init__(pos)

        self.song_controller = TabSongController()

        self.lines = [TabLine([pos[0], TabSettings.HEIGHT // 4 * _], TabSettings.HEIGHT // 4) for _ in range(4)]
        click_line_width = 5
        self.click_line_rect = (
            pygame.Rect(
                self._x + TabSettings.CLICK_LINE_LEFT_MARGIN + TabSettings.CLICK_LINE_WIDTH // 2 - click_line_width // 2,
                self._y, click_line_width, TabSettings.HEIGHT + TabSettings.LINE_PADDING)
        )
        self.click_line_color = TabSettings.HOR_LINE_COLOR

    def activate(self):
        self.song_controller.start()

    def event(self, event: pygame.event.Event):
        self.song_controller.event(event)

    def logic(self):
        self.song_controller.logic()
        for item in self.song_controller.items:
            item.logic()

    def draw(self, screen: pygame.Surface):
        for line in self.lines:
            line.draw(screen)
        pygame.draw.rect(screen, self.click_line_color, self.click_line_rect)
        for item in self.song_controller.items:
            item.draw(screen)


if __name__ == "__main__":
    TabSongController().read_song()
