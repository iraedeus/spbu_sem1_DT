from dataclasses import dataclass
from typing import TypeVar, Generic, Optional
import math

V = TypeVar("V")
Key = TypeVar("Key")


@dataclass
class TreeNode(Generic[V, Key]):
    key: Key
    value: Optional
    height: int = 1
    left: Optional["TreeNode[V, Key]"] = None
    right: Optional["TreeNode[V, Key]"] = None


@dataclass
class TreeMap(Generic[V, Key]):
    root: Optional["TreeNode[V, Key]"] = None


def is_tree_map_empty(tree: TreeMap) -> bool:
    return tree.root is None


def create_tree_map() -> TreeMap:
    return TreeMap(root=None)


def delete_tree_map(tree: TreeMap):
    def delete_recursion(tree_cell: TreeNode):
        delete_recursion(tree_cell.left)
        delete_recursion(tree_cell.right)
        tree_cell.left = None
        tree_cell.right = None

    delete_recursion(tree.root)


def get_height(tree_node: TreeNode) -> int:
    if tree_node is None:
        return 0
    else:
        return tree_node.height


def balance_factor(tree_node: TreeNode) -> int:
    return get_height(tree_node.left) - get_height(tree_node.right)


def fix_height(tree_node: TreeNode):
    if tree_node is None:
        return None
    else:
        left_height = get_height(tree_node.left)
        right_height = get_height(tree_node.right)

        if left_height > right_height:
            tree_node.height = left_height + 1
        else:
            tree_node.height = right_height + 1


def put(tree: TreeMap, key: Key, value: V, to_balance=True) -> None:
    new_node = TreeNode(height=1, key=key, value=value, left=None, right=None)

    def recursion(tree_cell: TreeNode):
        if tree_cell is None:
            return new_node
        if key < tree_cell.key:
            tree_cell.left = recursion(tree_cell.left)
            if to_balance:
                tree_cell = balance(tree_cell)
            return tree_cell
        elif key > tree_cell.key:
            tree_cell.right = recursion(tree_cell.right)
            if to_balance:
                tree_cell = balance(tree_cell)
            return tree_cell
        else:
            tree_cell.value = value
            return tree_cell

    if is_tree_map_empty(tree):
        tree.root = new_node
    else:
        tree.root = recursion(tree.root)


def remove_recursion(current_node: TreeNode, key: Key):
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


def remove_if_two_children(deleted_tree_cell: TreeNode):
    def find_min_node(tree_cell: TreeNode) -> TreeNode:
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


def remove(tree: TreeMap, key: Key) -> V:
    if not has_key(tree, key):
        raise ValueError(f"Can't remove {key} key, because this key doesnt exist")
    if tree.root.left is None and tree.root.right is None:
        root = tree.root
        tree.root = None
        return root.value

    tree.root, value = remove_recursion(tree.root, key)
    return value


def get_tree_node(tree: TreeMap, key: Key) -> TreeNode:
    def recursion(tree_cell: TreeNode):
        if tree_cell is None or key == tree_cell.key:
            return tree_cell
        elif key < tree_cell.key:
            return recursion(tree_cell.left)
        elif key > tree_cell.key:
            return recursion(tree_cell.right)

    return recursion(tree.root)


def get_value(tree: TreeMap, key: Key) -> V:
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")
    return get_tree_node(tree, key).value


def has_key(tree: TreeMap, key: Key) -> bool:
    node = get_tree_node(tree, key)
    return node is not None


def _postorder_comparator(node: TreeNode):
    return filter(None, (node.left, node.right, node))


def _inorder_comparator(node: TreeNode):
    return filter(None, (node.left, node, node.right))


def _preorder_comparator(node: TreeNode):
    return filter(None, (node, node.left, node.right))


def traverse(tree: TreeMap, order: str) -> list:
    if tree.root is None:
        return []

    output = []

    def recursion(current_node: TreeNode, order_func):
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


def get_lower_bound(tree: TreeMap, key: Key) -> Key:
    highers = [math.inf]
    current_node = tree.root
    while True:
        if current_node.key >= key:
            highers.append(current_node.key)

        if key < current_node.key:
            current_node = current_node.left
        elif key >= current_node.key:
            current_node = current_node.right

        if current_node is None:
            break
    return min(highers)


def get_upper_bound(tree: TreeMap, key: Key) -> Key:
    highers = [math.inf]
    current_node = tree.root
    while True:
        if current_node.key > key:
            highers.append(current_node.key)

        if key < current_node.key:
            current_node = current_node.left
        elif key >= current_node.key:
            current_node = current_node.right

        if current_node is None:
            break
    return min(highers)


def get_maximum(tree: TreeMap) -> Key:
    if tree.root is None:
        raise ValueError("Tree is empty")

    def recursion(current_node: TreeNode) -> Key:
        if current_node.right is not None:
            return recursion(current_node.right)
        else:
            return current_node.key

    return recursion(tree.root)


def get_minimum(tree: TreeMap) -> Key:
    if tree.root is None:
        raise ValueError("Tree is empty")

    def recursion(current_node: TreeNode) -> Key:
        if current_node.left is not None:
            return recursion(current_node.left)
        else:
            return current_node.key

    return recursion(tree.root)


def left_small_rotate(tree_node: TreeNode) -> TreeNode:
    right_child = tree_node.right

    tree_node.right = right_child.left
    right_child.left = tree_node

    tree_node = right_child

    fix_height(tree_node.left)
    fix_height(tree_node.right)
    fix_height(tree_node)
    return tree_node


def right_small_rotate(tree_node: TreeNode) -> TreeNode:
    left_child = tree_node.left

    tree_node.left = left_child.right
    left_child.right = tree_node

    tree_node = left_child

    fix_height(tree_node.left)
    fix_height(tree_node.right)
    fix_height(tree_node)
    return tree_node


def balance(tree_node: TreeNode) -> TreeNode:
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
