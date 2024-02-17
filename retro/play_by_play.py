from collections import Counter, defaultdict
import dataclasses
from typing import List

from retro.batting_line import BattingLine
from retro.game_spec import GameSpec
from retro.play import Play
from retro.pitching_line import PitchingLine
from retro.readers import EventRecords

def _build_from_events(records: List[EventRecords.Event]):
    # TODO: --> PbPParser class
    # produce (game_state, play) pairs
    # state + play -> state'
    spec = GameSpec.from_events(records)

    plays = []
    pitchers = []
    opp_pitcher = {
        '0': spec.home_starter,
        '1': spec.away_starter
    }

    for rec in records:
        if rec.tag == 'play':
            plays += [Play.from_play_line(rec)]
            pitchers += [opp_pitcher[rec.home_ind]]
        elif rec.tag == 'sub':
            if rec.position != '1': continue
            opp_pitcher[str(1-int(rec.home_ind))] = rec.player

    return PlayByPlay(spec, plays, pitchers)


@dataclasses.dataclass
class PlayByPlay:
    game_spec: GameSpec
    plays: List[Play]
    opp_pitchers: List[str]

    @staticmethod
    def from_events(lines):
        return _build_from_events(lines)

    def batting_lines(self):
        by_player = defaultdict(list)
        for play in self.plays:
            by_player[play.player] += [play]
        return [
            (plays[0].home_ind, BattingLine.from_plays(plays))
            for plays in by_player.values()
        ]

    def pitching_lines(self):
        plines = defaultdict(Counter)
        for (play, pitcher) in zip(self.plays, self.opp_pitchers):
            plines[(str(1-int(play.home_ind)), pitcher)] += Counter({
                'bfp': 1,
                'h': int(bool(play.h)),
                'bb': int(bool(play.bb)),
                'k': int(bool(play.k)),
            })

        return [
            (home_ind, PitchingLine(player=pitcher, **stats))
            for ((home_ind, pitcher), stats) in plines.items()
        ]
