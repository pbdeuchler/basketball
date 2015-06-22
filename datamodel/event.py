from enum import Enum

import basketball.utils as utils

event_types = [
    'quarter_start', 'quarter_finish', 'jump_ball', 'shot_made', 'shot_miss',
    'turnover', 'offensive_rebound', 'defensive_rebound', 'foul',
    'free_throw_made', 'free_throw_missed', ''
]

EventType = Enum('EventType', " ".join(event_types))


class EventTime:

    def __init__(self, minutes: int, seconds: int, milliseconds: int) -> None:
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds

    def equality(self, other: EventTime) -> int:
        minute_comparison = utils.cmp(self.minutes, other.minutes)
        if minute_comparison != 0:
            return minute_comparison

        second_comparison = utils.cmp(self.seconds, other.seconds)
        if second_comparison != 0:
            return second_comparison

        millisecond_comparison = utils.cmp(self.milliseconds, other.milliseconds)
        if millisecond_comparison != 0:
            return millisecond_comparison

        return 0

    def __lt__(self, other: EventTime) -> bool:
        if self.equality(other) == -1:
            return True
        return False

    def __le__(self, other: EventTime) -> bool:
        if self.__lt__(other) or self.__eq__(other):
            return True
        return False

    def __eq__(self, other: EventTime) -> bool:
        if self.equality(other) == 0:
            return True
        return False

    def __ne__(self, other: EventTime) -> bool:
        if self.__eq__(other):
            return False
        return True

    def __gt__(self, other: EventTime) -> bool:
        if self.equality(other) == 1:
            return True
        return False

    def __ge__(self, other: EventTime) -> bool:
        if self.__gt__(other) or self.__eq__(other):
            return True
        return False

    def to_json(self) -> str:
        pass


class Event(object):

    def __init__(self,
                type: EventType,  # type: ignore
                player: str,
                time: EventTime) -> None:

        pass
