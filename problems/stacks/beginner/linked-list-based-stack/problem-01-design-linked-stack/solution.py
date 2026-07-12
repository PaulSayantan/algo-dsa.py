"""Design a stack backed by a singly linked list (push/pop/top at the head)."""


class LinkedStack:
    def __init__(self) -> None:
        # TODO: keep a head pointer and a size counter
        pass

    def push(self, x: int) -> None:
        # TODO: insert a new node at the head
        pass

    def pop(self) -> int:
        # TODO: unlink and return the head value
        pass

    def top(self) -> int:
        # TODO
        pass

    def size(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    st = LinkedStack()
    st.push(10)
    st.push(20)
    st.push(30)
    print(st.size())  # expected: 3
    print(st.pop())  # expected: 30
    print(st.top())  # expected: 20
    print(st.size())  # expected: 2
