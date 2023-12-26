import string

from src.practice.practice_13.practice_13_1 import *


def create_fsm_number():
    language = "digit+(.digit+)?(E(+|-)?digit+)?"
    strings = [
        string.digits,
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
    fsm = create_fs_machine(language, table, states, strings, 0, [1, 3, 6])
    return fsm


def create_fsm_abb():
    language = "(a|b)+abb"
    strings = ["a", "b"]
    table = [[1, 0], [1, 2], [1, 3], [1, 0]]
    states = [0, 1, 2, 3]
    fsm = create_fs_machine(language, table, states, strings, 0, [3])
    return fsm


def main():
    fs_machines = [create_fsm_number(), create_fsm_abb()]
    print("If you want exit, enter 'Exit'")
    while True:
        input_string = input("Enter your string: ")
        if input_string == "Exit":
            break
        for fsm in fs_machines:
            if validate_string(fsm, input_string):
                print(f"Your string matches the language: {fsm.language}")


if __name__ == "__main__":
    main()
