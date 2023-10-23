import pytest
from io import StringIO
from src.practice.practice_6.practice_6_1 import *

to_float_arr = [
    ("5 8 9", [5.0, 8.0, 9.0]),
    ("0 66 9", [0.0, 66.0, 9.0]),
    ("9.83 0 9.8", [9.83, 0.0, 9.8]),
]

solve_linear_arr = [
    (6, 1, (-1 / 6,)),
    (6, 0, (0,)),
]

solve_quadratic_arr = [
    (3, 4, 1, (-2 / 6, -1.0)),
    (2, -14, 24, (3.0, 4.0)),
    (1, -4, 4, (2.0,)),
]

solve_equation_arr = [
    (1, -6, 9, (3,)),
    (1, 6, 9, (-3,)),
    (0, 5, 1, (-1 / 5,)),
    (5, -8, 3, (1, 3 / 5)),
]

main_scenario_arr = [
    ("1 17 -18", "(1.0, -18.0)\n", "(-18.0, 1.0)\n"),
    ("2 7 -4", "(0.5, -4.0)\n", "(-4.0, 0.5)\n"),
    ("1 18 81", "(-9.0,)\n", ""),
    ("0 11 5", f"({str(-5/11)},)\n", ""),
    ("0 0 0", "()\n", ""),
]


@pytest.mark.parametrize(
    "number,expected", [("9.9", True), ("9", True), ("a", False), ("*", False)]
)
def test_is_float(number, expected):
    assert is_float_number(number) == expected


@pytest.mark.parametrize("numbers,expected", to_float_arr)
def test_to_float(numbers, expected):
    assert to_float_coeffs(numbers) == expected


@pytest.mark.parametrize("numbers", [("88 *^& 8"), ("jj k l")])
def test_to_float_exceptions(numbers):
    with pytest.raises(ValueError):
        to_float_coeffs(numbers)


@pytest.mark.parametrize("b,c,expected", solve_linear_arr)
def test_solve_linear_equation(b, c, expected):
    assert solve_linear_equation(b, c) == expected


@pytest.mark.parametrize("b,c", [(0, 6), (0, 700)])
def test_linear_exceptions(b, c):
    with pytest.raises(ZeroDivisionError):
        solve_linear_equation(b, c)


@pytest.mark.parametrize("a,b,c,expected", solve_quadratic_arr)
def test_solve_quadratic_equation(a, b, c, expected):
    actual = solve_quadratic_equation(a, b, c)
    assert set(actual) == set(expected)


@pytest.mark.parametrize("a,b,c", [(1, 6, 999), (9, 83, 7373773)])
def test_quadratic_exceptions(a, b, c):
    with pytest.raises(ValueError):
        solve_quadratic_equation(a, b, c)


@pytest.mark.parametrize("a,b,c, expected", solve_equation_arr)
def test_solve_equations(a, b, c, expected):
    if a == 0:
        assert solve_equation(a, b, c) == expected
    else:
        actual = solve_equation(a, b, c)
        assert set(actual) == set(expected)


@pytest.mark.parametrize("input_user, expected1, expected2", main_scenario_arr)
def test_main_scenario(input_user, expected1, expected2, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: input_user)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert (output == expected1) or (output == expected2)
