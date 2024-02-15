import dataclasses

from typing import List
from retro.game_spec import GameSpec
from retro.readers import GameLogRecord

def build_from_game_log(line: GameLogRecord):
    def line_score(s):
        ret = []
        ix = 0
        while ix < len(s):
            c = s[ix]
            if c == 'x':
                ret += [None]
                ix += 1
            elif c != '(':
                ret += [int(c)]
                ix += 1
            else:
                offset = s[ix:].index(')')
                ret += [int(s[ix+1:ix+offset])]
                ix += offset+1
        return ret 

    return GameResult(
        game_spec=GameSpec.from_game_log(line),
        away_score=int(line.away_score),
        home_score=int(line.home_score),
        duration= line.duration and int(line.duration),

        home_innings=line_score(line.home_line_score),
        away_innings=line_score(line.away_line_score),
    )


@dataclasses.dataclass
class GameResult:
    """The result of a game. Built from game logs."""
    game_spec: GameSpec

    home_score: int
    away_score: int

    home_innings: List[int]
    away_innings: List[int]

    duration: int

    @staticmethod
    def from_game_log(line: GameLogRecord):
        return build_from_game_log(line)