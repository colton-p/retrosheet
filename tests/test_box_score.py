from retro.box_score import BoxScore

def test_from_box_file(box_score_lines):
    box = BoxScore.from_box_file(box_score_lines)

    assert box.game_spec.id == 'CHN195505140'
    (bline,) = [x for (home_ind, x) in box.batting_lines if x.player == 'banke101']
    assert bline.pa == 4
    assert bline.ab == 2
    assert bline.bb == 2

    (pline,) = [x for (home_ind, x) in box.pitching_lines if x.player == 'rushb101']
    assert pline.bfp == 33
    assert pline.h == 7
    assert pline.bb == 2
    assert pline.k == 2


def test_from_event_file(play_by_play_lines):
    box = BoxScore.from_events(play_by_play_lines)

    assert box.game_spec.id == 'TOR202209300'

    (bline,) = [x for (home_ind, x) in box.batting_lines if x.player == 'guerv002']
    assert bline.pa == 5
    assert bline.ab == 5
    assert bline.hr == 1
