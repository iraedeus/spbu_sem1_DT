import os.path
import sys


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None


def get_text_of_file(file_name):
    with open(file_name) as file_func:
        file_content_func = file_func.read()
    return file_content_func


def find_lines_tail(file_text, count_of_lines):
    if count_of_lines > len(file_text.split('\n')) - 1:
        return file_text
    output_string = ''
    array_lines = file_text.split('\n')[len(file_text.split('\n'))-count_of_lines-1:]
    for i in array_lines:
        output_string += i + '\n'
    return output_string


def find_string_with_bytes_tail(file_text, size_in_bytes):
    output_text = ''
    reversed_file_text = file_text[::-1]
    current_bytes = 0
    for i in range(len(reversed_file_text)):
        current_bytes += len(reversed_file_text[i].encode('utf-8'))
        if current_bytes <= size_in_bytes:
            output_text += reversed_file_text[i]
    return output_text[::-1]


def get_count_of_lines(file_path):
    line_count = 0
    with open(file_path) as file:
        for line in file:
            line_count += 1
    return line_count


def get_count_of_words(file_path):
    words_count = 0
    with open(file_path) as file:
        for line in file:
            words_count += line.count(' ') + line.count('\n')
    return words_count


def get_count_of_chars(file_path):
    chars_count = 0
    with open(file_path) as file:
        for line in file:
            chars_count += len(line)
    return chars_count


def wc_logic():
    if '-l' in args:  # Get count of lines
        output_nums.append(('Count of lines: ', get_count_of_lines(file_input_path)))
    if '-w' in args:  # Get count of words
        output_nums.append(('Count of words: ', get_count_of_words(file_input_path)))
    if '-c' in args:  # Get size of file
        output_nums.append(('Size of file: ', os.path.getsize(file_input_path)))
    if '-m' in args:  # Get count of chars
        output_nums.append(('Count of chars: ', get_count_of_chars(file_input_path) - get_count_of_lines(file_input_path)))


def wc_output(output_arr):
    for i in range(len(output_arr)):
        print(output_arr[i][0] + str(output_arr[i][1]))
    return None


def head_logic():
    parameter = int(sys.argv[3])
    if '-n' in args:  # Print first {parameter} lines
        with open(file_input_path) as file:
            for i in range(parameter):
                print(file.readline().replace('\n', '', 1))
                if i >= get_count_of_lines(file_input_path):
                    break
    elif '-c' in args:  # Print first {parameter} bytes
        with open(file_input_path) as file:
            print(file.read(parameter))
    else:
        print(paint_text('You entered wrong argument!', 'red'))


def tail_logic():
    parameter = int(sys.argv[3])
    if '-n' in args:  # Print last {parameter} lines
        file_content = get_text_of_file(file_input_path)
        print(find_lines_tail(file_content, parameter))
    elif '-c' in args:  # Print last {parameter} bytes
        file_content = get_text_of_file(file_input_path)
        print(find_string_with_bytes_tail(file_content, parameter))
    else:
        print(paint_text('You entered wrong argument!', 'red'))


def paint_text(text, color):
    if color == 'red':
        return "\033[31m{}".format(text)
    return text


if __name__ == '__main__':
    command = sys.argv[1]  # wc, head, tail
    args = sys.argv[2:len(sys.argv)-1]  # -c, -m etc.
    file_input_path = find_file(sys.argv[-1], '/')

    if command == 'wc':
        output_nums = []
        wc_logic()
        wc_output(output_nums)
        print(sys.argv[-1])
    elif command == 'head':
        head_logic()
    elif command == 'tail':
        tail_logic()
    else:
        print(paint_text('You entered wrong command!', 'red'))