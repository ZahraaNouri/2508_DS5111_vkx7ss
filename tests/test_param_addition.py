import pytest
import os


## TEXT BOOK EXAMPLE OF PARAMETRIZED TESTS
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
        (2, 2, 4),
        (333, 999, 1332),
        (0, 0, 0),
        (-5, -7, -12)
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected



## EXTENDED EXAMPLE TO SCALE WITH FILES
tfiles = [name for name in os.listdir('test_files') if name.endswith(".txt")]
cases = []
for fname in tfiles:
    text = open(f'test_files/{fname}').read()
    a, b, expected = text.split()
    cases.append( (int(a.strip()), int(b.strip()), int(expected.strip())) )


@pytest.mark.parametrize("a,b,expected", cases)
def test_addition_files(a, b, expected):
    assert a + b == expected
