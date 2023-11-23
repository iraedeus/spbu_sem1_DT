import pytest
from src.homework.homework_6.avl_tree import *


def create_test_tree(keys: list[int]) -> TreeMap:
    tree = create_tree_map()
    for key in keys:
        put(tree, key, key)
    return tree


@pytest.mark.parametrize("keys, expected", [([], True), ([4, 6, 3], False)])
def test_is_tree_empty(keys, expected):
    assert is_tree_map_empty(create_test_tree(keys)) == expected


@pytest.mark.parametrize(
    "keys, key, value, expected",
    [
        (
            [20, 5, 30, 25, 40, 1, 15, 9, 7, 12],
            26,
            200,
            [1, 5, 7, 9, 12, 15, 20, 25, 200, 30, 40],
        ),
        ([8, 3, 10, 14, 13, 1, 6, 4, 7], 8, 929, [1, 3, 4, 6, 7, 929, 10, 13, 14]),
    ],
)
def test_put(keys, key, value, expected):
    tree = create_test_tree(keys)
    put(tree, key, value)
    assert traverse(tree, "inorder", "values") == expected


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
    assert traverse(tree, "inorder", "keys") == expected[0] and value == expected[1]


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
    assert traverse(output_tree, "inorder", "keys") == expected


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
    assert traverse(create_test_tree(keys), order, "keys") == expected


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
        ([5, 3, 6, 1, 2, 4, 6, 10, 8], 4, 5),
        ([20, 5, 1, 15, 9, 7, 12, 30, 25, 40], 1, 5),
        ([40, 25, 10, 3, 17, 32, 30, 38, 78, 50, 93], 15, 17),
    ],
)
def test_get_higher_bound(keys, key, expected):
    tree = create_test_tree(keys)

    assert get_higher_bound(tree, key) == expected


@pytest.mark.parametrize(
    "keys, expected",
    [
        ([5, 3, 6, 1, 2, 4, 6, 10, 8], 10),
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
    "keys, left, right, expected",
    [
        (
            [1, 2, 3, 666, 5, 4444, 8, 300, 99, 19, 23, 60, 78, 79],
            20,
            80,
            [23, 60, 78, 79],
        ),
        ([8999, 77, 33, 2, 1, 90], 888, 999, []),
        ([1, 7, 3, 2, 5, 4, 999, 9, 10, 8], 8, 10, [9]),
    ],
)
def test_get_all(keys, left, right, expected):
    tree = create_test_tree(keys)
    all = get_all(tree, left, right)

    assert set(all) == set(expected)


@pytest.mark.parametrize(
    "keys, left, right, expected",
    [
        ([1, 2, 5, 6, 100], 101, 102, [1, 2, 5, 6, 100]),
        ([1, 100, 101, 709], 80, 110, [1, 709]),
        ([2, 4, 55, 66], 0, 100, []),
    ],
)
def test_remove_keys(keys, left, right, expected):
    tree = create_test_tree(keys)
    remove_keys(tree, left, right)
    assert traverse(tree, "inorder", "keys") == expected


@pytest.mark.parametrize(
    "tree_keys, key, expected",
    [
        ([4, 5, 6, 2, 10], 3, [[2], [4, 5, 6, 10]]),
        ([6, 33, 2, 11, 5], 900, [[2, 5, 6, 11, 33], []]),
    ],
)
def test_separate(tree_keys, key, expected):
    tree = create_test_tree(tree_keys)
    trees = split(tree, key)

    traversed_trees = [
        traverse(trees[0], "inorder", "keys"),
        traverse(trees[1], "inorder", "keys"),
    ]

    assert traversed_trees == expected


@pytest.mark.parametrize(
    "first_keys, second_keys, expected",
    [
        ([1, 2, 3], [4, 5, 7], [1, 2, 3, 4, 5, 7]),
        ([3, 6, 99], [1, 2, 44], [1, 2, 3, 6, 44, 99]),
        ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ],
)
def test_merge(first_keys, second_keys, expected):
    first_tree = create_test_tree(first_keys)
    second_tree = create_test_tree(second_keys)
    tree = merge(first_tree, second_tree)

    assert traverse(tree, "inorder", "keys") == expected
