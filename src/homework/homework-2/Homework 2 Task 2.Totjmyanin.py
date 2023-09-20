import os


def find_file_path(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    print('This file was not found in the file system')
    return None


def reading_file(path):
    with open(path, "r") as file:
        for line in file:
            for word in line.rstrip('\n').split(' '):
                yield word


def find_words_that_occur(path):
    return set(i for i in reading_file(path))  # For example: ('Hello', 'world')


def find_count_individual_word(word, path):
    return list(reading_file(path)).count(word)  # If word == 'Hello' - 1, 'world' - 1, etc.


def find_counts_each_word(path):
    counts_each_word = {}
    for word in find_words_that_occur(path):
        counts_each_word.update({word: find_count_individual_word(word, path)})
    return sorted(counts_each_word.items(), key=lambda x:x[1])  # [('Hello', 1), ('world', 1)]


def write_data_to_file(data, path):
    with open(path, "w") as file:
        for i in range(len(data)):
            file.write(data[i][0] + ',' + str(data[i][1]) + '\n')
    print("Writing data to the file was successful")


if __name__ == '__main__':
    txt_file_path = find_file_path(input('Enter name of your file in format XXX.txt: '), '/')
    csv_file_path = find_file_path(input('Enter name of your file in format XXX.csv: '), '/')

    if txt_file_path is None or csv_file_path is None:
        print("We cannot write data from txt file to csv file because one of them doesn't exist")
    else:
        received_data = find_counts_each_word(txt_file_path)
        write_data_to_file(received_data, csv_file_path)
