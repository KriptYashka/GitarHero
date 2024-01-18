import datetime
import os
from typing import List

import pygame

from handlers.song_structure import ArrowData, AccordData
from settings.arrow_settings import Direction
from settings.window_settings import Settings


def get_data(words: List[str]):
    if words[0] in "1234":
        num = int(words[0])
        m1, s1, mc1 = map(int, words[2].split(":"))
        m2, s2, mc2 = map(int, words[4].split(":"))
        time_start = datetime.time(minute=m1, second=s1, microsecond=mc1*1000)
        time_end = datetime.time(minute=m2, second=s2, microsecond=mc2*1000)
        return AccordData(num, time_start, time_end)
    if words[0].lower() in "wasd":
        direction = Direction.control_to_int(words[0].lower())
        m1, s1, mc1 = map(int, words[2].split(":"))
        time = datetime.time(minute=m1, second=s1, microsecond=mc1*1000)
        return ArrowData(direction, time)
    return None


def read_song(path: str):
    f_tabs = open(os.path.join(Settings.ROOT_DIR, f"songs/{path}/tabs.txt"))
    key_data = []
    for line in f_tabs:
        if line.startswith("#"):
            continue
        if (item := get_data(line.strip().split())) is not None:
            key_data.append(item)

    song = pygame.mixer.Sound(os.path.join(Settings.ROOT_DIR, f"songs/{path}/song.mp3"))
    return song, key_data

