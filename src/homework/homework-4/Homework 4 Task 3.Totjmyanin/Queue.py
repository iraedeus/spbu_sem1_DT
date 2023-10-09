import collections
from dataclasses import dataclass


@dataclass
class Node:
    value: int = None
    next: any = None


@dataclass
class Queue:
    size: int = 0
    head: Node = None


def new_queue():
    return Queue()


def size(queue):
    return queue.size


def empty(stack):
    return stack.size == 0


def top(queue):
    if queue.head is not None:
        return queue.head.value


def tail(queue):
    if queue.size > 1:
        current_node = queue.head
        for i in range(queue.size - 1):
            current_node = current_node.next
        return current_node.value
    else:
        return queue.head


def push(queue, value):
    if queue.head is None:
        node = Node(value, None)
        queue.head = node
    else:
        node = Node(value, queue.head)
        queue.head = node
    queue.size += 1


def pop(queue):
    if queue is not None:
        current_node = queue.head
        for i in range(queue.size - 1):
            current_node = current_node.next
        current_node.next = None
    queue.size -= 1
