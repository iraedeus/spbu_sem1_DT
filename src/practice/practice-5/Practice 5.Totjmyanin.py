import collections
from dataclasses import dataclass

StackElement = collections.namedtuple("StackElement", ["value", "next"])


@dataclass
class Stack:
    size: int = 0
    head: StackElement = None


def new_stack():
    return Stack()


def size(stack):
    return stack.size


def empty(stack):
    if stack.size == 0:
        return True
    else:
        return False


def top(stack):
    return stack.head.value


def push(stack, element_value):
    stack.head = StackElement(element_value, stack.head)
    stack.size += 1


def pop(stack):
    stack.head = stack.head.next
    stack.size -= 1


def main():
    stack = new_stack()
    for i in range(10):
        push(stack, i)
        print(f"Current value in head: {top(stack)}")

    print("Pushing in stack finished")

    for i in range(8):
        print(f"Current value in head: {top(stack)}")
        pop(stack)

    print("Popping from stack finished")

    print(f"Is stack empty: {empty(stack)}")


if __name__ == "__main__":
    main()
