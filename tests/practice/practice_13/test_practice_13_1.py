import pytest
from src.practice.practice_13.practice_13_1 import *


@pytest.mark.parametrize(
    "table, functions, start_state, final_states, string, expected",
    [
        (
            {0: [1, 0], 1: [1, 2], 2: [1, 3], 3: [1, 0]},
            [lambda x: x == "a", lambda y: y == "b"],
            0,
            [3],
            "ababb",
            True,
        ),
        (
            {0: [1, 0], 1: [1, 2], 2: [1, 3], 3: [1, 0]},
            [lambda x: x == "a", lambda y: y == "b"],
            0,
            [3],
            "abab",
            False,
        ),
        (
            {0: [1, 0], 1: [1, 2], 2: [1, 3], 3: [1, 0]},
            [lambda x: x == "a", lambda y: y == "b"],
            0,
            [3],
            "cacabb",
            False,
        ),
    ],
)
def test_validate_string(table, functions, start_state, final_states, string, expected):
    fsm = create_fs_machine(table, functions, start_state, final_states)
    assert validate_string(fsm, string) == expected
