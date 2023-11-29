def get_fibonacci(n: int) -> int:
    if not (0 <= n <= 90):
        raise ValueError("Your number must be between 0 and 90!")

    first_fibo = 0
    second_fibo = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(n - 1):
        new_fibo = first_fibo + second_fibo
        first_fibo = second_fibo
        second_fibo = new_fibo

    return second_fibo


def is_int(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def main():
    user_input = input(
        "Enter the number of the fibonacci number you want to get (from 0 to 90): "
    )
    if is_int(user_input):
        try:
            fibonacci_number = get_fibonacci(int(user_input))
            print(f"Your {user_input} fibonacci number is {fibonacci_number}")
        except ValueError as error:
            print(error)
    else:
        print("You entered not a number")


if __name__ == "__main__":
    main()
