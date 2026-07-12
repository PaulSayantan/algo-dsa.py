"""Design Circular Queue — LeetCode 622. Fixed capacity k, all ops O(1)."""


class MyCircularQueue:
    def __init__(self, k: int) -> None:
        # TODO: fixed-size buffer, head index, and a count of live elements
        pass

    def enQueue(self, value: int) -> bool:
        # TODO: reject if full; else write at (head + count) % cap
        pass

    def deQueue(self) -> bool:
        # TODO: reject if empty; else advance head
        pass

    def Front(self) -> int:
        # TODO: -1 if empty
        pass

    def Rear(self) -> int:
        # TODO: -1 if empty
        pass

    def isEmpty(self) -> bool:
        # TODO
        pass

    def isFull(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    cq = MyCircularQueue(3)
    print(cq.enQueue(1))  # expected: True
    print(cq.enQueue(2))  # expected: True
    print(cq.enQueue(3))  # expected: True
    print(cq.enQueue(4))  # expected: False
    print(cq.Rear())  # expected: 3
    print(cq.isFull())  # expected: True
    print(cq.deQueue())  # expected: True
    print(cq.enQueue(4))  # expected: True
    print(cq.Front())  # expected: 2
    print(cq.Rear())  # expected: 4
