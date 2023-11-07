import pytest
from src.homework.homework_8.homework_8_2 import *


@pytest.mark.parametrize(
    "string, expected",
    [
        ("aaabbccooeeeeeee", "a3b2c2o2e7"),
        ("abcde", "a1b1c1d1e1"),
        ("abcabccccabc", "a1b1c1a1b1c4a1b1c1"),
    ],
)
def test_encode(string, expected):
    assert encode(string) == expected


@pytest.mark.parametrize("string", [("1abcdebc"), ("&%$bb")])
def test_encode_exception(string):
    with pytest.raises(ValueError):
        encode(string)


@pytest.mark.parametrize(
    "string, expected",
    [("abcd", False), ("a4b7m782", True), ("3b4", False), ("v5n3m277p", False)],
)
def test_is_valid(string, expected):
    assert is_valid(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [("a2v2b2", "aavvbb"), ("a5a2g8", "aaaaaaagggggggg"), ("l1r9", "lrrrrrrrrr")],
)
def test_decode(string, expected):
    assert decode(string) == expected


@pytest.mark.parametrize("string", [("4b7a9k1"), ("abcbb5"), ("a6v2n")])
def test_decode_exception(string):
    with pytest.raises(ValueError):
        decode(string)
