from collections import defaultdict
import json
import dataclasses

from retro.box_score import BoxScore
from retro.batting_line import BattingLine
from retro.player import Player


def all_lines_for_year(year):
    for box in BoxScore.for_year(year):
        for _, bline in box.batting_lines:
            yield bline

def total_lines_for_year(year, min_pa=100):
    totals = defaultdict(BattingLine)
    for bline in all_lines_for_year(year):
        totals[bline.player] += bline

    return [line for line in totals.values() if line.pa > min_pa]

def main():
    out = []

    for year in range(1901, 2024):
        lines = total_lines_for_year(year, min_pa=100)
        player_map = {p.id: p.name for p in Player.for_years([year])}
        print(year, len(lines))

        out += [
            dataclasses.asdict(line) | {'year': year, 'player': player_map[line.player]}
            for line in lines
        ]

    with open('all_lines.json', 'w', encoding='utf8') as fp:
        json.dump(out, fp, indent=2)

main()
