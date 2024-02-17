import dataclasses
import datetime
from typing import List

from retro.readers import GameLogRecord, game_log_records, EventRecords

def _build_from_game_log(rec: GameLogRecord):
    def _build_lineup(side):
        lineup_ids = [getattr(rec, f'{side}_lineup_{ix}_id') for ix in range(1, 10)]
        lineup_names = [getattr(rec, f'{side}_lineup_{ix}_name') for ix in range(1, 10)]
        lineup_pos = [getattr(rec, f'{side}_lineup_{ix}_pos') for ix in range(1, 10)]
        if any(x == '' for x in lineup_ids):
            return []
        return [
            LineupSlot(player, name, ix + 1, int(position or -1))
            for (ix, (player, name, position)) in
            enumerate(zip(lineup_ids, lineup_names, lineup_pos))
        ]

    return GameSpec(
        home_team=rec.home_team,
        away_team=rec.away_team,
        site=rec.site,
        attendance=int(rec.attendance or '0'),
        number=rec.number,
        date=datetime.datetime.strptime(rec.date, '%Y%m%d'),
        winning_pitcher=rec.winning_pitcher,
        losing_pitcher=rec.losing_pitcher,
        save=rec.save,

        away_lineup=_build_lineup('away'),
        home_lineup=_build_lineup('home'),
        home_starter=rec.home_starter,
        away_starter=rec.away_starter,
    )

def _build_from_events(records: List[EventRecords.Event]):
    info = {
        rec.field: rec.value for rec in records if rec.tag == 'info'
    }
    start_lines = [rec for rec in records if rec.tag == 'start']

    lineups = {}
    for ind in '01':
        lineups[ind] = [
            LineupSlot(rec.player, rec.name, int(rec.order), int(rec.position))
            for rec in start_lines
            if rec.order in '123456789' and rec.home_ind == ind
        ]
    (home_starter,) = [ rec.player
            for rec in start_lines
            if rec.home_ind == '1' and rec.position == '1'
    ]
    (away_starter,) = [ rec.player
            for rec in start_lines
            if rec.home_ind == '0' and rec.position == '1'
    ]
    return GameSpec(
        home_team=info['hometeam'],
        away_team=info['visteam'],
        site=info.get('site', ''),
        attendance=int(info['attendance'] or 0),
        number=info['number'],
        date=datetime.datetime.strptime(info['date'], '%Y/%m/%d'),
        winning_pitcher=info['wp'],
        losing_pitcher=info['lp'],
        save=info['save'],
        away_lineup=lineups['0'],
        home_lineup=lineups['1'],
        home_starter=home_starter,
        away_starter=away_starter,
    )


@dataclasses.dataclass(frozen=True)
class LineupSlot:
    """A player in a batting order"""
    player: str
    name: str
    order: int
    position: int

@dataclasses.dataclass(frozen=True)
class GameSpec:
    """A specification of a game, but not the result. Built from either game logs or events."""
    home_team: str
    away_team: str
    site: str
    attendance: int
    date: datetime.date
    number: str

    winning_pitcher: str
    losing_pitcher: str
    save: str

    home_lineup: list[LineupSlot]
    away_lineup: list[LineupSlot]

    home_starter: str
    away_starter: str

    @property
    def id(self):
        return f'{self.home_team}{self.date.strftime("%Y%m%d")}{self.number}'

    @staticmethod
    def for_years(years):
        return (_build_from_game_log(gl) for gl in game_log_records(years=years))

    @staticmethod
    def from_events(lines: List[EventRecords.Event]):
        return _build_from_events(lines)

    @staticmethod
    def from_game_log(line: GameLogRecord):
        return _build_from_game_log(line)
