from retro.pitching_line import PitchingLine
from retro.play_by_play import PlayByPlay

def test_from_pbp(play_by_play_lines):
    pbp = PlayByPlay.from_events(play_by_play_lines)

    assert len(pbp.plays) == len(pbp.opp_pitchers)
    assert pbp.opp_pitchers[0] == pbp.game_spec.home_starter

def test_batting_lines(play_by_play_lines):
    pbp = PlayByPlay.from_events(play_by_play_lines)

    (bline,) = [x for (home_ind, x) in pbp.batting_lines() if x.player == 'guerv002']
    assert bline.pa == 5
    assert bline.ab == 5
    assert bline.hr == 1

def test_pitching_lines(play_by_play_lines):
    pbp = PlayByPlay.from_events(play_by_play_lines)

    expected = [
        PitchingLine(player='danit001', bfp=14, h=5, bb=0, k=3),
        PitchingLine(player='germf002', bfp=6, h=2, bb=0, k=1),
        PitchingLine(player='kikuy001', bfp=14, h=1, bb=1, k=5),
        PitchingLine(player='manoa001', bfp=23, h=2, bb=2, k=4),
        PitchingLine(player='piven001', bfp=28, h=6, bb=3, k=2),
    ]


    actual = sorted([x for (home_ind, x) in pbp.pitching_lines()], key=lambda x: x.player)
    assert len(expected) == len(actual)
    for (exp, act) in zip(expected, actual):
        assert exp == act
