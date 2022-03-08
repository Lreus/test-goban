from typing import List, Tuple
import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """

    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if (
            not self.goban
            or x < 0
            or y < 0
            or y >= len(self.goban)
            or x >= len(self.goban[0])
        ):
            return Status.OUT
        elif self.goban[y][x] == ".":
            return Status.EMPTY
        elif self.goban[y][x] == "o":
            return Status.WHITE
        elif self.goban[y][x] == "#":
            return Status.BLACK

        raise RuntimeError(f'Unexpected char in goban table {self.goban[y][x]}')

    def is_taken(self, x: int, y: int) -> bool:
        starting_status = self.get_status(x, y)

        if starting_status == Status.EMPTY or self.goban_has_one_slot():
            return False

        to_test = [(x, y)]
        already_tested = []

        while len(to_test) > 0:
            current_position = to_test.pop()
            for comparison in self.get_position_around(*current_position):
                if comparison not in already_tested:
                    compared_status = self.get_status(*comparison)
                    if compared_status == Status.EMPTY:
                        return False
                    if compared_status == starting_status:
                        to_test.append(comparison)
            already_tested.append(current_position)

        return True

    def get_position_around(self, a: int, b: int) -> List[Tuple]:
        right = (a + 1, b)
        down = (a, b + 1)
        left = (a - 1, b)
        up = (a, b - 1)

        return [right, down, left, up]

    def goban_has_one_slot(self) -> bool:
        return len("".join(self.goban)) == 1

