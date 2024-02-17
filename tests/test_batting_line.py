from retro.batting_line import BattingLine

def test_from_bline(box_score_lines):
    bline = [rec for rec in box_score_lines if rec.tag == 'stat' and rec.stat_type == 'bline'][0]
    line = BattingLine.from_bline(bline)

    assert line.player == 'willd102'
    assert line.ab == 4
