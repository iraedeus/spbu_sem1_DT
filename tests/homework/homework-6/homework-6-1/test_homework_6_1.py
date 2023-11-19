import pytest
from src.homework.homework_6.homework_6_1.homework_6_1 import *


def create_test_storage(sizes: list) -> TreeMap:
    storage = create_tree_map()
    for size in sizes:
        add(storage, size, 1)
    return storage


@pytest.mark.parametrize("size, expected", [(5, 1), (6, 2)])
def test_add(size, expected):
    storage = create_tree_map()
    put(storage, 6, 1)
    add(storage, size, 1)

    assert get_value(storage, size) == expected


@pytest.mark.parametrize(
    "sizes, size, expected", [([122, 122, 122, 89, 89], 122, 3), ([893, 77, 3], 100, 0)]
)
def test_get_size(sizes, size, expected):
    storage = create_test_storage(sizes)
    assert get_size(storage, size) == expected


@pytest.mark.parametrize(
    "sizes, size, expected", [([3, 3, 3, 78, 22], 3, 2), ([399, 100, 8], 100, 0)]
)
def test_select_if_exist(sizes, size, expected):
    storage = create_test_storage(sizes)
    select(storage, size)

    assert get_size(storage, size) == expected


@pytest.mark.parametrize(
    "sizes, size", [([54, 44, 3, 3], 9999), ([938, 3833, 3], 9999)]
)
def test_select_if_not_exist(sizes, size):
    storage = create_test_storage(sizes)
    assert select(storage, size) == "SORRY"
