import sys
import os


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None


def find_file_output(name, path):
    if find_file(name, path) is None:
        file = open(name, "w+")
    return find_file(name, path)


def get_numbers(input_file, list_less, list_between, list_greater, a, b):
    with open(input_file, "r") as file:
        for i in file.readline().split(" "):
            if int(i) < a:
                list_less.append(i)
            elif a <= int(i) <= b:
                list_between.append(i)
            else:
                list_greater.append(i)


def write_to_file(output_file, list_less, list_between, list_greater):
    with open(output_file, "w") as file:
        file.write(" ".join(list_less) + "\n")
        file.write(" ".join(list_between) + "\n")
        file.write(" ".join(list_greater) + "\n")


if __name__ == "__main__":
    args = sys.argv[1:]
    a, b = int(args[0]), int(args[1])
    input_file = find_file(args[2], "/")

    if find_file(args[3], "/") is None:
        print("Can't find file")
    else:
        output_file = find_file_output(args[3], "/")

        list_less, list_between, list_greater = [], [], []

        get_numbers(input_file, list_less, list_between, list_greater, a, b)
        write_to_file(output_file, list_less, list_between, list_greater)
