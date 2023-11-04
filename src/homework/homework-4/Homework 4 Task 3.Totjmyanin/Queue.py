from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int = None
    previous: Optional["Node"] = None
    next: Optional["Node"] = None


@dataclass
class Queue:
    size: int = 0
    head: Optional[Node] = None
    tail: Optional[Node] = None


def new_queue():
    return Queue()


def size(queue):
    return queue.size


def empty(queue):
    return queue.size == 0


def top(queue):
    if empty(queue):
        raise ValueError("Queue is empty")
    return queue.head.value


def tail(queue):
    if empty(queue):
        raise ValueError("Queue is empty")
    return queue.tail.value


def push(queue, value):
    if empty(queue):
        head_tail = Node(value=value, previous=None, next=None)
        queue.head = head_tail
        queue.tail = head_tail
    else:
        head = queue.head

        new_head = Node(value=value, previous=None, next=head)
        head.previous = new_head

        queue.head = new_head
    queue.size += 1


def pop(queue):
    if empty(queue):
        raise ValueError("Queue is empty")
    elif queue.size == 1:
        queue.head = None
        queue.tail = None
    else:
        queue.tail = queue.tail.previous

    queue.size -= 1
