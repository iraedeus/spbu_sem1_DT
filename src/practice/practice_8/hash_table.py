from dataclasses import dataclass


@dataclass
class HashTable:
    items: list[list[tuple] | list[None]]
    keys: list
    size: int = 1024


def create_hash_table(size) -> HashTable:
    table = HashTable(items=[], keys=list(), size=size)
    for i in range(table.size):
        table.items.append([])
    return table


def delete_hash_table(table: HashTable):
    for key in table.keys:
        index = hash(key) % table.size
        table.items[index] = list()
    del table


def put(table: HashTable, key, value):
    def replace_value(cell, key, value):
        for i in range(len(cell)):
            if key == cell[i][0]:
                del cell[i]
                break
        cell.append((key, value))

    key_value_tuple = (key, value)
    index = hash(key) % table.size
    cell = table.items[index]

    if has_key(table, key):
        replace_value(cell, key, value)
    else:
        cell.append(key_value_tuple)

    if key not in table.keys:
        table.keys.append(key)

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

    def del_key(table, key):
        for i in range(len(table.keys)):
            if table.keys[i] == key:
                del table.keys[i]

    index = hash(key) % table.size
    cell = table.items[index]
    if not has_key(table, key):
        raise ValueError
    else:
        del_key(table, key)
        return remove_in_cell(cell, key)


def get(table: HashTable, key):
    def get_value_in_cell(cell, key):
        for item in cell:
            if key == item[0]:
                return item[1]
        raise ValueError

    index = hash(key) % table.size

    try:
        return get_value_in_cell(table.items[index], key)
    except ValueError:
        raise ValueError(f"There is no value with this key {key}")


def has_key(table: HashTable, key) -> bool:
    def is_key_in_cell(cell, key):
        for item in cell:
            if key == item[0]:
                return True
        return False

    index = hash(key) % table.size
    return is_key_in_cell(table.items[index], key)


def items(table: HashTable) -> list[tuple]:
    output = []
    for key in table.keys:
        output.append((key, get(table, key)))

    return output


def is_need_resize(table) -> bool:
    return len(table.keys) / table.size > 0.7


def resize(table: HashTable):
    new_size = table.size * 2
    new_table = create_hash_table(new_size)

    for key in table.keys:
        value = get(table, key)
        put(new_table, key, value)

    table.size = new_size
    table.items = new_table.items
