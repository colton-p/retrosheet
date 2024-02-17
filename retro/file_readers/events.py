from collections import namedtuple
import csv
import glob
import itertools


class EventRecords:
    Info = namedtuple('Info', ['tag', 'field', 'value'])
    Id = namedtuple('Id', ['tag', 'id'])
    Start = namedtuple('Start', ['tag', 'player', 'name', 'home_ind', 'order', 'position'])
    Sub = namedtuple('Sub', ['tag', 'player', 'name', 'home_ind', 'order', 'position'])
    Play = namedtuple(
        'Play', ['tag', 'inning', 'home_ind', 'player', 'count', 'pitch_seq', 'event']
    )
    Event = Info | Id | Start | Sub | Play

def build_event_record(line) -> EventRecords.Event | None:
    (tag, *_rest) = line
    types = {
        'id': EventRecords.Id,
        'info': EventRecords.Info,
        'start': EventRecords.Start,
        'sub': EventRecords.Sub,
        'play': EventRecords.Play,
    }
    if tag not in types: return None

    return types[tag](*line[:len(types[tag]._fields)])

def _ungrouped_event_records(years):
    patterns = [f"data/events/{year}*.EV[AN]" for year in years]

    for pattern in patterns:
        for path in sorted(glob.glob(pattern)):
            with open(path, encoding="utf8") as gl:
                reader = csv.reader(gl)
                for line in reader:
                    rec = build_event_record(line)
                    if rec:
                        yield rec

def event_records(years=None):
    def keyed_games(rec_iter):
        game_id = None
        for rec in rec_iter:
            if rec.tag == 'id':
                game_id = rec.id
            yield (game_id, rec)

    rec_iter = _ungrouped_event_records(years=years)
    it = itertools.groupby(keyed_games(rec_iter), key=lambda x: x[0])
    for (_key, game_iter) in it:
        yield [record for (_, record) in game_iter]
