import datetime
from settings.arrow_settings import Direction


class ArrowData:
    def __init__(self, direction: Direction, time: datetime.time):
        self.direction = direction
        self.time = time

    def __str__(self):
        dict_name = {
            Direction.UP: "ВВЕРХ",
            Direction.DOWN: "ВНИЗ",
            Direction.LEFT: "ВЛЕВО",
            Direction.RIGHT: "ВПРАВО",
        }
        name = dict_name[self.direction]
        return f"Стрелка {name:6}: {self.time.minute:02}:{self.time.second:02}:{self.time.microsecond//1000:03}\n"


class AccordData:
    def __init__(self, num: int, time_start: datetime.time, time_end: datetime.time):
        self.num = num
        self.times = (time_start, time_end)

    def __str__(self):
        time1, time2 = self.times
        return (f"Аккорд {self.num:7}: "
                f"{time1.minute:02}:{time1.second:02}:{time1.microsecond//1000:03} - "
                f"{time2.minute:02}:{time2.second:02}:{time2.microsecond//1000:03}\n")
