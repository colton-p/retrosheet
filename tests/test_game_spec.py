from retro.game_spec import GameSpec


def test_ok():
    assert GameSpec

def test_from_game_log(game_log_record):

    game = GameSpec.from_game_log(game_log_record)

    assert game.id == 'TOR202209300'
    assert game.home_lineup[0].player == 'sprig001'
    assert game.home_lineup[0].position == 8
    assert game.attendance == 37283

def test_from_play_by_play(play_by_play_lines):
    print(play_by_play_lines[0])
    game = GameSpec.from_events(play_by_play_lines)

    assert game.id == 'TOR202209300'
    assert game.home_lineup[0].player == 'sprig001'
    assert game.home_lineup[0].position == 8
    assert game.attendance == 37283
