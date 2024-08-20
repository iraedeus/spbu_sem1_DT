import pytest
from io import StringIO
from src.test.test_2.safe_call import *


@safe_call
def dummy_unwrapped_fail_func(value):
    print(value / 0)


@safe_call
def dummy_wrapped_fail_func(value):
    def inner():
        return value + 90

    return inner()


@safe_call
def dummy_success_func(value):
    return value + 90


def dummy_exception_func():
    raise ValueError("Testing")


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "wa",
            "An exception type TypeError was occurred: unsupported operand type(s) for /: 'str' and 'int'\n"
            "Function: dummy_unwrapped_fail_func\n"
            "File: test_safe_call.py\n"
            "line_8: print(value / 0)\n",
        ),
        (
            "45",
            "An exception type TypeError was occurred: unsupported operand type(s) for /: 'str' and 'int'\n"
            "Function: dummy_unwrapped_fail_func\n"
            "File: test_safe_call.py\n"
            "line_8: print(value / 0)\n",
        ),
        (
            6,
            "An exception type ZeroDivisionError was occurred: division by zero\n"
            "Function: dummy_unwrapped_fail_func\n"
            "File: test_safe_call.py\n"
            "line_8: print(value / 0)\n",
        ),
    ],
)
def test_unwrapped_fail_deco(value, expected, monkeypatch):
    with warnings.catch_warnings(record=True) as warning:
        dummy_unwrapped_fail_func(value)

        assert len(warning) != 0
        assert str(warning[-1].message) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "abc",
            'An exception type TypeError was occurred: can only concatenate str (not "int") to str\n'
            "Function: inner\n"
            "File: test_safe_call.py\n"
            "line_14: return value + 90\n",
        ),
    ],
)
def test_wrapped_fail_deco(value, expected):
    with warnings.catch_warnings(record=True) as warning:
        dummy_wrapped_fail_func(value)

        assert len(warning) != 0
        assert str(warning[-1].message) == expected


@pytest.mark.parametrize("value, expected", [(5, 95), (90.9, 180.9)])
def test_success_deco(value, expected):
    with warnings.catch_warnings(record=True) as warning:
        output = dummy_success_func(value)

        assert len(warning) == 0
        assert output == expected


def test_get_info():
    try:
        dummy_exception_func()
    except ValueError:
        assert get_info() == (
            "dummy_exception_func",
            "test_safe_call.py",
            25,
            'raise ValueError("Testing")',
        )
