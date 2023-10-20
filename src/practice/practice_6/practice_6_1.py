def solve_quadratic_equation(a, b, c):
    discriminant = (b * b) - (4 * a * c)
    if discriminant == 0:
        return -b / (2 * a)
    elif discriminant > 0:
        x1 = (-b - (discriminant ** 0.5)) / (2 * a)
        x2 = (-b + (discriminant ** 0.5)) / (2 * a)
        return x1, x2
    else:
        raise ValueError("Discriminant must be greater or equal than 0")


def solve_linear_equation(b, c):
    if b != 0:
        return -c / b
    else:
        raise ZeroDivisionError


def solve_equation(a, b, c):
    if (a == 0) and (b == 0) and (c == 0):
        return
    elif a == 0:
        return solve_linear_equation(b, c)
    return solve_quadratic_equation(a, b, c)


def is_float_number(number):
    try:
        float(number)
    except:
        return False
    return True


def to_float_coeffs(user_input):
    for i in user_input:
        if not is_float_number(i):
            raise ValueError("You entered wrong coefficients")
        return map(float, user_input)


def main():
    coeffs = input("Enter your coefficients: ").split(" ")
    a, b, c = to_float_coeffs(coeffs)
    roots = solve_equation(a, b, c)

    if type(roots) == float:
        print(roots)
    else:
        print(roots[0], roots[1])


if __name__ == "__main__":
    main()