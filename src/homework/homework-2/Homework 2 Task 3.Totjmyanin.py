import os


def find_file_path(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    print('This file was not found in the file system')
    return None


def get_first_three_values(path):
    values = []
    with open(path, "r") as file:
        for i in range(3):
            values.append(file.readline().replace('\n', ''))
    return values


def delete_fragment_dna(dna, start, end):
    index_start = dna.find(start) + len(start)
    index_end = dna[index_start:len(dna)].find(end) + index_start
    return dna[0:index_start] + dna[index_end:]


def insert_fragment_dna(dna, start, fragment):
    return dna[0:dna.find(start) + len(start)] + fragment + dna[dna.find(start) + len(start):]


def execute_the_command(dna, command):
    if 'INSERT' in command:
        start = command.replace('\n', '').split(' ')[1]
        fragment = command.replace('\n', '').split(' ')[2]
        return insert_fragment_dna(dna, start, fragment)
    elif 'DELETE' in command:
        start = command.replace('\n', '').split(' ')[1]
        end = command.replace('\n', '').split(' ')[2]
        return delete_fragment_dna(dna, start, end)
    elif 'REPLACE' in command:
        template = command.replace('\n', '').split(' ')[1]
        fragment = command.replace('\n', '').split(' ')[2]
        return dna.replace(template, fragment, 1)


if __name__ == '__main__':
    log_file_path = find_file_path(input('Enter your log file in format XXX.txt: '), '/')
    output_file_path = find_file_path(input('Enter you output file in format XXX.txt: '), '/')

    dna = get_first_three_values(log_file_path)[1]
    n = get_first_three_values(log_file_path)[2]

    array_of_dna = []

    with open(log_file_path, "r") as file:
        for i in range(3):
            file.readline()
        for i in range(int(n)):
            current_command = file.readline().replace('\n', '')
            array_of_dna.append(execute_the_command(dna, current_command))
            dna = execute_the_command(dna, current_command)

    with open(output_file_path, "w") as file:
        for i in range(int(n)):
            file.write(array_of_dna[i] + '\n')