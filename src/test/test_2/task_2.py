import functools
import time
from inspect import getcallargs


def spy(function):
    @functools.wraps(function)
    def inner(*args, **kargs):
        t = time.localtime()
        start_time = time.strftime("%H:%M:%S", t)
        parameters = getcallargs(function, *args, **kargs)
        string_parameters = ", ".join(
            [f"{parameter} = {parameters[parameter]}" for parameter in parameters]
        )

        inner.logs.append((start_time, string_parameters))

        result = function(*args, **kargs)
        return result

    inner.logs = []

    return inner


def saved_logs(function):
    try:
        logs = function.logs
        for log in logs:
            yield log
    except AttributeError:
        print("This function haven't decorator spy")


def print_usage_statistics(function):
    for log in saved_logs(function):
        print(
            f"Function {function.__name__} was called at {log[0]} with parameters:\n{log[1]}"
        )


@spy
def with_spy(n, key="obed"):
    return n


def without_spy(n):
    return n


def main():
    with_spy(8, key="obed")
    print_usage_statistics(with_spy)


if __name__ == "__main__":
    main()
