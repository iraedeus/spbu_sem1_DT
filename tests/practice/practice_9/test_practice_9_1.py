import pytest
from src.practice.practice_9.practice_9_1 import *


def create_test_tree(keys: list[int]) -> TreeMap:
    tree = create_tree_map()
    for key in keys:
        put(tree, key, key)
    return tree


@pytest.mark.parametrize(
    "keys, key, value, expected",
    [
        (
            [20, 5, 30, 25, 40, 1, 15, 9, 7, 12],
            26,
            1,
            [1, 5, 7, 9, 12, 15, 20, 25, 1, 30, 40],
        ),
        ([8, 3, 10, 14, 13, 1, 6, 4, 7], 8, 929, [1, 3, 4, 6, 7, 929, 10, 13, 14]),
    ],
)
def test_put(keys, key, value, expected):
    tree = create_test_tree(keys)
    put(tree, key, value)
    assert traverse(tree, "inorder") == expected


@pytest.mark.parametrize(
    "keys, key, expected",
    [
        ([50, 30, 40, 70, 60, 80], 30, [[40, 50, 60, 70, 80], 30]),
        (
            [50, 25, 75, 12, 30, 60, 6, 52, 70],
            25,
            [[6, 12, 30, 50, 52, 60, 70, 75], 25],
        ),
        ([6], 6, [[], 6]),
        ([6, 7, 8], 6, [[7, 8], 6]),
        ([98, 6, 4, 2], 98, [[2, 4, 6], 98]),
    ],
)
def test_remove(keys, key, expected):
    tree = create_test_tree(keys)
    value = remove(tree, key)
    assert traverse(tree, "inorder") == expected[0] and value == expected[1]


@pytest.mark.parametrize(
    "keys, key, expected",
    [
        ([8, 3, 10, 1, 6, 14, 13, 4, 7], 3, [1, 3, 4, 6, 7]),
        ([8, 3, 10, 1, 6, 14, 13, 4, 7], 1, [1]),
    ],
)
def test_get_tree_node(keys, key, expected):
    input_tree = create_test_tree(keys)
    node = get_tree_node(input_tree, key)
    output_tree = TreeMap(size=1, root=node)
    assert traverse(output_tree, "inorder") == expected


@pytest.mark.parametrize("keys, key, expected", [([4, 66, 5, 3], 3, 3)])
def test_get(keys, key, expected):
    tree = create_test_tree(keys)
    assert get_value(tree, key) == expected


@pytest.mark.parametrize("keys, key", [([98, 46, 3, 44], 45)])
def test_exception_get(keys, key):
    tree = create_test_tree(keys)
    with pytest.raises(ValueError):
        get_value(tree, key)


@pytest.mark.parametrize(
    "keys, key, expected",
    [([4, 6, 22, 78, 1, 5], 22, True), ([11, 22, 34, 1, 2, 4, 33, 90], 389, False)],
)
def test_has_key(keys, key, expected):
    assert has_key(create_test_tree(keys), key) == expected


@pytest.mark.parametrize(
    "keys, expected, order",
    [
        (
            [10, 5, 1, 4, 35, 20, 99, 31, 17],
            [10, 5, 1, 4, 35, 20, 17, 31, 99],
            "preorder",
        ),
        ([8, 3, 10, 1, 6, 14, 4, 7, 13], [8, 3, 1, 6, 4, 7, 10, 14, 13], "preorder"),
        ([1, 3, 4, 6, 88], [1, 3, 4, 6, 88], "preorder"),
        (
            [20, 5, 30, 1, 15, 25, 40, 9, 7, 12],
            [20, 5, 1, 15, 9, 7, 12, 30, 25, 40],
            "preorder",
        ),
        (
            [10, 5, 1, 4, 35, 20, 99, 31, 17],
            [1, 4, 5, 10, 17, 20, 31, 35, 99],
            "inorder",
        ),
        ([8, 3, 10, 1, 6, 14, 4, 7, 13], [1, 3, 4, 6, 7, 8, 10, 13, 14], "inorder"),
        ([1, 3, 4, 6, 88], [1, 3, 4, 6, 88], "inorder"),
        (
            [20, 5, 30, 1, 15, 25, 40, 9, 7, 12],
            [1, 5, 7, 9, 12, 15, 20, 25, 30, 40],
            "inorder",
        ),
        (
            [10, 5, 1, 4, 35, 20, 99, 31, 17],
            [4, 1, 5, 17, 31, 20, 99, 35, 10],
            "postorder",
        ),
        ([8, 3, 10, 1, 6, 14, 4, 7, 13], [1, 4, 7, 6, 3, 13, 14, 10, 8], "postorder"),
        ([1, 3, 4, 6, 88], [88, 6, 4, 3, 1], "postorder"),
        (
            [20, 5, 30, 1, 15, 25, 40, 9, 7, 12],
            [1, 7, 12, 9, 15, 5, 25, 40, 30, 20],
            "postorder",
        ),
    ],
)
def test_traverse(keys, expected, order):
    assert traverse(create_test_tree(keys), order) == expected
