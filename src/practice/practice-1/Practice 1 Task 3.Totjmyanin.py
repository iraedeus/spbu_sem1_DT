def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def prime_numbers(n):
    return [i for i in range(2, n, 1) if is_prime(i)]


if __name__ == "__main__":
    input_from_user = input("Please enter your number: ")
    print("List with prime numbers up to " + input_from_user)
    answer = prime_numbers(int(input_from_user))

    print(",".join([str(i) for i in answer]))
