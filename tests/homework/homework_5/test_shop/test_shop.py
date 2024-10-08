import pytest
from src.homework.homework_5.shop.shop import *


def create_test_storage(sizes: list) -> TreeMap:
    storage = create_tree_map()
    for size in sizes:
        add(storage, size, 1)
    return storage


@pytest.mark.parametrize("size, count, expected", [(5, 2, 3), (6, 1, 1)])
def test_add(size, count, expected):
    storage = create_tree_map()
    put(storage, 5, 1)

    add(storage, size, count)

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


def test_main():
    main()
    results_path = find_log("shop_results.txt", "/")
    balance_path = find_log("shop_balance.txt", "/")

    with open("output_logs.txt", "r") as output, open(results_path, "r") as results:
        for line in output:
            assert line == results.readline()

    with open("storage_remains.txt", "r") as remains, open(
        balance_path, "r"
    ) as balance:
        for line in remains:
            assert line == balance.readline()
