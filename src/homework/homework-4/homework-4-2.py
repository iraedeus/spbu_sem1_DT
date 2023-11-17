from math import floor


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

    binary_integer_part = bin(integer_part)[2:]
    mantissa_bits = bits - len(binary_integer_part) - k
    binary_fractional_part = to_bin_fractional(fractional_part, mantissa_bits)

    return (binary_integer_part + binary_fractional_part)[1:]


def find_true_order(number):
    integer_part = floor(abs(number))
    binary_integer_part = bin(integer_part)[2:]

    return len(binary_integer_part) - 1


def to_fp16(number):
    if number != 0:
        true_order = find_true_order(number)
        shifted_order = true_order + 2**4 - 1

        mantissa = find_mantissa(number, 5, 16)
        return check_sign(number) + bin(shifted_order).lstrip("0b") + " " + mantissa
    else:
        return "0 " + "0" * 5 + " " + "0" * 11


def to_fp32(number):
    if number != 0:
        true_order = find_true_order(number)
        shifted_order = true_order + 2**7 - 1

        mantissa = find_mantissa(number, 8, 32)
        return check_sign(number) + bin(shifted_order).lstrip("0b") + " " + mantissa
    else:
        return "0 " + "0" * 8 + " " + "0" * 23


def to_fp64(number):
    if number != 0:
        true_order = find_true_order(number)
        shifted_order = true_order + 2**10 - 1

        mantissa = find_mantissa(number, 11, 64)
        return check_sign(number) + bin(shifted_order).lstrip("0b") + " " + mantissa
    else:
        return "0 " + "0" * 11 + " " + "0" * 52


def to_exponential(number):
    if number >= 0:
        output = "+"
    else:
        output = "-"

    bin_integer_part = bin(floor(number)).lstrip("0b")
    bin_fractional_part = to_bin_fractional(number - floor(number), 10)
    p = len(bin_integer_part)

    output += "0," + bin_integer_part + bin_fractional_part + f"*2^{p}"
    return output


def output_to_user(choice, number):
    exponential_number = to_exponential(number)
    if choice == "1":
        print(f"Your number in exponential format: {exponential_number}")
        print(f"Your number in FP16: {to_fp16(number)}")
    if choice == "2":
        print(f"Your number in exponential format: {exponential_number}")
        print(f"Your number in FP32: {to_fp32(number)}")
    if choice == "3":
        print(f"Your number in exponential format: {exponential_number}")
        print(f"Your number in FP64: {to_fp64(number)}")
    else:
        print("You have chosen an incorrect action")


if __name__ == "__main__":
    try:
        user_number = float(input("Enter you number: ").replace(",", "."))
        user_choice = input("Choose format: \n" "1) FP16 \n" "2) FP32 \n" "3) FP64 \n")
        output_to_user(user_choice, user_number)
        print(bin(0).lstrip("0b"))
    except ValueError:
        print("You entered not a number")
