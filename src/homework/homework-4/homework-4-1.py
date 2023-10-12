from math import *


def binary_inversion(number):
    output = ""
    for i in range(len(number)):
        if number[i] == "0":
            output += "1"
        else:
            output += "0"
    return output


def to_binary(number):
    sign_bit = "0"
    if number < 0:
        sign_bit = "1"
    output = ""

    number = abs(number)
    while number >= 1:
        output = str(number % 2) + output
        number = number // 2

    bytes = ceil((len(output) + 1) / 8)
    binary_one = format_binary("01", bytes)

    if sign_bit == "0":
        return sign_bit + output
    else:
        return sign_bit + binary_sum(binary_inversion(output), binary_one)


def format_binary(number, bytes):
    if number[0] == "1":
        output = "1" + "11111111" * bytes
    else:
        output = "0" + "00000000" * bytes
    return output[: len(output) - len(number) + 1] + number[1:]


def binary_sum(number1, number2):
    output = ""
    remembered_digit = 0

    for i in range(1, len(number1) + 1):
        sum_of_digits = remembered_digit + int(number1[-i]) + int(number2[-i])

        if sum_of_digits > 1:
            remembered_digit = 1
            output = str(sum_of_digits % 2) + output
        else:
            remembered_digit = 0
            output = str(sum_of_digits % 2) + output

    if len(output) > len(number1):
        return output[1:]
    return output


def binary_difference(number1, number2):
    bytes = ceil((len(number1) + 1) / 8)
    binary_one = format_binary("01", bytes)
    number2 = binary_sum(binary_inversion(number2), binary_one)

    return binary_sum(number1, number2)


def to_decimal(number):
    output = 0
    for i in range(1, len(number) + 1):
        output += int(number[-i]) * 2 ** (i - 1)
        if i == len(number):
            output -= int(number[-i]) * 2**i
    return output


def output_to_user(number1, number2):
    if abs(number1) > abs(number2):
        numbers_bytes = ceil(len(to_binary(number1)) / 8)
    else:
        numbers_bytes = ceil(len(to_binary(number2)) / 8)

    user_binary_number1 = format_binary(to_binary(number1), numbers_bytes)
    user_binary_number2 = format_binary(to_binary(number2), numbers_bytes)
    sum_of_numbers = binary_sum(user_binary_number1, user_binary_number2)
    difference_of_numbers = binary_difference(user_binary_number1, user_binary_number2)

    print(" ")
    print(f"{number1} in binary system: {user_binary_number1}")
    print(f"{number2} in binary system: {user_binary_number2}")
    print(f"{number1} + {number2} in binary system: {sum_of_numbers}")
    print(f"{number1} + {number2} in decimal system: {to_decimal(sum_of_numbers)}")
    print(f"{number1} - {number2} in binary system: {difference_of_numbers}")
    print(
        f"{number1} - {number2} in decimal system: {to_decimal(difference_of_numbers)}"
    )


if __name__ == "__main__":
    user_number1 = int(input("Enter your first number: "))
    user_number2 = int(input("Enter your second number: "))

    output_to_user(user_number1, user_number2)
