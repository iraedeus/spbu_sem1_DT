import os
import sys
import collections
import string


def check_files(path_input, path_output):
    if not os.path.exists(path_input):
        raise FileNotFoundError("The input file doesnt exists")
    if os.path.exists(path_output):
        raise FileExistsError("The output file is already exists")


def delete_not_letters(counter):
    output_dict = {}
    for i in string.ascii_letters:
        if i in counter:
            output_dict[i] = counter[i]
    return dict(sorted(output_dict.items()))


def get_count_chars(file_input):
    counter = collections.Counter()
    with open(file_input, "r") as file:
        for item in file:
            counter.update(item)
    return delete_not_letters(counter)


def write_to_output(file_output, counter):
    with open(file_output, "w") as file:
        for i in counter:
            file.write(f"{i}: {counter[i]}\n")


def main():
    file_input = sys.argv[2]
    file_output = sys.argv[3]

    try:
        check_files(file_input, file_output)
        counter = get_count_chars(file_input)
        write_to_output(file_output, counter)
    except FileExistsError as error:
        print(error)
    except FileNotFoundError as error:
        print(error)


if __name__ == "__main__":
    main()
