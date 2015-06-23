import typing
import datetime


class Player:

    def __init__(self, id: int, name: str, career_start: int, career_end: int,
                positions: typing.List[str], height: typing.Dict[str, int],
                weight: int, born: datetime.date, college: str) -> None:
        self.id = id
        self.name = name
        self.lookup_name = name.split(" ")[0][0] + ". " + name.split(" ")[1]
        self.career_start = career_start
        self.career_end = career_end
        self.positions = positions
        self.height = height
        self.weight = weight
        self.born = born
        self.college = college
