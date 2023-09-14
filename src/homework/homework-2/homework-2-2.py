import os


def find_file_path(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    print('This file was not found in the file system')
    return None


def find_words_that_occur(path):
    words = []
    with open(path, "r") as file:
        for line in file:
            for word in line.replace('\n', '').split(' '):
                words.append(word)
    return set(words)  # For example: ('Hello', 'world')


def find_count_individual_word(path, word):
    count_of_words = 0
    with open(path, "r") as file:
        for line in file:
            count_of_words += line.replace('\n', '').split(' ').count(word)
    return count_of_words  # If word == 'Hello' - 1, 'world' - 1, etc.


def find_counts_each_word():
    counts_each_word = {}
    for word in find_words_that_occur(txt_file_path):
        counts_each_word.update({word: find_count_individual_word(txt_file_path, word)})
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
        print('We cannot write data from txt file to csv file, because one of them doesnt exist')
    else:
        received_data = find_counts_each_word()
        write_data_to_file(received_data, csv_file_path)
