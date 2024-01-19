import datetime
from settings.arrow import Direction


class ArrowData:
    def __init__(self, direction: int, time: datetime.time):
        self.direction = direction
        self.time_start = time

    def __str__(self):
        dict_name = {
            Direction.UP: "ВВЕРХ",
            Direction.DOWN: "ВНИЗ",
            Direction.LEFT: "ВЛЕВО",
            Direction.RIGHT: "ВПРАВО",
        }
        name = dict_name[self.direction]
        return (f"Стрелка {name:6}: "
                f"{self.time_start.minute:02}:{self.time_start.second:02}:{self.time_start.microsecond // 1000:03}\n")


class AccordData:
    def __init__(self, num: int, time_start: datetime.time, time_end: datetime.time):
        self.num = num
        self.time_start = time_start
        self.time_end = time_end

    def __str__(self):
        return (f"Аккорд {self.num:7}: "
                f"{self.time_start.minute:02}:{self.time_start.second:02}:{self.time_start.microsecond // 1000:03} - "
                f"{self.time_end.minute:02}:{self.time_end.second:02}:{self.time_end.microsecond//1000:03}\n")
