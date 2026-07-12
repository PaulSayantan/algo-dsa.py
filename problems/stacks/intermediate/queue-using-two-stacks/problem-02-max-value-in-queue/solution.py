"""Max Value in a Queue — max-queue via two stacks (design)."""


class MaxQueue:
    def __init__(self) -> None:
        # TODO: two stacks; each frame carries (value, running_max)
        pass

    def push_back(self, x: int) -> None:
        # TODO: push to the 'in' stack, folding the running max
        pass

    def pop_front(self) -> int:
        # TODO: pour 'in' into 'out' when empty, then pop; -1 if empty
        pass

    def max_value(self) -> int:
        # TODO: larger of the two stack-top running maxes; -1 if empty
        pass


if __name__ == "__main__":
    q = MaxQueue()
    q.push_back(1)
    q.push_back(3)
    print(q.max_value())  # expected: 3
    print(q.pop_front())  # expected: 1
    print(q.max_value())  # expected: 3
    q.push_back(2)
    print(q.max_value())  # expected: 3
    print(q.pop_front())  # expected: 3
    print(q.max_value())  # expected: 2
    print(q.pop_front())  # expected: 2
    print(q.pop_front())  # expected: -1
    print(q.max_value())  # expected: -1
