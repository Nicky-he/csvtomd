from csvtomd.csvtomd import pad_to, normalize_cols, pad_cells, horiz_div

import sure  # noqa


def test_pad_to():
    pad_to('word', 8).should.equal('word    ')
    pad_to('word', 2).should.equal('word')


def test_normalize_cols():
    initial = [
        ['a', 'b', 'c'],
        ['d'],
        ['e', 'f'],
    ]
    expected = [
        ['a', 'b', 'c'],
        ['d',  '',  ''],
        ['e', 'f',  ''],
    ]
    normalize_cols(initial).should.equal(expected)


def test_pad_cells():
    initial = [
        ['12345', '123',  '1'],
        [    '1', '123', '12'],
    ]
    expected = [
        ['12345', '123', '1 '],
        ['1    ', '123', '12'],
    ]
    pad_cells(initial).should.equal(expected)


def test_horiz_div():
    output = horiz_div([3, 1, 2], '-', '|', 1)
    expected = '-----|---|----'
    output.should.equal(expected)
    output = horiz_div([5, 3, 1], '.', '#', 2)
    expected = '.........#.......#.....'
    output.should.equal(expected)
