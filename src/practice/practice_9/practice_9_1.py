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


def create_tree_map() -> TreeMap:
    return TreeMap(root=None, size=0)


def delete_tree_map(tree: TreeMap) -> None:
    root = tree.root

    def delete_recursion(tree_cell: TreeNode):
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

    delete_recursion(root)


def put(tree: TreeMap, key: int, value: V) -> None:
    new_node = TreeNode(key=key, value=value, left=None, right=None)

    def recursion(tree_cell: TreeNode):
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
        tree.root = TreeNode(key=key, value=value, left=None, right=None)
        tree.size += 1
    else:
        root = tree.root
        recursion(root)
        tree.size += 1


def remove_if_two_children(deleted_tree_cell: TreeNode[V]):
    value = deleted_tree_cell.value

    new_value = 0
    new_key = 0

    def recursion(current_node: TreeNode[V], parent):
        if current_node.left is None and current_node.right is None:
            nonlocal new_key, new_value
            new_key = current_node.key
            new_value = current_node.value
            parent.left = None
        else:
            recursion(current_node.left, current_node)
    deleted_tree_cell.key = new_key
    deleted_tree_cell.value = value
    recursion(deleted_tree_cell, None)
    return deleted_tree_cell, value


def remove(tree: TreeMap[V], key: int) -> V:
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")
    root = tree.root
    if tree.size == 1:
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
    root = tree.root

    def recursion(tree_cell: TreeNode) -> TreeNode:
        if key == tree_cell.key:
            return tree_cell

        if key < tree_cell.key and tree_cell.left is not None:
            return recursion(tree_cell.left)
        elif key > tree_cell.key and tree_cell.right is not None:
            return recursion(tree_cell.right)

    return recursion(root)


def get_value(tree: TreeMap[V], key: int) -> V:
    root = tree.root
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")
    return get_tree_node(tree, key).value


def has_key(tree: TreeMap[V], key: int) -> bool:
    root = tree.root
    return get_tree_node(tree, key) is not None


def _postorder_comparator(node: TreeNode[V]):
    return filter(None, (node.left, node.right, node))


def _inorder_comparator(node: TreeNode[V]):
    return filter(None, (node.left, node,  node.right))


def _preorder_comparator(node: TreeNode[V]):
    return filter(None, (node, node.left, node.right))

def traverse(tree: TreeMap, order: str) -> list[V]:
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