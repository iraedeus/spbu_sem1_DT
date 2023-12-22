import math
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional

V = TypeVar("V")


@dataclass
class TreeNode(Generic[V]):
    key: Optional[int]
    value: Optional[V]
    height: int = 1
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
    if tree_node is not None:
        left_height = get_height(tree_node.left)
        right_height = get_height(tree_node.right)

        if left_height > right_height:
            tree_node.height = left_height + 1
        else:
            tree_node.height = right_height + 1


def put(tree: TreeMap[V], key: int, value: V) -> None:
    new_node = TreeNode(height=1, key=key, value=value, left=None, right=None)

    def recursion(tree_cell: TreeNode[V]):
        if tree_cell is None:
            return new_node
        if key < tree_cell.key:
            tree_cell.left = recursion(tree_cell.left)
            tree_cell = balance(tree_cell)
            return tree_cell
        elif key > tree_cell.key:
            tree_cell.right = recursion(tree_cell.right)
            tree_cell = balance(tree_cell)
            return tree_cell
        else:
            tree_cell.value = value
            return tree_cell

    if is_tree_map_empty(tree):
        tree.root = new_node
    else:
        tree.root = recursion(tree.root)
    tree.size += 1


def remove_recursion(current_node: TreeNode[V], key: int):
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
    def find_min_node(tree_cell: TreeNode[V]) -> TreeNode[V]:
        current_node = tree_cell
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    value = deleted_tree_cell.value

    min_node = find_min_node(deleted_tree_cell.right)

    remove_recursion(deleted_tree_cell, min_node.key)

    deleted_tree_cell.key = min_node.key
    deleted_tree_cell.value = min_node.value

    return deleted_tree_cell, value


def remove(tree: TreeMap[V], key: int) -> V:
    if not has_key(tree, key):
        raise ValueError(f"Can't remove {key} key, because this key doesnt exist")
    if tree.size == 1:
        root = tree.root

        tree.root = None
        tree.size -= 1
        return root.value

    tree.root, value = remove_recursion(tree.root, key)
    return value


def get_tree_node(tree: TreeMap[V], key: int) -> TreeNode[V]:
    def recursion(tree_cell: TreeNode):
        if tree_cell is None or key == tree_cell.key:
            return tree_cell
        elif key < tree_cell.key:
            return recursion(tree_cell.left)
        elif key > tree_cell.key:
            return recursion(tree_cell.right)

    return recursion(tree.root)


def get_value(tree: TreeMap[V], key: int) -> V:
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")
    return get_tree_node(tree, key).value


def has_key(tree: TreeMap[V], key: int) -> bool:
    node = get_tree_node(tree, key)
    return node is not None


def _postorder_comparator(node: TreeNode[V]):
    return filter(None, (node.left, node.right, node))


def _inorder_comparator(node: TreeNode[V]):
    return filter(None, (node.left, node, node.right))


def _preorder_comparator(node: TreeNode[V]):
    return filter(None, (node, node.left, node.right))


def traverse(tree: TreeMap[V], order: str) -> list[V]:
    if tree.size == 0:
        return []

    output = []

    def recursion(current_node: TreeNode[V], order_func):
        node_order = order_func(current_node)
        for node in node_order:
            if node is not current_node:
                recursion(node, order_func)
            else:
                output.append(current_node.value)

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
    return output


def get_lower_bound(tree: TreeMap[V], key: int) -> int:
    output = get_maximum(tree) + 1

    def recursion(current_node: TreeNode[V], key: int):
        nonlocal output

        if key < current_node.key and current_node.left is not None:
            recursion(current_node.left, key)
        elif key > current_node.key and current_node.right is not None:
            recursion(current_node.right, key)

        if current_node.key >= key:
            output = min(current_node.key, output)

    recursion(tree.root, key)
    return output


def get_higher_bound(tree: TreeMap[V], key: int) -> int:
    highers = []

    def recursion(current_node: TreeNode[V], key: int, highers: list):
        if key < current_node.key and current_node.left is not None:
            recursion(current_node.left, key, highers)
        elif key > current_node.key and current_node.right is not None:
            recursion(current_node.right, key, highers)

        if current_node.key > key:
            highers.append(current_node.key)

    recursion(tree.root, key, highers)
    return min(highers)


def get_maximum(tree: TreeMap[V]) -> int:
    if tree.root is None:
        raise ValueError("Tree is empty")

    def recursion(current_node: TreeNode[V]) -> int:
        if current_node.right is not None:
            return recursion(current_node.right)
        else:
            return current_node.key

    return recursion(tree.root)


def get_minimum(tree: TreeMap[V]) -> int:
    if tree.root is None:
        raise ValueError("Tree is empty")

    def recursion(current_node: TreeNode[V]) -> int:
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

    fix_height(tree_node.left)
    fix_height(tree_node.right)
    fix_height(tree_node)
    return tree_node


def right_small_rotate(tree_node: TreeNode[V]) -> TreeNode[V]:
    left_child = tree_node.left

    tree_node.left = left_child.right
    left_child.right = tree_node

    tree_node = left_child

    fix_height(tree_node.left)
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
