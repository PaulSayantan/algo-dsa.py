"""Double-ended priority queue (two heaps + lazy deletion) (design)."""
import heapq  # noqa: F401


class DEPQ:
    def __init__(self) -> None:
        # TODO: min-heap, max-heap, and an alive map keyed by id
        pass

    def push(self, x: int) -> None:
        # TODO
        pass

    def popMin(self) -> int:
        # TODO
        pass

    def popMax(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    dq = DEPQ()
    dq.push(5)
    dq.push(1)
    dq.push(8)
    dq.push(3)
    print(dq.popMin())  # expected: 1
    print(dq.popMax())  # expected: 8
    print(dq.popMin())  # expected: 3
    print(dq.popMax())  # expected: 5
    dq.push(10)
    dq.push(-2)
    print(dq.popMax())  # expected: 10
    print(dq.popMin())  # expected: -2
