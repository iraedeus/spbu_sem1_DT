from Queue import *

if __name__ == "__main__":
    queue = new_queue()

    for i in range(10):
        push(queue, i)
        print(f"Head in queue now: {top(queue)}")

    print(" ")

    for i in range(3):
        pop(queue)
        print(f"Tail in queue now: {tail(queue)}")