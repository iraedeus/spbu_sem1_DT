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
    [([[0, 0, 1], [0, 0, 1], [0, 0, 0]], [[0, 0, 1], [0, 0, 1], [1, 1, 0]])],
)
def test_angle_symmetry(input, expected):
    assert angle_symmetry(input) == expected


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
