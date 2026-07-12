"""Implement a LIFO stack using a single FIFO linked-list queue."""


class _Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class MyStack:
    def __init__(self) -> None:
        # TODO: head pointer, tail pointer, and a size counter for the queue
        pass

    def push(self, x: int) -> None:
        # TODO: enqueue x at the tail, then rotate the earlier (size - 1) elements
        # from head to tail so x ends up at the head
        pass

    def pop(self) -> int:
        # TODO: dequeue and return the head value
        pass

    def top(self) -> int:
        # TODO: return the head value without removing it
        pass

    def empty(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    s = MyStack()
    print(s.empty())  # expected: True
    s.push(1)
    s.push(2)
    print(s.top())  # expected: 2
    print(s.pop())  # expected: 2
    print(s.top())  # expected: 1
    s.push(3)
    print(s.pop())  # expected: 3
    print(s.pop())  # expected: 1
    print(s.empty())  # expected: True
