from src.homework.homework_6.avl_tree import *
import os


OUTPUT_FILE = "output.txt"


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None


def get(directory: TreeMap, address: list):
    street = address[0]
    house, corpus = map(int, address[1:])
    try:
        houses = get_tree_node(directory, street).value
        corpuses = get_value(houses, house)
    except:
        return None

    for block in corpuses:
        if block[0] == corpus:
            return block[1]


def create(directory: TreeMap, address: list, index: int):
    street = address[0]
    house, corpus = map(int, address[1:])

    if has_key(directory, street):
        houses = get_tree_node(directory, street).value
        if has_key(houses, house):
            corpuses = get_tree_node(houses, house).value
            corpuses.append((corpus, index))
            corpuses.sort()
        else:
            put(houses, house, [(corpus, index)])
    else:
        house_tree = create_tree_map()
        corpuses = [(corpus, index)]
        put(house_tree, house, corpuses)

        put(directory, street, house_tree)


def rename(directory: TreeMap, street_name: str, new_name: str):
    try:
        houses = get_value(directory, street_name)
        remove(directory, street_name)
        put(directory, new_name, houses)
    except:
        return None


def delete_block(directory: TreeMap, address: list):
    street = address[0]
    house, corpus = map(int, address[1:])

    try:
        houses = get_tree_node(directory, street).value
        corpuses = get_tree_node(houses, house).value
    except:
        return None

    for i in range(len(corpuses)):
        if corpuses[i][0] == corpus:
            del corpuses[i]
            break

    if not corpuses:
        remove(houses, int(house))
    if houses.root is None:
        remove(directory, street)


def delete_house(directory: TreeMap, address: list):
    street, house = address
    try:
        houses = get_tree_node(directory, street).value
        remove(houses, int(house))
    except:
        return None

    if houses.root is None:
        remove(directory, street)


def delete_street(directory: TreeMap, street: str):
    try:
        remove(directory, street)
    except:
        return None


def filter(streets: list[tuple], left_address, right_address):
    output = []
    left_street = left_address[0]
    left_house, left_corpus = map(int, left_address[1:])
    right_street = right_address[0]
    right_house, right_corpus = map(int, right_address[1:])

    for street in streets:
        for house in street[1]:
            for corpus in house[1]:
                if left_street != right_street:
                    if left_street < street[0] < right_street:
                        output.append(f"{street[0]} {house[0]} {corpus[0]}\n")
                    if street[0] == left_street:
                        if left_house < house[0]:
                            output.append(f"{street[0]} {house[0]} {corpus[0]}\n")
                        elif left_house == house[0]:
                            if left_corpus <= corpus[0]:
                                output.append(f"{street[0]} {house[0]} {corpus[0]}\n")
                    if street[0] == right_street:
                        if house[0] < right_house:
                            output.append(f"{street[0]} {house[0]} {corpus[0]}\n")
                        elif house[0] == right_house:
                            if corpus[0] < right_corpus:
                                output.append(f"{street[0]} {house[0]} {corpus[0]}\n")
                else:
                    if left_house != right_house:
                        if left_house < house[0] < right_house:
                            output.append(f"{street[0]} {house[0]} {corpus[0]}\n")
                        elif left_house == house[0]:
                            if left_corpus <= corpus[0]:
                                output.append(f"{street[0]} {house[0]} {corpus[0]}\n")
                        elif house[0] == right_house:
                            if corpus[0] < right_corpus:
                                output.append(f"{street[0]} {house[0]} {corpus[0]}\n")
                    else:
                        if left_corpus <= corpus[0] < right_corpus:
                            output.append(f"{street[0]} {house[0]} {corpus[0]}\n")

    return output


def print_list(directory: TreeMap, left_address, right_address):
    streets = []

    def recursion(tree_cell: TreeNode):
        left_child = tree_cell.left
        right_child = tree_cell.right

        if left_address[0] <= tree_cell.key <= right_address[0]:
            if left_child is not None:
                recursion(left_child)
            streets.append(tree_cell)
            if right_child is not None:
                recursion(right_child)
        elif tree_cell.key > right_address[0] and left_child is not None:
            recursion(left_child)
        elif tree_cell.key < left_address[0] and right_child is not None:
            recursion(right_child)

    recursion(directory.root)

    a = map(lambda street: (street.key, street.value), streets)
    b = list(map(lambda item: (item[0], traverse(item[1], "inorder")), a))

    return filter(b, left_address, right_address)


def write_list_to_file(addresses, file):
    for address in addresses:
        file.write(address)
    file.write("\n")


def write_list_to_console(addresses):
    for address in addresses:
        print(address.rstrip("\n"))


def static(directory):
    file_input = find_file(input("Enter your input file: "), "/")

    with open(file_input, "r") as log, open(OUTPUT_FILE, "w+") as output:
        log.readline()
        for instruction in log:
            instruction = instruction.rstrip("\n").split(" ")
            command = instruction[0]
            if command == "CREATE":
                address = instruction[1:4]
                index = int(instruction[-1])
                create(directory, address, index)
            elif command == "RENAME":
                old_name = instruction[1]
                new_name = instruction[2]
                rename(directory, old_name, new_name)
            elif command == "LIST":
                left_address = instruction[1:4]
                right_address = instruction[4:]
                streets = print_list(directory, left_address, right_address)
                write_list_to_file(streets, output)
            elif command == "DELETE_STREET":
                street = instruction[1]
                delete_street(directory, street)
            elif command == "DELETE_HOUSE":
                address = instruction[1:3]
                delete_house(directory, address)
            elif command == "DELETE_BLOCK":
                address = instruction[1:4]
                delete_block(directory, address)
            elif command == "GET":
                address = instruction[1:4]
                index = get(directory, address)
                output.write(str(index) + "\n")
            else:
                print("Incorrect command")


def interactive(directory):
    print("To exit program enter EXIT")
    while True:
        user_input = input("Enter your command: ")
        instruction = user_input.split()
        command = instruction[0]

        if command == "CREATE":
            address = instruction[1:4]
            index = int(instruction[-1])
            create(directory, address, index)
        elif command == "RENAME":
            old_name, new_name = instruction[1:3]
            rename(directory, old_name, new_name)
        elif command == "LIST":
            left_address = instruction[1:4]
            right_address = instruction[4:7]
            streets = print_list(directory, left_address, right_address)
            write_list_to_console(streets)
            print("")
        elif command == "DELETE_STREET":
            street = instruction[1]
            delete_street(directory, street)
        elif command == "DELETE_HOUSE":
            address = instruction[1:3]
            delete_house(directory, address)
        elif command == "DELETE_BLOCK":
            address = instruction[1:4]
            delete_block(directory, address)
        elif command == "GET":
            address = instruction[1:4]
            index = get(directory, address)
            print(index)
        elif command == "EXIT":
            break
        else:
            print("Incorrect command")


def main():
    directory = create_tree_map()
    print("1) Read the file and create new file with result\n" "2) Interactive mode")
    user_choice = input("Enter your action: \n")

    if user_choice == "1":
        static(directory)
    elif user_choice == "2":
        interactive(directory)
    else:
        print("You chosen incorrect action, try again")


if __name__ == "__main__":
    main()
