class Direction:
    UP = 0
    RIGHT = 1
    LEFT = 2
    DOWN = 3

    @staticmethod
    def control_to_int(key: str):
        dict_name = {
            "w": Direction.UP,
            "a": Direction.LEFT,
            "s": Direction.DOWN,
            "d": Direction.RIGHT,
        }
        return dict_name[key] if key in dict_name else None


class ArrowSettings:
    SPEED = 8
    SIZE = 100
    color = {
        Direction.UP: [200, 0, 0],
        Direction.RIGHT: [50, 200, 50],
        Direction.DOWN: [0, 0, 200],
        Direction.LEFT: [200, 100, 200],
    }
