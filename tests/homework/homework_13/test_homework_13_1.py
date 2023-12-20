import pytest
from unittest.mock import patch
from io import StringIO
from src.homework.homework_13.homework_13_1 import *
import builtins


@pytest.mark.parametrize(
    "input_user, expected",
    [
        ("abb", "Your string is word of a regular expression: (a|b)+abb"),
        (
            "ababa",
            "",
        ),
        (
            "45.45",
            "Your string is word of a regular expression: digit+(.digit+)?(E(+|-)?digit+)?",
        ),
        (
            "45E",
            "",
        ),
    ],
)
def test_main_scenario(input_user, expected, monkeypatch):
    inputs = [input_user, "Exit"]
    prints = []

    def mock_input(s):
        return inputs.pop(0)

    def mock_print(prints):
        return lambda s: prints.append(s)

    def mock_start_input_output(prints):
        builtins.input = mock_input
        builtins.print = mock_print(prints)

    mock_start_input_output(prints)
    main()
    assert len(prints) == 1 or prints[1] == expected
