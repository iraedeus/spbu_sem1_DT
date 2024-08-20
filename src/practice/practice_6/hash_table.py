from dataclasses import dataclass
from typing import Callable, Any

DEFAULT_HASHTABLE_SIZE = 1024
LOAD_FACTOR_THRESHOLD = 0.7


@dataclass
class HashTable:
    items: list[list[tuple] | None]
    keys: list
    hash_fn: Callable[[Any], int]
    size: int = DEFAULT_HASHTABLE_SIZE


def create_hash_table() -> HashTable:
    table = HashTable(items=[], keys=list(), size=DEFAULT_HASHTABLE_SIZE, hash_fn=hash)
    for _ in range(DEFAULT_HASHTABLE_SIZE):
        empty_cell = []
        table.items.append(empty_cell)
    return table


def get_index(table: HashTable, key):
    return table.hash_fn(key) % table.size


def delete_hash_table(table: HashTable):
    for key in table.keys:
        index = get_index(table, key)
        table.items[index] = None
    del table


def check_cell(cell, key):
    for i in cell:
        if i[0] == key:
            return True
    return False


def put(table: HashTable, key, value):
    def add_value(cell, key, value):
        for i in range(len(cell)):
            if key == cell[i][0]:
                del cell[i]
                break
        cell.append((key, value))

    index = get_index(table, key)
    cell = table.items[index]

    if not check_cell(cell, key):
        table.keys.append(key)

    add_value(cell, key, value)

    if is_need_resize(table):
        resize(table)


def remove(table: HashTable, key):
    def remove_in_cell(cell, key):
        value = 0
        for i in range(len(cell)):
            if cell[i][0] == key:
                value = cell[i][1]
                del cell[i]

        return value

    index = get_index(table, key)
    cell = table.items[index]

    if not has_key(table, key):
        raise ValueError(f"There is no value with this key {key}")
    else:
        value = remove_in_cell(cell, key)


def get(table: HashTable, key):
    def get_value_in_cell(cell, key):
        for item in cell:
            if key == item[0]:
                return item[1]
        raise ValueError(f"There is no value with this key {key}")

    index = get_index(table, key)
    cell = table.items[index]

    return get_value_in_cell(cell, key)


def has_key(table: HashTable, key) -> bool:
    def is_key_in_cell(cell, key):
        for item in cell:
            if key == item[0]:
                return True
        return False

    index = get_index(table, key)
    return is_key_in_cell(table.items[index], key)


def items(table: HashTable) -> list[tuple]:
    output = []
    for cell in table.items:
        if cell != []:
            for item in cell:
                output.append(item)
    return output


def load_factor(table):
    return len(table.keys) / table.size


def is_need_resize(table) -> bool:
    return load_factor(table) > LOAD_FACTOR_THRESHOLD


def resize(table: HashTable):
    new_size = table.size * 2
    global DEFAULT_HASHTABLE_SIZE
    DEFAULT_HASHTABLE_SIZE = new_size
    new_table = create_hash_table()

    for key in table.keys:
        value = get(table, key)
        put(new_table, key, value)

    table.size = new_size
    table.items = new_table.items
