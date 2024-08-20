import pytest
from unittest.mock import patch
from io import StringIO
from src.homework.homework_7.re_checker import *
import builtins


@pytest.mark.parametrize(
    "input_user, expected",
    [
        (["abb", "Exit"], "Your string matches the language: (a|b)+abb\n"),
        (
            ["ababa", "Exit"],
            "",
        ),
        (
            ["45.45", "Exit"],
            "Your string matches the language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            ["45E", "Exit"],
            "",
        ),
    ],
)
def test_main_scenario(input_user, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: input_user.pop(0))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output.lstrip("If you want exit, enter 'Exit'\n") == expected
