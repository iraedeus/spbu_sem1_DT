import pytest
from io import StringIO
from src.homework.homework_13.homework_13_1 import *


@pytest.mark.parametrize(
    "string, expected",
    [
        ("abb", True),
        ("abab", False),
        ("ababababababababb", True),
        ("oweijfowiefoiwejfabb", False),
    ],
)
def test_check_if_abb(string, expected):
    assert check_if_abb(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("56775", True),
        ("56+45", False),
        ("56.656", True),
        ("56.45E10", True),
        ("56.56.56E100", False),
    ],
)
def test_check_if_number(string, expected):
    assert check_if_number(string) == expected


@pytest.mark.parametrize(
    "input_user, expected",
    [
        ("abb", "Your string is word of a regular expression: (a|b)+abb\n"),
        (
            "ababa",
            "Your string does not belong to either of the two regular expressions\n",
        ),
        (
            "45.45",
            "Your string is word of a regular expression: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            "45E",
            "Your string does not belong to either of the two regular expressions\n",
        ),
    ],
)
def test_main_scenario(input_user, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: input_user)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()

    assert output == expected
