from src.homework.homework_5.avl_tree import *
import argparse
import os


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    parser.add_argument("-l", "--logs", default="shop_logs.txt")
    parser.add_argument("-o", "--output", default="output_logs.txt")
    parser.add_argument("-r", "--remains", default="storage_remains.txt")

    return parser.parse_args()


def add(storage: TreeMap, size: int, count: int):
    node = get_tree_node(storage, size)
    if node is None:
        put(storage, size, count)
    else:
        node.value += count


def get_size(storage: TreeMap, size: int) -> int:
    node = get_tree_node(storage, size)
    if node is not None:
        return node.value
    return 0


def select(storage: TreeMap, size: int):
    if storage.root is None:
        return "SORRY"

    key = get_lower_bound(storage, size)

    node = get_tree_node(storage, key)

    if node is not None:
        node.value -= 1
        chosen_size = node.key
        if node.value == 0:
            remove(storage, key)

        return chosen_size
    else:
        return "SORRY"


def find_log(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None


def write_result_command(storage, instruction, file):
    command = instruction[0]
    if command == "ADD":
        size = int(instruction[1])
        count = int(instruction[2])
        add(storage, size, count)
    elif command == "GET":
        size = int(instruction[1])
        count = get_size(storage, size)
        file.write(str(count) + "\n")
    elif command == "SELECT":
        chosen_size = select(storage, int(instruction[1]))
        file.write(str(chosen_size) + "\n")


def write_result(storage, file_path, output):
    with open(file_path, "r") as input, open(output, "w+") as output:
        input.readline()
        for line in input:
            instruction = line.rstrip("\n").split(" ")
            write_result_command(storage, instruction, output)


def write_storage(storage, output_file):
    def recursion(storage_cell: TreeNode, file):
        size = str(storage_cell.key)
        count = str(storage_cell.value)
        if storage_cell.left is None:
            file.write(f"{size} {count}\n")
        elif storage_cell.left is not None:
            recursion(storage_cell.left, file)
            file.write(f"{size} {count}\n")

        if storage_cell.right is not None:
            recursion(storage_cell.right, file)

    with open(output_file, "w+") as file:
        recursion(storage.root, file)


def main():
    args = parse()

    input_file = find_log(args.logs, "/")

    storage = create_tree_map()
    write_result(storage, input_file, args.output)
    write_storage(storage, args.remains)


if __name__ == "__main__":
    main()
