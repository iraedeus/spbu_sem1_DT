import pytest
from src.homework.homework_6.homework_6_2.homework_6_2 import *


def create_test_storage(selections):
    directory = create_tree_map()
    for sample in selections:
        address = sample[0].split(" ")
        create(directory, address, sample[1])
    return directory


@pytest.mark.parametrize(
    "selections, expected",
    [
        (
            [("obed 12 2", 2), ("obed 12 3", 3), ("zavtrak 2 1", 4)],
            [(12, [(2, 2), (3, 3)]), (2, [(1, 4)])],
        ),
        ([("ujin 12 3", 4), ("ujin 13 3", 7)], [(12, [(3, 4)]), (13, [(3, 7)])]),
    ],
)
def test_create(selections, expected):
    directory = create_test_storage(selections)
    streets = traverse(directory, "inorder")
    houses = list(map(lambda item: traverse(item[1], "inorder"), streets))
    output = []
    for item in houses:
        output += item

    assert output == expected


@pytest.mark.parametrize(
    "selections, address, expected",
    [
        ([("bbb 12 4", 102), ("aaa 12 3", 101), ("aaa 12 2", 100)], "aaa 12 2", 100),
        ([("obed 13 3", 8)], "obed 13 4", None),
    ],
)
def test_get(selections, address, expected):
    directory = create_test_storage(selections)
    address = address.split()

    assert get(directory, address) == expected


@pytest.mark.parametrize(
    "selections, old_name, new_name, address, expected",
    [
        (
            [("obed 12 2", 10), ("obed 13 4", 100)],
            "obed",
            "zavtrak",
            "zavtrak 12 2",
            10,
        ),
        ([("obed 12 2", 10), ("obed 13 4", 100)], "obed", "zavtrak", "obed 12 2", None),
    ],
)
def test_rename(selections, old_name, new_name, address, expected):
    directory = create_test_storage(selections)
    address = address.split()
    rename(directory, old_name, new_name)

    assert get(directory, address) == expected


@pytest.mark.parametrize(
    "selections, address, expected",
    [
        (
            [("obed 12 3", 10), ("obed 12 4", 22), ("zavtrak 10 2", 11)],
            "obed 12 4",
            [(12, [(3, 10)]), (10, [(2, 11)])],
        ),
        (
            [("obed 12 3", 10), ("obed 12 4", 22), ("zavtrak 10 2", 11)],
            "zavtrak 10 2",
            [(12, [(3, 10), (4, 22)])],
        ),
    ],
)
def test_delete_block(selections, address, expected):
    directory = create_test_storage(selections)
    address = address.split()
    delete_block(directory, address)

    streets = traverse(directory, "inorder")
    houses = list(map(lambda item: traverse(item[1], "inorder"), streets))
    output = []
    for item in houses:
        output += item

    assert output == expected


@pytest.mark.parametrize(
    "selections, address, expected",
    [
        (
            [("obed 12 3", 10), ("obed 12 4", 22), ("zavtrak 10 2", 11)],
            "obed 12",
            [(10, [(2, 11)])],
        ),
        (
            [("obed 12 3", 10), ("obed 12 4", 22), ("zavtrak 10 2", 11)],
            "zavtrak 10",
            [(12, [(3, 10), (4, 22)])],
        ),
    ],
)
def test_delete_house(selections, address, expected):
    directory = create_test_storage(selections)
    address = address.split()
    delete_house(directory, address)

    streets = traverse(directory, "inorder")
    houses = list(map(lambda item: traverse(item[1], "inorder"), streets))
    output = []
    for item in houses:
        output += item

    assert output == expected


@pytest.mark.parametrize(
    "selections, street, expected",
    [
        (
            [("obed 11 3", 10), ("obed 12 4", 22), ("zavtrak 10 2", 11)],
            "obed",
            [(10, [(2, 11)])],
        ),
        (
            [("obed 11 3", 10), ("obed 12 4", 22), ("zavtrak 10 2", 11)],
            "zavtrak",
            [(11, [(3, 10)]), (12, [(4, 22)])],
        ),
    ],
)
def test_delete_street(selections, street, expected):
    directory = create_test_storage(selections)
    delete_street(directory, street)

    streets = traverse(directory, "inorder")
    houses = list(map(lambda item: traverse(item[1], "inorder"), streets))
    output = []
    for item in houses:
        output += item

    assert output == expected


@pytest.mark.parametrize(
    "selection, left_address, right_address, expected",
    [
        (
            [("aaa 11 3", 10), ("aaa 12 4", 22), ("bbb 10 2", 11)],
            "aaa 11 4",
            "bbb 11 1",
            ["aaa 12 4\n", "bbb 10 2\n"],
        ),
        (
            [("obed 11 3", 10), ("obed 12 4", 22), ("zavtrak 10 2", 11)],
            "zzzz 10000 0",
            "zzzzzzzzz 10000 10",
            [],
        ),
    ],
)
def test_list(selection, left_address, right_address, expected):
    directory = create_test_storage(selection)
    left_address = left_address.split()
    right_address = right_address.split()

    assert print_list(directory, left_address, right_address) == expected


def test_static(monkeypatch):
    directory = create_tree_map()
    monkeypatch.setattr("builtins.input", lambda _: "streets_logs.txt")
    static(directory)

    results = find_file("streets_results.txt", "/")

    with open(results, "r") as results, open(OUTPUT_FILE, "r") as output:
        for line in results:
            assert line == output.readline()
