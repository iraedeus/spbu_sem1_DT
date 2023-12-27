import random

import pytest
from src.homework.homework_6.avl_tree import *


def create_test_tree(keys: list[int], to_balance=True) -> TreeMap:
    tree = create_tree_map()
    for key in keys:
        put(tree, key, key, to_balance=to_balance)
    return tree


def create_balance_test_tree(keys):
    tree = create_tree_map()
    for key in keys:
        put(tree, key, key)


@pytest.mark.parametrize("keys, expected", [([], True), ([4, 6, 3], False)])
def test_is_tree_empty(keys, expected):
    assert is_tree_map_empty(create_test_tree(keys)) == expected


@pytest.mark.parametrize(
    "size",
    [(100), (50), (20)],
)
def test_put(size):
    tree = create_tree_map()

    def check(tree_node):
        assert -2 < balance_factor(tree_node) < 2
        if tree_node.left is not None:
            check(tree_node.left)
            assert tree_node.left.key < tree_node.key
        if tree_node.right is not None:
            check(tree_node.right)
            assert tree_node.right.key > tree_node.key

    for i in range(size):
        key_value = random.randint(0, 10000)
        put(tree, key_value, key_value)
        check(tree.root)


@pytest.mark.parametrize(
    "keys, key, expected",
    [
        ([50, 30, 40, 70, 60, 80], 30, [[40, 50, 60, 70, 80], 30]),
        (
            [5, 2, 1, 3, 4, 7, 6, 9, 8, 10],
            2,
            [[1, 3, 4, 5, 6, 7, 8, 9, 10], 2],
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
    output_tree = TreeMap(root=node)
    assert traverse(output_tree, "inorder") == expected


@pytest.mark.parametrize("keys, key, expected", [([4, 66, 5, 3], 3, 3)])
def test_get_value(keys, key, expected):
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
            [5, 1, 4, 20, 10, 17, 35, 31, 99],
            "preorder",
        ),
        ([8, 3, 10, 1, 6, 14, 4, 7, 13], [8, 3, 1, 6, 4, 7, 13, 10, 14], "preorder"),
        ([1, 3, 4, 6, 88], [3, 1, 6, 4, 88], "preorder"),
        (
            [20, 5, 30, 1, 15, 25, 40, 9, 7, 12],
            [20, 9, 5, 1, 7, 15, 12, 30, 25, 40],
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
            [4, 1, 17, 10, 31, 99, 35, 20, 5],
            "postorder",
        ),
        ([8, 3, 10, 1, 6, 14, 4, 7, 13], [1, 4, 7, 6, 3, 10, 14, 13, 8], "postorder"),
        ([1, 3, 4, 6, 88], [1, 4, 88, 6, 3], "postorder"),
        (
            [20, 5, 30, 1, 15, 25, 40, 9, 7, 12],
            [1, 7, 5, 12, 15, 9, 25, 40, 30, 20],
            "postorder",
        ),
    ],
)
def test_traverse(keys, expected, order):
    assert traverse(create_test_tree(keys), order) == expected


@pytest.mark.parametrize(
    "keys, key, expected",
    [
        ([5, 3, 6, 1, 2, 4, 6, 10, 8], 4, 4),
        ([20, 5, 1, 15, 9, 7, 12, 30, 25, 40], 6, 7),
        ([40, 25, 10, 3, 17, 32, 30, 38, 78, 50, 93], 90, 93),
    ],
)
def test_get_lower_bound(keys, key, expected):
    tree = create_test_tree(keys)

    assert get_lower_bound(tree, key) == expected


@pytest.mark.parametrize(
    "keys, key, expected",
    [
        ([5, 3, 6, 1, 2, 4, 10, 8], 4, 5),
        ([1000, 70, 2000, 35, 71, 1500, 3000, 1250, 1750, 2500, 3500], 1750, 2000),
        ([20, 5, 1, 15, 9, 7, 12, 30, 25, 40], 1, 5),
        ([40, 25, 10, 3, 17, 32, 30, 38, 78, 50, 93], 15, 17),
    ],
)
def test_get_upper_bound(keys, key, expected):
    tree = create_test_tree(keys)

    assert get_upper_bound(tree, key) == expected


@pytest.mark.parametrize(
    "keys, expected",
    [
        ([5, 3, 6, 1, 2, 4, 10, 8], 10),
        ([20, 5, 1, 15, 9, 7, 12, 30, 25, 40], 40),
        ([40, 25, 10, 3, 17, 32, 30, 38, 78, 50, 93], 93),
    ],
)
def test_get_maximum(keys, expected):
    tree = create_test_tree(keys)

    assert get_maximum(tree) == expected


@pytest.mark.parametrize(
    "keys, expected",
    [
        ([5, 3, 6, 1, 2, 4, 6, 10, 8], 1),
        ([20, 5, 1, 15, 9, 7, 12, 30, 25, 40], 1),
        ([40, 25, 10, 3, 17, 32, 30, 38, 78, 50, 93], 3),
    ],
)
def test_get_minimum(keys, expected):
    tree = create_test_tree(keys)

    assert get_minimum(tree) == expected


@pytest.mark.parametrize(
    "keys, expected",
    [([5, 3, 1, 4], [3, 1, 5, 4]), ([10, 5, 6, 1, 2], [5, 1, 2, 10, 6])],
)
def test_right_rotate(keys, expected):
    tree = create_test_tree(keys, to_balance=False)
    tree.root = right_small_rotate(tree.root)

    assert traverse(tree, "preorder") == expected


@pytest.mark.parametrize(
    "keys, expected",
    [
        ([7, 2, 10, 20, 15], [10, 7, 2, 20, 15]),
        ([50, 100, 75, 120], [100, 50, 75, 120]),
    ],
)
def test_left_rotate(keys, expected):
    tree = create_test_tree(keys, to_balance=False)
    tree.root = left_small_rotate(tree.root)

    assert traverse(tree, "preorder") == expected
