from Deque import *

if __name__ == "__main__":
    deque = create_deque()
    for i in range(1, 3):
        put_front(deque, "ab" * i)

    for i in range(1, 4):
        put_back(deque, i)

    for i in range(2):
        print(pop_back(deque))
    for i in range(get_size(deque)):
        print(pop_front(deque))
    print("\n")
    print(is_empty(deque))
