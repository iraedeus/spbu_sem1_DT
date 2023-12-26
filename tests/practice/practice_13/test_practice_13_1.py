import pytest
from src.practice.practice_13.practice_13_1 import *
from src.homework.homework_13.homework_13_1 import *


@pytest.mark.parametrize(
    "language, table, states, strings, start_state, terminal_states",
    [("ab+", [[2, -1], [-1, 3], [-1, 3]], [1, 2], ["a", "b"], 1, [3])],
)
def test_create_fs_machine(
    language, table, states, strings, start_state, terminal_states
):
    fsm = create_fs_machine(
        language, table, states, strings, start_state, terminal_states
    )
    assert (
        fsm.language == language,
        fsm.table == Table(table=table, rows=strings, columns=states),
        fsm.current_state == start_state,
        fsm.terminal_states == terminal_states,
    )


@pytest.mark.parametrize(
    "string, expected",
    [
        ("ababb", True),
        ("abab", False),
        ("cacabb", False),
    ],
)
def test_validate_string(string, expected):
    fsm = create_fsm_abb()
    assert validate_string(fsm, string) == expected
