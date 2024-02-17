from collections import namedtuple
import csv
import glob
import itertools

from retro.file_readers.events import EventRecords

# https://www.retrosheet.org/boxfile.txt
class BoxRecords:
    Id = EventRecords.Id
    Info = EventRecords.Info
    Start = EventRecords.Start
    Sub = EventRecords.Sub

    Bline = namedtuple('Bline', [
        'tag','stat_type','player','home_ind','pos','seq','ab','r','h','double','triple',
        'hr','rbi','sh','sf','hbp','bb','ibb','k','sb','cs','gidp','interference'])
    Pline = namedtuple('Pline', [
        'tag', 'stat_type','player','home_ind', 'seq','ipx3','no_out','bfp','h','h2b','h3b',
        'hr','r','er','bb','ibb','k','hbp','wp','balk','sh','sf'])

    Box = Id | Info | Start | Sub | Bline | Pline

def build_box_record(line: BoxRecords.Box):
    (tag, *_rest) = line
    types = {
        'id': EventRecords.Id,
        'info': EventRecords.Info,
        'start': EventRecords.Start,
        'sub': EventRecords.Sub,
    }
    if tag in types:
        return types[tag](*line[:len(types[tag]._fields)])

    if tag == 'stat':
        (tag, stat_type, *_rest) = line
        if stat_type == 'bline':
            return BoxRecords.Bline(*line)
        if stat_type == 'pline':
            return BoxRecords.Pline(*line)

    return None

def _ungrouped_box_records(years):
    patterns = [f"data/boxes/{year}.EB[AN]" for year in years]

    for pattern in patterns:
        for path in sorted(glob.glob(pattern)):
            with open(path, encoding="utf8") as gl:
                reader = csv.reader(gl)
                for line in reader:
                    rec = build_box_record(line)
                    if rec:
                        yield rec

def box_records(years=None):
    def keyed_games(rec_iter):
        game_id = None
        for rec in rec_iter:
            if rec.tag == 'id':
                game_id = rec.id
            yield (game_id, rec)

    rec_iter = _ungrouped_box_records(years=years)
    it = itertools.groupby(keyed_games(rec_iter), key=lambda x: x[0])
    for (_key, game_iter) in it:
        yield [record for (_, record) in game_iter]
