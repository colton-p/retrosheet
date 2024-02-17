import dataclasses
import re

from retro.readers import EventRecords


@dataclasses.dataclass(frozen=True)
class Play:
    game_id: str
    inning: int
    home_ind: int
    player: str
    final_count: str
    pitch_seq: str
    outcome: str
    modifier: str
    advances: str

    @staticmethod
    def is_non_batting_play(line):
        non_bat = ["CS", "SB", "PO", "NP", "BK", "DI", "OA", "PB", "WP"]
        return any(line[-1].startswith(x) for x in non_bat)

    @staticmethod
    def from_play_line(rec: EventRecords.Play):
        assert rec.tag == "play"

        pat = r"([^/\\.]+)(/[^\\.]+)*(\\..+)?"
        m = re.match(pat, rec.event)
        if not m:
            assert False, rec.event
        (outcome, modifier, advances) = m.groups()

        outcome = outcome.replace("!", "").replace("#", "")

        return Play(
            "",
            int(rec.inning),
            int(rec.home_ind),
            rec.player,
            rec.count,
            rec.pitch_seq,
            outcome,
            modifier,
            advances,
        )

    def classify(self):
        attrs = [
            "reach_on_error",
            "h",
            "bb",
            "k",
            "hbp",
            "bip_out",
            "fc",
            "fle",
            "catchers_int",
        ]

        return [prop for prop in attrs if getattr(self, prop)]

    @property
    def bb(self):
        return self.outcome == "W" or self.outcome.startswith("W+") or self.ibb

    @property
    def ibb(self):
        return self.outcome == "IW"

    @property
    def h(self):
        return any((self.single, self.double, self.triple, self.hr))

    @property
    def single(self):
        return re.match(r"S\d*$", self.outcome)

    @property
    def double(self):
        # return self.outcome == 'DGR' or re.match(r'D\d*$', self.outcome)
        return re.fullmatch("D(GR)?[1-9]{0,3}", self.outcome)

    @property
    def triple(self):
        return re.match(r"T\d*$", self.outcome)

    @property
    def reach_on_error(self):
        return re.fullmatch(r"[1-9]{0,3}E[1-9]", self.outcome)

    @property
    def fc(self):
        return re.match(r"FC[1-9]{0,1}$", self.outcome)

    @property
    def catchers_int(self):
        return self.outcome == "C"

    @property
    def hr(self):
        return re.fullmatch(r"HR[1-9]{0,2}", self.outcome)

    @property
    def k(self):
        return re.fullmatch(r"K[1-9]{0,4}", self.outcome) or self.outcome.startswith(
            "K+"
        )

    @property
    def hbp(self):
        return self.outcome == "HP"

    @property
    def bip_out(self):
        patterns = [
            r"[1-9]{1,6}",
            # $(%) $(%)$(%) $(%)$(%)$(%)
            # $(%)$ $(%)$(%)$ $(%)$(%)$(%)$
            r"([1-9]{1,6}\([123HB]\)){0,3}[1-9]{0,2}",
        ]
        return any(re.fullmatch(pat, self.outcome) for pat in patterns)

    @property
    def fle(self):
        return re.fullmatch(r"FLE[1-9]", self.outcome)

    @property
    def sf(self):
        return self.modifier and "SF" in self.modifier

    @property
    def sh(self):
        return self.modifier and "SH" in self.modifier

    @property
    def ab(self):
        if self.sf or self.sh:
            return False
        return self.h or self.bip_out or self.k or self.reach_on_error or self.fc
