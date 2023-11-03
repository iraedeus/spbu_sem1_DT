from dataclasses import dataclass
from typing import TypeVar, Generic

V = TypeVar("V")


@dataclass
class TreeNode(Generic[V]):
    key: int
    value: V
    left: "TreeNode[V]" or None
    right: "TreeNode[V]" or None


@dataclass
class TreeMap(Generic[V]):
    root: TreeNode[V] | None
    size: int


def is_tree_map_empty(tree: TreeMap) -> bool:
    return tree.size == 0


def create_tree_map() -> TreeMap:
    return TreeMap(root=None, size=0)


def delete_tree_map(tree: TreeMap) -> None:
    tree.root = None


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


def remove_if_two_child(deleted_tree_cell: TreeNode):
    right_child = deleted_tree_cell.right
    value = 0
    key = 0

    def recursion(tree_cell, parent):
        nonlocal value, key

        if tree_cell.left is not None:
            recursion(tree_cell.left, tree_cell)
        else:
            key = tree_cell.key
            value = tree_cell.value
            if parent.left == tree_cell:
                parent.left = None
            else:
                parent.right = None

    recursion(right_child, deleted_tree_cell)
    deleted_tree_cell.key = key
    deleted_tree_cell.value = value


def remove_root(tree):
    value = tree.root.value
    right_child = tree.root.right
    left_child = tree.root.left
    if right_child is None and left_child is None:
        tree.root = None
    elif right_child is None and left_child is not None:
        tree.root = left_child
    elif right_child is not None and left_child is None:
        tree.root = right_child
    else:
        remove_if_two_child(tree.root)
    return value


def remove_parent_left(tree_cell, parent):
    value = tree_cell.value
    left_child = tree_cell.left
    right_child = tree_cell.right
    if left_child is not None and right_child is None:
        parent.left = left_child
        return value
    elif right_child is not None and left_child is None:
        parent.left = right_child
        return value
    elif right_child is None and left_child is None:
        parent.left = None
        return value
    else:
        remove_if_two_child(tree_cell)
        return value


def remove_parent_right(tree_cell, parent):
    value = tree_cell.value
    left_child = tree_cell.left
    right_child = tree_cell.right
    if left_child is not None and right_child is None:
        parent.right = left_child
        return value
    elif right_child is not None and left_child is None:
        parent.right = right_child
        return value
    elif right_child is None and left_child is None:
        parent.right = None
        return value
    else:
        remove_if_two_child(tree_cell)
        return value


def remove(tree: TreeMap, key: int) -> V:
    root = tree.root
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")

    def remove_recursion(tree_cell: TreeNode, parent):
        left_child = tree_cell.left
        right_child = tree_cell.right

        # Check if key is similar with key_cell.key
        if key == tree_cell.key:
            if parent is None:
                return remove_root(tree)
            if tree_cell == parent.left:
                return remove_parent_left(tree_cell, parent)
            else:
                return remove_parent_right(tree_cell, parent)

        # Check at which of the children we enter
        if key < tree_cell.key and left_child is not None:
            return remove_recursion(left_child, tree_cell)
        elif key > tree_cell.key and right_child is not None:
            return remove_recursion(right_child, tree_cell)

    tree.size -= 1
    return remove_recursion(root, None)


def get_tree_node(tree: TreeMap, key: int) -> TreeNode:
    root = tree.root

    def recursion(tree_cell: TreeNode) -> TreeNode:
        if key == tree_cell.key:
            return tree_cell

        if key < tree_cell.key and tree_cell.left is not None:
            return recursion(tree_cell.left)
        elif key > tree_cell.key and tree_cell.right is not None:
            return recursion(tree_cell.right)

    return recursion(root)


def get_value(tree: TreeMap, key: int) -> V:
    root = tree.root
    if not has_key(tree, key):
        raise ValueError("Tree doesn't have this key")
    return get_tree_node(tree, key).value


def has_key(tree: TreeMap, key: int) -> bool:
    root = tree.root
    return get_tree_node(tree, key) is not None


def inorder_traverse(tree: TreeMap):
    root = tree.root
    output = []

    def inorder_recursion(tree_cell: TreeNode):
        if tree_cell.left is not None and tree_cell.right is not None:
            inorder_recursion(tree_cell.left)
            output.append(tree_cell.value)
            inorder_recursion(tree_cell.right)
        elif tree_cell.left is None and tree_cell.right is not None:
            output.append(tree_cell.value)
            inorder_recursion(tree_cell.right)
        elif tree_cell.left is not None and tree_cell.right is None:
            inorder_recursion(tree_cell.left)
            output.append(tree_cell.value)
        else:
            output.append(tree_cell.value)

    inorder_recursion(root)
    return output


def preorder_traverse(tree: TreeMap):
    root = tree.root
    output = []

    def preorder_recursion(tree_cell: TreeNode):
        if tree_cell.left is not None and tree_cell.right is not None:
            output.append(tree_cell.value)
            preorder_recursion(tree_cell.left)
            preorder_recursion(tree_cell.right)
        elif tree_cell.left is None and tree_cell.right is not None:
            output.append(tree_cell.value)
            preorder_recursion(tree_cell.right)
        elif tree_cell.left is not None and tree_cell.right is None:
            output.append(tree_cell.value)
            preorder_recursion(tree_cell.left)
        else:
            output.append(tree_cell.value)

    preorder_recursion(root)
    return output


def postorder_traverse(tree: TreeMap):
    root = tree.root
    output = []

    def postorder_recursion(tree_cell: TreeNode):
        if tree_cell.left is not None and tree_cell.right is not None:
            postorder_recursion(tree_cell.left)
            postorder_recursion(tree_cell.right)
            output.append(tree_cell.value)
        elif tree_cell.left is None and tree_cell.right is not None:
            postorder_recursion(tree_cell.right)
            output.append(tree_cell.value)
        elif tree_cell.left is not None and tree_cell.right is None:
            postorder_recursion(tree_cell.left)
            output.append(tree_cell.value)
        else:
            output.append(tree_cell.value)

    postorder_recursion(root)
    return output


def traverse(tree: TreeMap, order: str) -> list[V]:
    if tree.size == 0:
        return []
    if order == "inorder":
        return inorder_traverse(tree)
    elif order == "preorder":
        return preorder_traverse(tree)
    elif order == "postorder":
        return postorder_traverse(tree)
    raise SyntaxError("Order must be one of follow: 'inorder', 'preorder', 'postorder'")
