import argparse
from retro import readers
from retro.player import Player
from retro.box_score import BoxScore
from retro.batting_line import BattingLine


def main(args):
    player_map = {p.name.lower(): p.id for p in Player.for_years([args.year])}
    player = player_map[args.name]

    if args.year < 1950:
        boxes = (BoxScore.from_box_file(e) for e in readers.box_records([args.year]))
    else:
        boxes = (BoxScore.from_events(e) for e in readers.event_records([args.year]))

    tot = BattingLine()
    for box in boxes:
        for (_home_ind, bline) in box.batting_lines:
            if bline.player != player:
                continue
            tot += bline
    print(tot)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int)
    parser.add_argument('name')
    main(parser.parse_args())
