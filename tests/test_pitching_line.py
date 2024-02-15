from retro.pitching_line import PitchingLine


def test_from_pline(box_score_lines):
    plines = [line for line in box_score_lines if line.tag == 'stat' and line.stat_type == 'pline']
    line = PitchingLine.from_pline(plines[-1])

    assert line.player == 'rushb101'
    assert line.bfp == 33
    assert line.h == 7
    assert line.bb == 2
    assert line.k == 2