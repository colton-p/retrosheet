from collections import namedtuple
import csv
import glob

RosterRecord = namedtuple('RosterRecord', [
    'player',
    'last_name',
    'first_name',
    'bats',
    'throws',
    'team',
    'position'
])

def build_roster_record(line):
    return RosterRecord(*line)

def roster_records(years):
    patterns = [f"data/rosters/*{year}.ROS" for year in years]

    for pattern in patterns:
        for path in sorted(glob.glob(pattern)):
            with open(path, encoding="utf8") as gl:
                reader = csv.reader(gl)
                for line in reader:
                    rec = build_roster_record(line)
                    if rec:
                        yield rec