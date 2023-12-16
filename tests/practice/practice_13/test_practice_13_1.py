import pytest
from src.practice.practice_13.practice_13_1 import *


@pytest.mark.parametrize(
    "table, states, functions, start_state, final_states, string, expected",
    [
        (
            [[1, 0], [1, 2], [1, 3], [1, 0]],
            [0, 1, 2, 3],
            [lambda x: x == "a", lambda y: y == "b"],
            0,
            [3],
            "ababb",
            True,
        ),
        (
            [[1, 0], [1, 2], [1, 3], [1, 0]],
            [0, 1, 2, 3],
            [lambda x: x == "a", lambda y: y == "b"],
            0,
            [3],
            "abab",
            False,
        ),
        (
            [[1, 0], [1, 2], [1, 3], [1, 0]],
            [0, 1, 2, 3],
            [lambda x: x == "a", lambda y: y == "b"],
            0,
            [3],
            "cacabb",
            False,
        ),
    ],
)
def test_validate_string(
    table, states, functions, start_state, final_states, string, expected
):
    fsm = create_fs_machine(table, states, functions, start_state, final_states)
    assert validate_string(fsm, string) == expected
