from collections import Counter
import json

from retro.box_score import BoxScore
from retro.player import Player


out = []
for year in range(1901, 2024):
    print(year)
    ks = Counter()
    hrs = Counter()
    player_map = {p.id: p.name for p in Player.for_years([year])}

    for box in BoxScore.for_year(year):
        for _, pline in box.pitching_lines:
            if pline.k:
                ks[pline.player] += pline.k

        for _, bline in box.batting_lines:
            if bline.hr:
                hrs[bline.player] += bline.hr

    print(ks.most_common(10))
    print(hrs.most_common(10))
    both = set(ks) & set(hrs)
    print(len(both))
    print("--")

    out += [ {'year': year, 'player': player_map[k], 'k': ks[k], 'hr': hrs[k]} for k in both ]

json.dump(out, open('k-hr.json', 'w', encoding='utf8'), indent=2)
