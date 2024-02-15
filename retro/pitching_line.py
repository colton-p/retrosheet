import dataclasses

from retro.readers import BoxRecords

def build_from_pline(rec: BoxRecords.Pline):
    assert rec.tag == 'stat'
    assert rec.stat_type == 'pline'
    assert rec.home_ind in ['0','1']

    return PitchingLine(
        player=rec.player,
        bfp=int(rec.bfp),
        h=int(rec.h),
        bb=int(rec.bb),
        k=int(rec.k),
    )


@dataclasses.dataclass
class PitchingLine:
    player: str = ''
    bfp: int = 0
    h: int = 0
    bb: int = 0
    k: int = 0

    @staticmethod
    def from_pline(line: BoxRecords.Pline):
        return build_from_pline(line)
    
    def __add__(self, other):
        assert self.player == other.player, (self, other)
        a = dataclasses.asdict(self)
        b = dataclasses.asdict(other)

        return PitchingLine(
            player=self.player,
            **{k: a.get(k,0) + b.get(k, 0) for k in a.keys() if k != 'player'}
        )