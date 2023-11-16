from pytest import mark

from messages import show_count

@mark.parametrize('qty, word, expected', [
    (1, 'part', '1 part'),
    (2, 'part', '2 parts'),
])

def test_show_count(qty: int, word: str, expected: str) -> None:
    got = show_count(qty, word)
    assert got == expected

def test_show_zero() -> None:
    got = show_count(0, 'part')
    assert got == 'no parts'

def test_irregular() -> None:
    got = show_count(3, 'child', 'children')
    assert got == '3 children'