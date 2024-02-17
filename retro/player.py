
import dataclasses
import retro.readers as readers

def players_for_year(year):
    def player_from_roster(rec: readers.RosterRecord):
        return Player(
            id=rec.player,
            first=rec.first_name,
            last=rec.last_name,
            bats=rec.bats,
            throws=rec.throws,
            position=rec.position,
        )

    seen = set()
    for rec in readers.roster_records(years=year):
        if rec.player not in seen:
            seen.add(rec.player)
            yield player_from_roster(rec)


@dataclasses.dataclass(frozen=True)
class Player:
    id: str
    first: str
    last: str
    bats: str
    throws: str
    position: str

    @staticmethod
    def for_years(years):
        return players_for_year(years)

    @property
    def name(self):
        return f'{self.first} {self.last}'
