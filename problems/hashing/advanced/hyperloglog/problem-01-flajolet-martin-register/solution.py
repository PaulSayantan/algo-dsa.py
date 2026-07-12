"""Flajolet-Martin register: track the max trailing-zero run of hashed items."""


class FMSketch:
    def __init__(self, mod: int = 256) -> None:
        # TODO: remember the modulus and the running max trailing-zero count
        pass

    def add(self, x: int) -> None:
        # TODO: hash x, count trailing zeros, keep the max
        pass

    def max_trailing_zeros(self) -> int:
        # TODO: the largest trailing-zero run seen so far
        pass

    def estimate(self) -> int:
        # TODO: 2 ** max_trailing_zeros
        pass


if __name__ == "__main__":
    fm = FMSketch(256)
    fm.add(1)
    fm.add(2)
    fm.add(3)
    fm.add(7)
    print(fm.max_trailing_zeros())  # expected: 3
    print(fm.estimate())  # expected: 8
