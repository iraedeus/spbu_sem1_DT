import pytest
from src.test.test_2.task_1 import *
from io import StringIO


@pytest.mark.parametrize(
    "number, expected", [(0, 0), (1, 1), (2, 1), (67, 44945570212853)]
)
def test_get_fibonacci(number, expected):
    assert get_fibonacci(number) == expected


@pytest.mark.parametrize("number", [(1000), (-100)])
def test_get_fibonacci_exceptions(number):
    with pytest.raises(ValueError):
        get_fibonacci(number)


@pytest.mark.parametrize(
    "number, expected", [("8,9", False), ("9", True), ("fsff", False)]
)
def test_is_int(number, expected):
    assert is_int(number) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        (0, "Your 0 fibonacci number is 0\n"),
        (6, "Your 6 fibonacci number is 8\n"),
        (80, "Your 80 fibonacci number is 23416728348467685\n"),
        ("fasf", "You entered not a number\n"),
    ],
)
def test_main(user_input, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    fake_output = StringIO()

    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
