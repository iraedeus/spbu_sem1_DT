from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Table:
    rows: list
    columns: list
    table: list[list]


@dataclass
class FSMachine:
    table: Table
    current_state: int = field(default_factory=int)
    final_states: list[int] = field(default_factory=list)


def create_fs_machine(
    table: list[list],
    states: list,
    functions: list,
    start_state: int,
    final_states: list,
) -> FSMachine:
    table = Table(table=table, columns=functions, rows=states)

    fsm = FSMachine(table=table)
    fsm.current_state = start_state
    fsm.final_states = final_states

    return fsm


def validate_string(fsm: FSMachine, string: str) -> bool:
    table = fsm.table
    for char in string:
        have_function = False
        for i in range(len(table.columns)):
            if table.columns[i](char) and table.table[fsm.current_state][i] != -1:
                fsm.current_state = table.table[fsm.current_state][i]
                have_function = True
                break

        if not have_function:
            return False

    return fsm.current_state in fsm.final_states
