"""Rendezvous (Highest-Random-Weight) hashing."""


class RendezvousHash:
    def __init__(self) -> None:
        # TODO: store the node list
        pass

    def add_node(self, name: str) -> None:
        # TODO
        pass

    def get_node(self, key: str):
        # TODO: return the node maximizing a FIXED hash(node, key) score
        # (break ties deterministically, e.g. by iterating nodes in sorted order)
        pass


if __name__ == "__main__":
    hrw = RendezvousHash()
    hrw.add_node("cacheA")
    hrw.add_node("cacheB")
    hrw.add_node("cacheC")
    print(hrw.get_node("obj-1"))  # expected: 'cacheB'
    print(hrw.get_node("obj-2"))  # expected: 'cacheA'
    print(hrw.get_node("obj-3"))  # expected: 'cacheC'
    print(hrw.get_node("obj-4"))  # expected: 'cacheA'
