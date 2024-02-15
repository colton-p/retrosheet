from retro.file_readers.game_logs import GameLogRecord, game_log_records
from retro.file_readers.events import event_records, EventRecords
from retro.file_readers.box_scores import box_records, BoxRecords
from retro.file_readers.rosters import roster_records, RosterRecord


# event files
# box scores
# game logs

# event files ---> GameSpec
#             ---> PlayByPlay

#   game logs ---> GameSpec
#             ---> GameResult



# TODO:
# events            box         game logs
#   |                |             |
#   v                v             v
# PlayByPlay ...> BoxScore ...> GameResult
#
# pbp has seq of plays, subs, etc.
# TODO: build box score from pbp
# TODO: build game result from boxscore