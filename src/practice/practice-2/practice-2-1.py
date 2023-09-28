def greatest_common_divisor(num1, num2):  # Euclid's algorithm
    divisible = num1
    divider = num2
    while True:
        remainder_of_division = divisible % divider
        divisible = divider
        if remainder_of_division == 0:
            return divider
        divider = remainder_of_division


if __name__ == "__main__":
    user_input = int(input("Enter n: "))

    for denominator in range(2, user_input + 1):
        for numerator in range(1, denominator):
            if greatest_common_divisor(numerator, denominator) == 1:
                print(str(numerator) + "/" + str(denominator))
