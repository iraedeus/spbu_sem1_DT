import random


def computer_makes_number():
    final_num = str(random.randint(0, 9))
    while len(final_num) < 4:
        current_digit = str(random.randint(0, 9))
        if current_digit not in final_num:
            final_num += current_digit
    return final_num


def print_rules():
    print(
        "The computer makes a four-digit number with non-repeating digits. You need to guess it by entering your number.\n"
        "If, for example, 2 digits from your number match the numbers from the hidden one, but do not stand in their place,"
        'then the result will be: "2 cows".\n'
        "If, for example, one digit coincides with a digit from a hidden number and stands in its place,"
        ' then the result will be: "1 bull"'
    )


def paint_in_color(text, color):
    if color == "green":
        return "\033[32m{}".format(text)
    if color == "yellow":
        return "\033[33m{}".format(text)
    if color == "white":
        return "\033[0m{}".format(text)


def check_digits(computer_num, user_num):
    count_of_cows = 0
    count_of_bulls = 0
    for i in range(len(computer_num)):
        if user_num[i] == computer_num[i]:
            count_of_bulls += 1
        elif user_num[i] in computer_num:
            count_of_cows += 1
    return paint_in_color(f"{count_of_bulls} bulls\n", "green") + paint_in_color(
        f"{count_of_cows} cows", "yellow"
    )


def check_if_input_wrong(user_input):
    for i in range(len(user_input)):
        current_digit = user_input[i]
        if user_input.count(current_digit) > 1:
            return True


def game_process():
    while True:
        user_input = input(paint_in_color("Enter a number!: ", "white"))
        if check_if_input_wrong(user_input):
            print("You entered wrong number, try again.")
            continue
        if hidden_number == user_input:
            print("Congratulations! You've won!")
            break
        print(check_digits(hidden_number, user_input))


if __name__ == "__main__":
    print_rules()
    hidden_number = computer_makes_number()
    game_process()
