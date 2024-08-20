from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    value: Any
    previous: Optional["Node"] = None
    next: Optional["Node"] = None


@dataclass
class Deque:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    size: int = 0


def create_deque():
    return Deque(head=None, tail=None)


def get_size(deque: Deque) -> int:
    return deque.size


def is_empty(deque: Deque) -> bool:
    return deque.size == 0


def put_if_empty(deque: Deque, value: Any):
    new_node = Node(previous=None, next=None, value=value)
    deque.head = new_node
    deque.tail = new_node


def put_front(deque: Deque, value: Any):
    if is_empty(deque):
        put_if_empty(deque, value)
    else:
        old_head = deque.head
        new_head = Node(previous=None, next=old_head, value=value)
        deque.head = new_head
        old_head.previous = new_head
    deque.size += 1


def put_back(deque: Deque, value: Any):
    if is_empty(deque):
        put_if_empty(deque, value)
    else:
        old_tail = deque.tail
        new_tail = Node(previous=old_tail, next=None, value=value)
        deque.tail = new_tail
        old_tail.next = new_tail
    deque.size += 1


def pop_front(deque: Deque) -> Any:
    if is_empty(deque):
        raise ValueError("Deque is empty")

    value = deque.head.value
    new_head = deque.head.next
    deque.head = new_head
    if deque.head is not None:
        deque.head.previous = None
    deque.size -= 1
    return value


def pop_back(deque: Deque) -> Any:
    if is_empty(deque):
        raise ValueError("Deque is empty")

    value = deque.tail.value
    new_tail = deque.tail.previous
    deque.tail = new_tail
    if deque.tail is not None:
        deque.tail.next = None
    deque.size -= 1
    return value
