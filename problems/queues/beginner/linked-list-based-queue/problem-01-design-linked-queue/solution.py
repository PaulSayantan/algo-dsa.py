"""Design a FIFO queue backed by a singly linked list with head + tail pointers."""


class _Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class LinkedQueue:
    def __init__(self) -> None:
        # TODO: head pointer, tail pointer, and a size counter
        pass

    def enqueue(self, x: int) -> None:
        # TODO: link a new node after the tail (O(1))
        pass

    def dequeue(self) -> int:
        # TODO: unlink and return the head value; reset tail if it becomes empty
        pass

    def front(self) -> int:
        # TODO
        pass

    def size(self) -> int:
        # TODO
        pass

    def empty(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    q = LinkedQueue()
    print(q.empty())  # expected: True
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.size())  # expected: 3
    print(q.front())  # expected: 10
    print(q.dequeue())  # expected: 10
    print(q.front())  # expected: 20
    print(q.size())  # expected: 2
    print(q.dequeue())  # expected: 20
    print(q.dequeue())  # expected: 30
    print(q.empty())  # expected: True
