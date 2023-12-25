import functools
import traceback
import sys
import warnings
from typing import Callable


def get_info():
    exc_traceback = sys.exc_info()[2]
    tb = traceback.extract_tb(exc_traceback)[-1]

    return tb.name, tb.filename.split("/")[-1], tb.lineno, tb.line


def safe_call(function: Callable):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as error:
            error_type = type(error).__name__
            function_name, file_name, line_number, line = get_info()

            warning_message = (
                f"An exception type {error_type} was occurred: {error}\n"
                f"Function: {function_name}\n"
                f"File: {file_name}\n"
                f"line_{line_number}: {line}\n"
            )
            warnings.warn(warning_message)
            return None

    return inner


@safe_call
def goo():
    def loo():
        return "a" + 1

    return loo()


@safe_call
def foo(a):
    a / 0


@safe_call
def type_error():
    return "78" - 9


def main():
    foo(8)
    type_error()
    goo()


if __name__ == "__main__":
    main()
