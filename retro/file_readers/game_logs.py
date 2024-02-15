import csv

from collections import namedtuple
# https://www.retrosheet.org/gamelogs/glfields.txt
GameLogRecord = namedtuple(
    "GameLogRecord",
    [
        "date",
        "number",
        "away_team",
        "home_team",
        "away_score",
        "home_score",
        "site",
        "attendance",
        "duration",
        "away_line_score",
        "home_line_score",
        "winning_pitcher",
        "losing_pitcher",
        "save",
        'away_starter',
        'home_starter',
    ] +
    [f'away_lineup_{ix}_id' for ix in range(1, 10)] +
    [f'away_lineup_{ix}_pos' for ix in range(1, 10)] +
    [f'home_lineup_{ix}_id' for ix in range(1, 10)] +
    [f'home_lineup_{ix}_pos' for ix in range(1, 10)]
)

def build_game_log_record(line):
    glr = ({
        "date": 1, "number": 2, "away_team": 4, "home_team": 7,
        "away_score": 10, "home_score": 11, "site": 17, "attendance": 18,
        "duration": 19, "away_line_score": 20, "home_line_score": 21,
        "winning_pitcher": 94, "losing_pitcher": 96, "save": 98,
        'away_starter': 102, 'home_starter': 104,
    } |
        {f'away_lineup_{ix+1}_id': 106 + 3*ix for ix in range(9)} |
        {f'away_lineup_{ix+1}_pos': 108 + 3*ix for ix in range(9)} |
        {f'home_lineup_{ix+1}_id': 133 + 3*ix for ix in range(9)} |
        {f'home_lineup_{ix+1}_pos': 135 + 3*ix for ix in range(9)}
    )

    attrs = {field: line[index - 1] for (field, index) in glr.items()}
    return GameLogRecord(**attrs)


def game_log_records(years=None):
    """GameLogRecords for the given years"""

    if isinstance(years, list):
        paths = [f"data/gamelogs/gl{year}.txt" for year in years]
    else:
        paths = [f"data/gamelogs/gl{years}.txt"]

    for path in paths:
        with open(path, encoding="utf8") as gl:
            reader = csv.reader(gl)
            for line in reader:
                yield build_game_log_record(line)
