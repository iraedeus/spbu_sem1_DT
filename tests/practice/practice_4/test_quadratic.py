import pytest
from io import StringIO
from src.practice.practice_4.quadratic import *


@pytest.mark.parametrize(
    "number,expected", [("9.9", True), ("9", True), ("a", False), ("*", False)]
)
def test_is_float(number, expected):
    assert is_float_number(number) == expected


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ("5 8 9", [5.0, 8.0, 9.0]),
        ("0 66 9", [0.0, 66.0, 9.0]),
        ("9.83 0 9.8", [9.83, 0.0, 9.8]),
    ],
)
def test_to_float(numbers, expected):
    assert to_float_coeffs(numbers) == expected


@pytest.mark.parametrize("numbers", [("88 *^& 8"), ("jj k l")])
def test_to_float_exceptions(numbers):
    with pytest.raises(ValueError):
        to_float_coeffs(numbers)


@pytest.mark.parametrize(
    "b,c,expected",
    [
        (6, 1, (-1 / 6,)),
        (6, 0, (0,)),
    ],
)
def test_solve_linear_equation(b, c, expected):
    assert solve_linear_equation(b, c) == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (3, 4, 1, (-2 / 6, -1.0)),
        (2, -14, 24, (3.0, 4.0)),
        (1, -4, 4, (2.0,)),
    ],
)
def test_solve_quadratic_equation(a, b, c, expected):
    actual = solve_quadratic_equation(a, b, c)
    assert set(actual) == set(expected)


@pytest.mark.parametrize("a,b,c", [(1, 6, 999), (9, 83, 7373773)])
def test_quadratic_exceptions(a, b, c):
    with pytest.raises(ValueError):
        solve_quadratic_equation(a, b, c)


@pytest.mark.parametrize(
    "a,b,c, expected",
    [
        (1, -6, 9, (3.0,)),
        (1, 6, 9, (-3.0,)),
        (0, 5, 1, (-1 / 5,)),
        (5, -8, 3, (1.0, 3 / 5)),
    ],
)
def test_solve_equations(a, b, c, expected):
    assert set(solve_equation(a, b, c)) == set(expected)


def test_solve_equations_exception():
    with pytest.raises(ValueError):
        solve_equation(0, 0, 0)
        solve_equation(0, 0, 9)


@pytest.mark.parametrize(
    "input_user, expected1, expected2",
    [
        ("1 17 -18", "(1.0, -18.0)\n", "(-18.0, 1.0)\n"),
        ("2 7 -4", "(0.5, -4.0)\n", "(-4.0, 0.5)\n"),
        ("1 18 81", "(-9.0,)\n", ""),
        ("0 11 5", f"({str(-5/11)},)\n", ""),
    ],
)
def test_main_scenario(input_user, expected1, expected2, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: input_user)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert (output == expected1) or (output == expected2)
