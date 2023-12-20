from src.practice.practice_13.practice_13_1 import *


def create_fsm_number():
    strings = [
        "0123456789",
        ".",
        "E",
        "+-",
    ]
    table = [
        [1, -1, -1, -1],
        [1, 2, 4, -1],
        [3, -1, -1, -1],
        [3, -1, 4, -1],
        [6, -1, -1, 5],
        [6, -1, -1, -1],
        [6, -1, -1, -1],
    ]
    states = [0, 1, 2, 3, 4, 5, 6]
    fsm = create_fs_machine(table, states, strings, 0, [1, 3, 6])
    return fsm


def create_fsm_abb():
    strings = ["a", "b"]
    table = [[1, 0], [1, 2], [1, 3], [1, 0]]
    states = [0, 1, 2, 3]
    fsm = create_fs_machine(table, states, strings, 0, [3])
    return fsm


def print_if_abb(fsm: FSMachine, string: str):
    if validate_string(fsm, string):
        print("Your string is word of a regular expression: (a|b)+abb")


def print_if_number(fsm: FSMachine, string: str):
    if validate_string(fsm, string):
        print(
            "Your string is word of a regular expression: digit+(.digit+)?(E(+|-)?digit+)?"
        )


def main():
    fsm_number = create_fsm_number()
    fsm_abb = create_fsm_abb()
    print("If you want exit, enter 'Exit'")
    while True:
        input_string = input("Enter your string: ")
        if input_string == "Exit":
            break
        print_if_number(fsm_number, input_string)
        print_if_abb(fsm_abb, input_string)


if __name__ == "__main__":
    main()
