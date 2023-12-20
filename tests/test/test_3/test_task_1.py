import pytest
from src.test.test_3.task_1 import *
from io import StringIO


@pytest.mark.parametrize(
    "input, expected",
    [
        (3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    ],
)
def test_create_list(input, expected):
    assert create_list(input) == expected


@pytest.mark.parametrize("input", [(0), (-21), (100000)])
def test_exception_create_list(input):
    with pytest.raises(ValueError):
        create_list(input)


@pytest.mark.parametrize(
    "input, expected",
    [([[0, 0, 1], [0, 0, 1], [0, 0, 0]], [[1, 0, 1], [1, 0, 1], [0, 0, 0]])],
)
def test_horizontal_symmetry(input, expected):
    assert vertical_symmetry(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [([[0, 0, 1], [0, 0, 1], [0, 0, 0]], [[0, 0, 1], [0, 0, 1], [0, 0, 1]])],
)
def test_angle_symmetry(input, expected):
    assert horizontal_symmetry(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [([[0, 0, 1], [0, 0, 1], [1, 1, 0]], "     █\n     █\n █ █  \n\n")],
)
def test_print_sprite(input, expected, monkeypatch):
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    print_sprite(input)

    output = fake_output.getvalue()
    assert output == expected


@pytest.mark.parametrize("input_user", [["10", "", "Exit"], ["15", "", "Exit"]])
def test_main_scenario(input_user, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: input_user.pop(0))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue().rstrip("\n").split("\n")

    size = len(output)
    for i in range(size):
        for j in range(size):
            current_char = output[i][j * 2 : j * 2 + 2]
            vertical_symmetry_char = output[i][(size - j - 1) * 2 : (size - j) * 2]
            horizontal_symmetry_char = output[size - i - 1][j * 2 : j * 2 + 2]
            assert (current_char == vertical_symmetry_char) or (
                current_char == horizontal_symmetry_char
            )
