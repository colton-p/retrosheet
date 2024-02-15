import dataclasses
from collections import Counter
from typing import List

from retro.play import Play
from retro.readers import BoxRecords


def build_from_bline(rec: BoxRecords.Bline):
    #(stat,bline,id,side,_pos,_seq,*stats) = line
    #(ab,_r,h,double,triple,hr,_rbi,_sh,sf,hbp,bb,_ibb,k,_sb,_cs,_gidp,_int) = map(int, stats)
    assert rec.tag == 'stat'
    assert rec.stat_type == 'bline'
    assert rec.home_ind in ['0','1']

    pa_fields = (rec.ab,rec.hbp,rec.bb,rec.sh,rec.sf,rec.interference)
    return BattingLine(
        player=rec.player,
        pa=sum(int(v) for v in pa_fields),
        ab=int(rec.ab),
        h=int(rec.h),
        double=int(rec.double),
        triple=int(rec.triple),
        hr=int(rec.hr),
        hbp=int(rec.hbp),
        bb=int(rec.bb),
        k=int(rec.k),
        sf=int(rec.sf),
    )


@dataclasses.dataclass
class BattingLine:
    player: str = ''
    pa: int = 0
    ab: int = 0
    h: int = 0
    double: int = 0
    hr: int = 0
    triple: int = 0
    hbp: int = 0
    k: int = 0
    bb: int = 0
    sf: int = 0

    @staticmethod
    def from_plays(plays: List[Play]):
        attrs = ['hbp', 'ab', 'h', 'double', 'triple', 'hr', 'k', 'bb', 'sf']
        c = sum((
            Counter({attr: int(bool(getattr(p, attr))) for attr in attrs})
            for p in plays), Counter({a: 0 for a in attrs})
        )
        return BattingLine(player=plays[0].player, pa=len(plays), **c)
    
    @staticmethod
    def from_play(_play: Play):
        ...
    
    @staticmethod
    def from_bline(line: BoxRecords.Bline):
        return build_from_bline(line)
    
    @property
    def avg(self):
        if self.ab == 0: return 0
        return self.h / self.ab

    @property
    def obp(self):
        return (self.hbp + self.bb + self.h) / self.pa
    
    @property
    def slg(self):
        return self.tb / self.ab

    @property
    def tb(self):
        return (self.h + self.double + 2*self.triple + 3*self.hr)
    
    def __add__(self, other):
        if self.player and other.player:
            assert self.player == other.player, (self, other)
        a = dataclasses.asdict(self)
        b = dataclasses.asdict(other)

        player = self.player or other.player
        return BattingLine(
            player=player,
            **{k: a.get(k,0) + b.get(k, 0) for k in a.keys() if k != 'player'}
        )