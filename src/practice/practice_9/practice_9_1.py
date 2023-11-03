from dataclasses import dataclass
from typing import TypeVar, Generic, Optional

V = TypeVar("V")


@dataclass
class TreeNode(Generic[V]):
    key: int
    value: V
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
        left_child = tree_cell.left
        right_child = tree_cell.right

        if left_child is None and right_child is None:
            del tree_cell
        elif right_child is not None:
            delete_recursion(tree_cell.right)
            del tree_cell
        elif left_child is not None:
            delete_recursion(tree_cell.left)
            del tree_cell

    delete_recursion(tree.root)


def put(tree: TreeMap[V], key: int, value: V) -> None:
    new_node = TreeNode(key=key, value=value, left=None, right=None)

    def recursion(tree_cell: TreeNode[V]):
        if key < tree_cell.key:
            if tree_cell.left is None:
                tree_cell.left = new_node
            else:
                recursion(tree_cell.left)
        elif key > tree_cell.key:
            if tree_cell.right is None:
                tree_cell.right = new_node
            else:
                recursion(tree_cell.right)
        else:
            tree_cell.value = value

    if is_tree_map_empty(tree):
        tree.root = new_node
    else:
        root = tree.root
        recursion(root)
    tree.size += 1


def find_min_node(tree_cell: TreeNode[V]) -> TreeNode[V]:
    def find_recursion(current_node: TreeNode[V], parent):
        if current_node.left is None:
            return current_node
        else:
            find_recursion(current_node.left, current_node)

    return find_recursion(tree_cell, None)


def remove_if_two_children(deleted_tree_cell: TreeNode[V]):
    value = deleted_tree_cell.value

    min_node = find_min_node(deleted_tree_cell.right)
    tree = TreeMap(root=deleted_tree_cell)
    remove(tree, min_node.key)

    deleted_tree_cell = tree.root
    deleted_tree_cell.key = min_node.key
    deleted_tree_cell.value = min_node.value

    return deleted_tree_cell, value


def remove(tree: TreeMap[V], key: int) -> V:
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")
    if tree.size == 1:
        root = tree.root

        tree.root = None
        tree.size -= 1
        return root.value

    def remove_recursion(current_node: TreeNode[V], key: int):
        if current_node.key < key:
            new_right_child, value = remove_recursion(current_node.right, key)
            current_node.right = new_right_child
            return current_node, value
        elif current_node.key > key:
            new_left_child, value = remove_recursion(current_node.left, key)
            current_node.left = new_left_child
            return current_node, value
        else:
            if current_node.left is None and current_node.right is None:
                return None, current_node.value
            elif current_node.left is None or current_node.right is None:
                if current_node.left is None:
                    return current_node.right, current_node.value
                else:
                    return current_node.left, current_node.value
            else:
                output = remove_if_two_children(current_node)
                return output[0], output[1]

    tree.root, value = remove_recursion(tree.root, key)
    return value


def get_tree_node(tree: TreeMap[V], key: int) -> TreeNode[V]:
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")

    def recursion(tree_cell: TreeNode) -> TreeNode:
        if key == tree_cell.key:
            return tree_cell

        if key < tree_cell.key and tree_cell.left is not None:
            return recursion(tree_cell.left)
        elif key > tree_cell.key and tree_cell.right is not None:
            return recursion(tree_cell.right)

    output = recursion(tree.root)
    if output is None:
        raise ValueError("Tree doesn't have this key")
    return output


def get_value(tree: TreeMap[V], key: int) -> V:
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")
    return get_tree_node(tree, key).value


def has_key(tree: TreeMap[V], key: int) -> bool:
    output = False

    def recursion(tree_cell: TreeNode[V], key: int):
        if key == tree_cell.key:
            nonlocal output
            output = True
        if key < tree_cell.key and tree_cell.left is not None:
            return recursion(tree_cell.left, key)
        elif key > tree_cell.key and tree_cell.right is not None:
            return recursion(tree_cell.right, key)

    recursion(tree.root, key)
    return output


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
    if order == "inorder":
        recursion(tree.root, _inorder_comparator)
    if order == "postorder":
        recursion(tree.root, _postorder_comparator)

    return output
