import pytest
from io import StringIO
from src.homework.homework_8.homework_8_1 import *


@pytest.mark.parametrize(
    "char, expected", [("A", "U+0041"), ("Æ", "U+00C6"), ("흔", "U+D754")]
)
def test_to_unicode_char(char, expected):
    assert to_unicode_char(char) == expected


@pytest.mark.parametrize(
    "char, expected",
    [
        ("ﺻ", "11111110 10111011"),
        ("𐍇", "11011000 00000000 11011111 01000111"),
        ("𐏊", "11011000 00000000 11011111 11001010"),
    ],
)
def test_to_utf16(char, expected):
    assert to_utf16(char) == expected


@pytest.mark.parametrize(
    "input_user, expected",
    [
        (
            "Hi",
            "H    U+0048    00000000 01001000\ni    U+0069    00000000 01101001\n\n",
        ),
        (
            "我爱一只猫",
            "我    U+6211    01100010 00010001\n爱    U+7231    01110010 00110001\n一    U+4E00    01001110 00000000\n只    U+53EA    01010011 11101010\n猫    U+732B    01110011 00101011\n\n",
        ),
    ],
)
def test_main(monkeypatch, input_user, expected):
    monkeypatch.setattr("builtins.input", lambda _: input_user)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
