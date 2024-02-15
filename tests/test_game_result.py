from retro.game_result import GameResult


def test_from_game_log(game_log_record):
    game = GameResult.from_game_log(game_log_record)

    assert game.game_spec.id == 'TOR202209300'
    assert game.home_score == 9
    assert game.away_score == 0

    assert game.home_innings == [1, 1, 2, 0, 0, 4, 0, 1, None]
    assert game.away_innings == [0 for _ in range(9)]


def test_from_game_log2(game_log_record2):
    game = GameResult.from_game_log(game_log_record2)
    assert game.home_score == 5
    assert game.away_score == 28

    assert game.away_innings == [1, 2, 7, 4, 11, 2, 0, 0, 1]
    assert game.home_innings == [0, 0, 0, 3, 0, 1, 1, 0, 0]