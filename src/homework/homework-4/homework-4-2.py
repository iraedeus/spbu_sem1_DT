from math import *


def to_bin_fractional(number, mantissa_bits):
    binary_fractional = ""
    for i in range(mantissa_bits):
        number = number * 2
        if number >= 1:
            binary_fractional += "1"
            number -= 1
        else:
            binary_fractional += "0"
    return binary_fractional


def check_sign(number):
    if number >= 0:
        return "0 "
    return "1 "


def find_mantissa(number, k, bits):
    integer_part = floor(abs(number))
    fractional_part = abs(number) - integer_part

    binary_integer_part = bin(integer_part).lstrip("0b")
    mantissa_bits = bits - len(binary_integer_part) - k - 2
    binary_fractional_part = to_bin_fractional(fractional_part, mantissa_bits)

    return (binary_integer_part + binary_fractional_part)[1:]


def find_true_order(number):
    integer_part = floor(abs(number))
    binary_integer_part = bin(integer_part).lstrip("0b")

    return len(binary_integer_part) - 1


def to_fp16(number):
    true_order = find_true_order(number)
    shifted_order = true_order + 2**4 - 1

    mantissa = find_mantissa(number, 5, 16)
    return check_sign(number) + bin(shifted_order).lstrip("0b") + " " + mantissa


def to_fp32(number):
    true_order = find_true_order(number)
    shifted_order = true_order + 2**7 - 1

    mantissa = find_mantissa(number, 8, 32)
    return check_sign(number) + bin(shifted_order).lstrip("0b") + " " + mantissa


def to_fp64(number):
    true_order = find_true_order(number)
    shifted_order = true_order + 2**10 - 1

    mantissa = find_mantissa(number, 11, 64)
    return check_sign(number) + bin(shifted_order).lstrip("0b") + " " + mantissa


def to_exponential(number):
    if number > 0:
        output = "+"
    else:
        output = "-"

    number = abs(number)
    p = 0

    if number >= 1:
        while number / 2 >= 1:
            p += 1
            number /= 2
    else:
        while -1 <= number <= 1:
            p -= 1
            number *= 2

    return output + f"{str(number)}*2^{str(p)}"


def output_to_user(choice, number):
    print(f"Your number in exponential format: {to_exponential(number)}")
    if choice == "1":
        print(f"Your number in FP16: {to_fp16(number)}")
    if choice == "2":
        print(f"Your number in FP32: {to_fp32(number)}")
    if choice == "3":
        print(f"Your number in FP64: {to_fp64(number)}")


if __name__ == "__main__":
    user_number = float(input("Enter you number: ").replace(",", "."))
    user_choice = input("Choose format: \n" "1) FP16 \n" "2) FP32 \n" "3) FP64 \n")
    output_to_user(user_choice, user_number)