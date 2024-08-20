import pytest
from src.practice.practice_6.hash_table import *


def create_test_hash_table(keys_values):
    table = create_hash_table()

    for key, item in keys_values:
        put(table, key, item)

    return table


@pytest.mark.parametrize(
    "keys_values",
    [[["abc", 100], ["dbc", 200], ["obed", 1000]], (["zavtrak", 999], [8383, 11])],
)
def test_delete_hash_table(keys_values):
    table = create_test_hash_table(keys_values)

    table = delete_hash_table(table)
    assert table is None


@pytest.mark.parametrize(
    "keys_values, key, value, expected",
    [
        (
            [["string", 78], [50, "obed"]],
            "string",
            "string",
            [("string", "string"), (50, "obed")],
        ),
        (
            [["test", "test"], ["matmeh", "luchshe vseh"], [0, 9]],
            "90",
            90,
            [("test", "test"), ("matmeh", "luchshe vseh"), (0, 9), ("90", 90)],
        ),
    ],
)
def test_put_different(keys_values, key, value, expected):
    table = create_test_hash_table(keys_values)
    put(table, key, value)
    all_items = items(table)

    assert set(all_items) == set(expected)


@pytest.mark.parametrize(
    "keys_values, key, value, expected",
    [
        (
            [["string", 78], [50, "obed"]],
            150,
            "string",
            [("string", 78), (50, "obed"), (150, "string")],
        )
    ],
)
def test_put_similar(keys_values, key, value, expected):
    table = create_test_hash_table(keys_values)

    put(table, key, value)
    all_items = items(table)

    assert set(all_items) == set(expected)


@pytest.mark.parametrize(
    "keys_values, key, expected",
    [
        (
            [[False, True], [True, False], ["python", 100]],
            "python",
            [(True, False), (False, True)],
        ),
        ([[False, True], [True, False]], True, [(False, True)]),
    ],
)
def test_remove(keys_values, key, expected):
    table = create_test_hash_table(keys_values)
    remove(table, key)
    all_items = items(table)
    assert set(all_items) == set(expected)


@pytest.mark.parametrize(
    "keys_values, key",
    [
        ([[False, True], [True, False]], "python"),
    ],
)
def test_remove_exception(keys_values, key):
    table = create_test_hash_table(keys_values)
    with pytest.raises(ValueError):
        remove(table, key)


@pytest.mark.parametrize(
    "keys_values, key, expected",
    [
        ((["test", "test"], ["matmeh", "luchshe vseh"]), "matmeh", "luchshe vseh"),
        ((["abc", 100], ["dbc", 200], ["obed", 1000]), "obed", 1000),
    ],
)
def test_get(keys_values, key, expected):
    table = create_test_hash_table(keys_values)
    assert get(table, key) == expected


@pytest.mark.parametrize(
    "keys_values, key",
    [
        ([[False, "False"], ["True", True], ["100", 100]], "python"),
    ],
)
def test_get_exception(keys_values, key):
    table = create_test_hash_table(keys_values)
    with pytest.raises(ValueError):
        get(table, key)


@pytest.mark.parametrize(
    "keys_values, key, expected",
    [
        ([["ofc", False], ["yes", True]], "yes", True),
        ([["ofc", False], ["yes", True]], "no", False),
        ([[50, False]], 150, False),
        ([[50, False], [150, True]], 150, True),
    ],
)
def test_has_key(keys_values, key, expected):
    table = create_test_hash_table(keys_values)
    assert has_key(table, key) == expected


@pytest.mark.parametrize("key", [(list())])
def test_has_key_exception(key):
    table = create_hash_table()
    with pytest.raises(TypeError):
        has_key(table, key)


@pytest.mark.parametrize(
    "keys_values, expected",
    [
        (
            [["abc", 100], ["dbc", 200], ["obed", 1000]],
            [("abc", 100), ("dbc", 200), ("obed", 1000)],
        )
    ],
)
def test_items(keys_values, expected):
    table = create_test_hash_table(keys_values)

    all_items = items(table)
    assert set(all_items) == set(expected)
