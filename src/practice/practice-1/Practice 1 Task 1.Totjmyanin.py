def incomplete_quotient(a, b):
    answer = 0
    while a >= b:
        answer += 1
        a -= b
    return answer


def main():
    while True:
        divisible_from_user = input("Enter your divisible number: ")
        try:
            float(divisible_from_user)
        except ValueError:
            print("You entered not a number!")
            continue

        divider_from_user = input("Enter your divider: ")
        try:
            float(divider_from_user)
        except ValueError:
            print("You entered not a number!")
            continue

        quotient = incomplete_quotient(
            float(divisible_from_user), float(divider_from_user)
        )
        print("Quotient is: " + str(quotient))


if __name__ == "__main__":
    main()
