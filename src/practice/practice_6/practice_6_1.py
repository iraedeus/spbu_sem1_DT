def solve_quadratic_equation(a, b, c):
    discriminant = (b * b) - (4 * a * c)
    if discriminant == 0:
        return (-b / (2 * a),)
    elif discriminant > 0:
        x1 = (-b - (discriminant**0.5)) / (2 * a)
        x2 = (-b + (discriminant**0.5)) / (2 * a)
        return x1, x2
    else:
        raise ValueError("Discriminant must be greater or equal than 0")


def solve_linear_equation(b, c):
    if b == 0:
        raise ValueError("Division by 0!")
    else:
        return (-c / b,)


def solve_equation(a, b, c):
    if a == b == c == 0:
        raise ValueError("x is any number")
    elif a == 0:
        try:
            return solve_linear_equation(b, c)
        except ValueError:
            print("Division by 0!")
            return ()
    try:
        return solve_quadratic_equation(a, b, c)
    except ValueError:
        print("Discriminant is less than 0!")
        return ()


def is_float_number(number):
    try:
        float(number)
    except:
        return False
    return True


def to_float_coeffs(user_input):
    user_input = user_input.split(" ")
    if len(user_input) == 3:
        for i in user_input:
            if not is_float_number(i):
                raise ValueError(
                    "You entered wrong coefficients: They must be float number"
                )
            return list(map(float, user_input))
    else:
        raise ValueError("You must enter 3 coefficients")


def main():
    try:
        a, b, c = to_float_coeffs(input("Enter your coefficients: "))
        print(solve_equation(a, b, c))
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
