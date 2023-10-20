import pytest
from io import StringIO
from src.practice.practice_6.practice_6_1 import *

is_float_arr = [("9.9", True), ("9", True), ("a", False), ("*", False)]

solve_linear_arr = [
    (6, 1, -1 / 6),
    (6, 0, 0),
]

linear_exceptions_arr = [(0, 6), (0, 700)]

solve_quadratic_arr = [(3, 4, 1, [-2 / 6, -1]), [2, -14, 24, [3, 4]], [1, -4, 4, 2]]

quadratic_exceptions_arr = [(1, 6, 999), (9, 83, 7373773)]

solve_equation_arr = [
    (1, -6, 9, 3),
    (1, 6, 9, -3),
    (0, 5, 1, -1 / 5),
    (5, -8, 3, [1, 3 / 5]),
]

main_scenario_arr = [
    ("1 17 -18", [1.0, -18.0]),
    ("2 7 -4", [1 / 2, -4.0]),
    ("1 18 81", -9.0),
    ("0 11 5", -5 / 11),
]


@pytest.mark.parametrize("number,expected", is_float_arr)
def test_is_float(number, expected):
    assert is_float_number(number) == expected


@pytest.mark.parametrize("b,c,expected", solve_linear_arr)
def test_solve_linear_equation(b, c, expected):
    assert solve_linear_equation(b, c) == expected


@pytest.mark.parametrize("b,c", linear_exceptions_arr)
def test_linear_exceptions(b, c):
    with pytest.raises(ZeroDivisionError):
        solve_linear_equation(b, c)


@pytest.mark.parametrize("a,b,c,expected", solve_quadratic_arr)
def test_solve_quadratic_equation(a, b, c, expected):
    actual = solve_quadratic_equation(a, b, c)
    if type(actual) == float:
        assert actual == expected
    else:
        assert actual[0] in expected and actual[1] in expected


@pytest.mark.parametrize("a,b,c", quadratic_exceptions_arr)
def test_quadratic_exceptions(a, b, c):
    with pytest.raises(ValueError):
        solve_quadratic_equation(a, b, c)


@pytest.mark.parametrize("a,b,c, expected", solve_equation_arr)
def test_solve_equations(a, b, c, expected):
    if a == 0:
        assert solve_equation(a, b, c) == expected
    else:
        actual = solve_equation(a, b, c)
        if type(actual) == float:
            assert actual == expected
        else:
            assert actual[0] in expected and actual[1] in expected


@pytest.mark.parametrize("input_user, expected", main_scenario_arr)
def test_main_scenario(input_user, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: input_user)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    output = output.rstrip("\n").split(" ")

    if len(output) == 1:
        assert float(output[0]) == expected
    else:
        assert float(output[0]) in expected and float(output[1]) in expected
