from dataclasses import dataclass, field


@dataclass
class Table:
    rows: list[str]
    columns: list[int]
    table: list[list[int]]


@dataclass
class FSMachine:
    language: str
    table: Table
    current_state: int
    terminal_states: list[int] = field(default_factory=list)


def create_fs_machine(
    language: str,
    table: list[list],
    states: list,
    functions: list,
    start_state: int,
    terminal_states: list,
) -> FSMachine:
    table = Table(table=table, columns=functions, rows=states)
    fsm = FSMachine(
        language=language,
        table=table,
        current_state=start_state,
        terminal_states=terminal_states,
    )
    return fsm


def validate_string(fsm: FSMachine, string: str) -> bool:
    table = fsm.table
    for char in string:
        for i in range(len(table.columns)):
            if char in table.columns[i] and table.table[fsm.current_state][i] != -1:
                fsm.current_state = table.table[fsm.current_state][i]
                break
        else:
            return False

    return fsm.current_state in fsm.terminal_states
