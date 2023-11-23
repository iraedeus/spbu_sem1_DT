from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Any

V = TypeVar("V")


@dataclass
class TreeNode(Generic[V]):
    height: int = 1
    key: Optional[Any] = None
    value: Optional[V] = None
    left: Optional["TreeNode[V]"] = None
    right: Optional["TreeNode[V]"] = None


@dataclass
class TreeMap(Generic[V]):
    root: Optional["TreeNode[V]"] = None
    size: int = 0


def is_tree_map_empty(tree: TreeMap) -> bool:
    return tree.size == 0


def create_tree_map() -> TreeMap[V]:
    return TreeMap(root=None, size=0)


def delete_tree_map(tree: TreeMap[V]):
    def delete_recursion(tree_cell: TreeNode[V]):
        delete_recursion(tree_cell.left)
        delete_recursion(tree_cell.right)
        tree_cell.left = None
        tree_cell.right = None

    delete_recursion(tree.root)


def get_height(tree_node: TreeNode[V]) -> int:
    if tree_node is None:
        return 0
    else:
        return tree_node.height


def balance_factor(tree_node: TreeNode[V]) -> int:
    return get_height(tree_node.left) - get_height(tree_node.right)


def fix_height(tree_node: TreeNode[V]):
    left_height = get_height(tree_node.left)
    right_height = get_height(tree_node.right)

    if left_height > right_height:
        tree_node.height = left_height + 1
    else:
        tree_node.height = right_height + 1


def put(tree: TreeMap[V], key, value: V) -> None:
    new_node = TreeNode(height=1, key=key, value=value, left=None, right=None)

    def recursion(parent: TreeNode[V] | None, tree_cell: TreeNode[V]):
        if key < tree_cell.key:
            if tree_cell.left is None:
                tree_cell.left = new_node
            else:
                recursion(tree_cell, tree_cell.left)
        elif key > tree_cell.key:
            if tree_cell.right is None:
                tree_cell.right = new_node
            else:
                recursion(tree_cell, tree_cell.right)
        else:
            tree_cell.value = value

        if tree_cell == tree.root:
            tree.root = balance(tree_cell)
        else:
            if parent.left == tree_cell:
                parent.left = balance(tree_cell)
            else:
                parent.right = balance(tree_cell)

    if is_tree_map_empty(tree):
        tree.root = new_node
    else:
        root = tree.root
        recursion(None, root)
    tree.size += 1


def find_min_node(tree_cell: TreeNode[V]) -> TreeNode[V]:
    def find_recursion(current_node: TreeNode[V]):
        if current_node.left is None:
            return current_node
        else:
            return find_recursion(current_node.left)

    return find_recursion(tree_cell)


def remove_recursion(current_node: TreeNode[V], key):
    if current_node.key < key:
        new_right_child, value = remove_recursion(current_node.right, key)
        current_node.right = new_right_child
        return current_node, value
    elif current_node.key > key:
        new_left_child, value = remove_recursion(current_node.left, key)
        current_node.left = new_left_child
        return current_node, value

    if current_node.left is None and current_node.right is None:
        return None, current_node.value
    elif current_node.left is None or current_node.right is None:
        if current_node.left is None:
            return current_node.right, current_node.value
        else:
            return current_node.left, current_node.value
    else:
        return remove_if_two_children(current_node)


def remove_if_two_children(deleted_tree_cell: TreeNode[V]):
    value = deleted_tree_cell.value

    min_node = find_min_node(deleted_tree_cell.right)

    remove_recursion(deleted_tree_cell, min_node.key)

    deleted_tree_cell.key = min_node.key
    deleted_tree_cell.value = min_node.value

    return deleted_tree_cell, value


def remove(tree: TreeMap[V], key) -> V:
    if not has_key(tree, key):
        raise ValueError(f"Can't remove {key} key, because this key doesnt exist")
    if tree.size == 1:
        root = tree.root

        tree.root = None
        tree.size -= 1
        return root.value

    tree.root, value = remove_recursion(tree.root, key)
    return value


def get_tree_node(tree: TreeMap[V], key) -> TreeNode[V]:
    def recursion(tree_cell: TreeNode):
        if tree_cell is None or key == tree_cell.key:
            return tree_cell
        elif key < tree_cell.key:
            return recursion(tree_cell.left)
        elif key > tree_cell.key:
            return recursion(tree_cell.right)

    return recursion(tree.root)


def get_value(tree: TreeMap[V], key) -> V:
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")
    return get_tree_node(tree, key).value


def has_key(tree: TreeMap[V], key) -> bool:
    node = get_tree_node(tree, key)
    return node is not None


def _postorder_comparator(node: TreeNode[V]):
    return filter(None, (node.left, node.right, node))


def _inorder_comparator(node: TreeNode[V]):
    return filter(None, (node.left, node, node.right))


def _preorder_comparator(node: TreeNode[V]):
    return filter(None, (node, node.left, node.right))


def traverse_keys(tuples: list[tuple]):
    return [item[0] for item in tuples]


def traverse_values(tuples: list[tuple]):
    return [item[1] for item in tuples]


def traverse(tree: TreeMap[V], order: str, field="default"):
    if tree.size == 0:
        return []

    output = []

    def recursion(current_node: TreeNode[V], order_func):
        node_order = order_func(current_node)
        for node in node_order:
            if node is not current_node:
                recursion(node, order_func)
            else:
                output.append((current_node.key, current_node.value))

    if order == "preorder":
        recursion(tree.root, _preorder_comparator)
    elif order == "inorder":
        recursion(tree.root, _inorder_comparator)
    elif order == "postorder":
        recursion(tree.root, _postorder_comparator)
    else:
        raise ValueError(
            "Unknown order, order can be one of follow: postorder, inorder, preorder"
        )

    if field == "keys":
        return traverse_keys(output)
    elif field == "values":
        return traverse_values(output)
    elif field == "default":
        return output
    else:
        raise ValueError("Unknown field, field must be keys or values")


def get_lower_bound(tree: TreeMap[V], key) -> int:
    output = get_maximum(tree) + 1

    def recursion(current_node: TreeNode[V], key):
        nonlocal output

        if key < current_node.key and current_node.left is not None:
            recursion(current_node.left, key)
        elif key > current_node.key and current_node.right is not None:
            recursion(current_node.right, key)

        if current_node.key >= key:
            output = min(current_node.key, output)

    recursion(tree.root, key)
    return output


def get_higher_bound(tree: TreeMap[V], key) -> int:
    output = get_maximum(tree)

    def recursion(current_node: TreeNode[V], key):
        nonlocal output

        if key < current_node.key and current_node.left is not None:
            recursion(current_node.left, key)
        elif key > current_node.key and current_node.right is not None:
            recursion(current_node.right, key)

        if current_node.key > key:
            output = min(current_node.key, output)

    recursion(tree.root, key)
    return output


def get_maximum(tree: TreeMap[V]):
    if tree.root is None:
        raise ValueError("Tree is empty")

    def recursion(current_node: TreeNode[V]):
        if current_node.right is not None:
            return recursion(current_node.right)
        else:
            return current_node.key

    return recursion(tree.root)


def get_minimum(tree: TreeMap[V]):
    if tree.root is None:
        raise ValueError("Tree is empty")

    def recursion(current_node: TreeNode[V]):
        if current_node.left is not None:
            return recursion(current_node.left)
        else:
            return current_node.key

    return recursion(tree.root)


def left_small_rotate(tree_node: TreeNode[V]) -> TreeNode[V]:
    right_child = tree_node.right

    tree_node.right = right_child.left
    right_child.left = tree_node

    tree_node = right_child

    if tree_node.left is not None:
        fix_height(tree_node.left)
    if tree_node.right is not None:
        fix_height(tree_node.right)
    fix_height(tree_node)
    return tree_node


def right_small_rotate(tree_node: TreeNode[V]) -> TreeNode[V]:
    left_child = tree_node.left

    tree_node.left = left_child.right
    left_child.right = tree_node

    tree_node = left_child

    if tree_node.left is not None:
        fix_height(tree_node.left)
    if tree_node.right is not None:
        fix_height(tree_node.right)
    fix_height(tree_node)
    return tree_node


def balance(tree_node: TreeNode[V]) -> TreeNode[V]:
    fix_height(tree_node)

    if balance_factor(tree_node) == 2:
        left_child = tree_node.left
        if left_child is not None and balance_factor(left_child) < 0:
            tree_node.left = left_small_rotate(left_child)
        tree_node = right_small_rotate(tree_node)
    elif balance_factor(tree_node) == -2:
        right_child = tree_node.right
        if right_child is not None and balance_factor(right_child) > 0:
            tree_node.right = right_small_rotate(right_child)
        tree_node = left_small_rotate(tree_node)

    return tree_node


def get_all(tree: TreeMap[V], left, right) -> list:
    output = []

    def recursion(tree_cell: TreeNode):
        left_child = tree_cell.left
        right_child = tree_cell.right

        if left < tree_cell.key < right:
            output.append(tree_cell.key)
            if left_child is not None:
                recursion(left_child)
            if right_child is not None:
                recursion(right_child)
        elif tree_cell.key > right and left_child is not None:
            recursion(left_child)
        elif tree_cell.key < left and right_child is not None:
            recursion(right_child)

    recursion(tree.root)
    return output


def remove_keys(tree: TreeMap[V], left, right):
    keys = get_all(tree, left, right)
    tree.size -= len(keys)
    for key in keys:
        remove(tree, key)


def split(tree: TreeMap[V], key) -> tuple[TreeMap[V], TreeMap[V]]:
    first_tree = create_tree_map()
    second_tree = create_tree_map()

    nodes = traverse(tree, "inorder")

    for node in nodes:
        if node[0] < key:
            put(first_tree, node[0], node[1])
        else:
            put(second_tree, node[0], node[1])

    return first_tree, second_tree


def merge(first_tree: TreeMap[V], second_tree: TreeMap[V]) -> TreeMap[V]:
    tree = create_tree_map()

    if first_tree.size <= second_tree.size:
        first_tree_nodes = traverse(first_tree, "inorder")
        for node in first_tree_nodes:
            put(second_tree, node[0], node[1])
        tree = second_tree
    else:
        second_tree_nodes = traverse(second_tree, "inorder")
        for node in second_tree_nodes:
            put(first_tree, node[0], node[1])
        tree = first_tree

    return tree
