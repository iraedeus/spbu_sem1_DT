import os


def find_file_path(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    print('This file was not found in the file system')
    return None


def get_lines_from_file(path, start_line, end_line):
    values = []
    with open(path, "r") as file:
        for i in range(0, start_line):
            file.readline()
        if end_line is None:
            for i in file:
                values.append(i.rstrip('\n'))
        else:
            for i in range(start_line, end_line):
                values.append(file.readline().rstrip('\n'))
    return values


def delete_fragment_dna(dna, start, end):
    index_start = dna.find(start) + len(start)
    index_end = dna[index_start:len(dna)].find(end) + index_start
    return dna[0:index_start] + dna[index_end:]


def insert_fragment_dna(dna, start, fragment):
    dna_before_fragment = dna[0:dna.find(start) + len(start)]
    dna_after_fragment = dna[dna.find(start) + len(start):]
    return dna_before_fragment + fragment + dna_after_fragment


def execute_the_command(dna, raw_command):
    command, arg1, arg2 = raw_command.split(" ")
    if command == 'INSERT':
        return insert_fragment_dna(dna, arg1, arg2)
    elif command == 'DELETE':
        return delete_fragment_dna(dna, arg1, arg2)
    elif command == 'REPLACE':
        return dna.replace(arg1, arg2, 1)


if __name__ == '__main__':
    log_file_path = find_file_path(input('Enter your log file in format XXX.txt: '), '/')
    output_file_path = find_file_path(input('Enter you output file in format XXX.txt: '), '/')

    _, dna, n = get_lines_from_file(log_file_path, 0, 3)

    array_of_dna = []

    with open(log_file_path, "r") as file:
        for current_command in get_lines_from_file(log_file_path, 3, None):
            dna = execute_the_command(dna, current_command)
            array_of_dna.append(dna)

    with open(output_file_path, "w") as file:
        for dna in array_of_dna:
            print(dna, file=file)
