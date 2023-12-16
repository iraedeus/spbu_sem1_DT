from src.practice.practice_13.practice_13_1 import *


def check_if_abb(string: str) -> bool:
    functions = [lambda x: x == "a", lambda y: y == "b"]
    table = [[1, 0], [1, 2], [1, 3], [1, 0]]
    states = [0, 1, 2, 3]
    fsm = create_fs_machine(table, states, functions, 0, [3])

    return validate_string(fsm, string)


def check_if_number(string: str) -> bool:
    functions = [
        lambda x: x.isdigit(),
        lambda x: x == ".",
        lambda x: x == "E",
        lambda x: x in "+-",
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

    fsm = create_fs_machine(table, states, functions, 0, [1, 3, 6])

    return validate_string(fsm, string)


def main():
    input_string = input("Enter your string: ")

    if check_if_number(input_string):
        print(
            "Your string is word of a regular expression: digit+(.digit+)?(E(+|-)?digit+)?"
        )
    elif check_if_abb(input_string):
        print("Your string is word of a regular expression: (a|b)+abb")
    else:
        print("Your string does not belong to either of the two regular expressions")


if __name__ == "__main__":
    main()
