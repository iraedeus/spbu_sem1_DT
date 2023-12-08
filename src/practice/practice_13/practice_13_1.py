from dataclasses import dataclass, field
from typing import Callable


@dataclass
class FSMachine:
    table: dict = field(default_factory=dict)
    functions: list[Callable] = field(default_factory=list)
    current_state: int = field(default_factory=int)
    final_states: list[int] = field(default_factory=list)


def create_fs_machine(
    table: dict, functions: list, start_state: int, final_states: list
) -> FSMachine:
    """
    In the table parameter, there should be a dict where the key is a possible state of the FSM, and the value of the key is a list with transitions to other states.\n
    The functions parameter contains a list of functions for which the DKA makes the transition.\n
    In this case, the functions and transition lists are ordered in such a way that the i-th element of the function corresponds to the i-th transition.\n
    Thus, the FSM table looks like this:\n
     # |  a  | b |...\n
    0 |  1  | 3 |...\n
    1 | -1 | 2 |...\n
    ...
    If the number -1 is in the transition list in the i-th place, then the i-th function cannot move anywhere from the current state
    """

    fsm = FSMachine()
    fsm.table = table
    fsm.functions = functions
    fsm.current_state = start_state
    fsm.final_states = final_states

    return fsm


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_index = 0
    while current_index < len(string):
        current_char = string[current_index]
        have_function = False
        for i in range(len(fsm.functions)):
            current_function = fsm.functions[i]
            if current_function(current_char):
                fsm.current_state = fsm.table[fsm.current_state][i]
                if fsm.current_state == -1:
                    return False
                have_function = True
                break

        if not have_function:
            return False

        current_index += 1

    return fsm.current_state in fsm.final_states
