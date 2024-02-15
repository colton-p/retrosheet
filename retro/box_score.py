import dataclasses
from typing import List, Tuple

from retro.game_spec import GameSpec
from retro.play_by_play import PlayByPlay
from retro.batting_line import BattingLine
from retro.pitching_line import PitchingLine

from retro.readers import EventRecords, box_records, event_records

@dataclasses.dataclass
class BoxScore:
    game_spec: GameSpec
    batting_lines: List[Tuple[int, BattingLine]]
    pitching_lines: List[Tuple[int, BattingLine]]

    @staticmethod
    def for_year(year):
        if year < 1950:
            return (BoxScore.from_box_file(e) for e in box_records([year]))
        return (BoxScore.from_events(e) for e in event_records([year]))

    @staticmethod
    def from_box_file(lines):
        spec = GameSpec.from_events(lines)
        blines = [(rec.home_ind, BattingLine.from_bline(rec)) for rec in lines if rec.tag == 'stat' and rec.stat_type == 'bline']
        plines = [(rec.home_ind, PitchingLine.from_pline(rec)) for rec in lines if rec.tag == 'stat' and rec.stat_type == 'pline']
        return BoxScore(spec, blines, plines)

    @staticmethod
    def from_events(lines: List[EventRecords.Event]):
        pbp = PlayByPlay.from_events(lines)
        return BoxScore(
            pbp.game_spec,
            pbp.batting_lines(),
            pbp.pitching_lines(),
        )
