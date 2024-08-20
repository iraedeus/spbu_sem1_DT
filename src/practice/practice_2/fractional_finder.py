import math


def find_fractions(n):
    fractions = {}
    for denominator in range(2, user_input + 1):
        for numerator in range(1, denominator):
            if math.gcd(numerator, denominator) == 1:
                fractions[str(numerator) + "/" + str(denominator)] = (
                    numerator / denominator
                )
    return fractions


def print_fractions(sorted_dict):
    for i in sorted_dict:
        print(i[0])


if __name__ == "__main__":
    user_input = int(input("Enter n: "))
    fractions = find_fractions(user_input)

    sorted_fractions = sorted(fractions.items(), key=lambda x: x[1])
    print_fractions(sorted_fractions)
