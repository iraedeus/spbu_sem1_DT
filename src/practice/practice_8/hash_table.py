from dataclasses import dataclass

SIZE = 1024


@dataclass
class HashTable:
    items: list[dict | None]
    keys: set
    size: int


def create_hash_table() -> HashTable:
    table = HashTable(items=[None] * SIZE, keys=set(), size=0)
    return table


def is_hashable(value) -> bool:
    try:
        hash(value)
    except TypeError:
        return False
    return True


def delete_hash_table(table: HashTable):
    for key in table.keys:
        index = hash(key) % SIZE
        table.items[index] = None
    del table


def put(table: HashTable, key, value):
    if not is_hashable(key):
        raise ValueError("Unhashable key")

    index = hash(key) % SIZE

    if table.items[index] is None:
        table.items[index] = {key: value}
    else:
        table.items[index][key] = value
    table.size += 1
    table.keys.add(key)


def remove(table: HashTable, key):
    if not is_hashable(key):
        raise ValueError("Unhashable key")

    index = hash(key) % SIZE
    if not has_key(table, key):
        raise ValueError
    else:
        value = table.items[index][key]
        del table.items[index][key]
        table.size -= 1
        table.keys.remove(key)

        return value


def get(table: HashTable, key):
    if not is_hashable(key):
        raise ValueError("Unhashable key")

    index = hash(key) % SIZE

    if table.items[index] is None:
        raise ValueError(f"There is no value with this key {key}")
    else:
        try:
            return table.items[index][key]
        except:
            raise ValueError(f"There is no value with this key {key}")


def has_key(table: HashTable, key) -> bool:
    if not is_hashable(key):
        raise ValueError("Unhashable key")

    index = hash(key) % SIZE
    if table.items[index] is None:
        return False
    else:
        return key in table.items[index].keys()


def items(table: HashTable) -> list[tuple]:
    output = []
    for key in table.keys:
        output.append((key, get(table, key)))

    return output
