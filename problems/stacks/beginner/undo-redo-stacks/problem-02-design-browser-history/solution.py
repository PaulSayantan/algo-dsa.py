"""Design Browser History backed by back/forward stacks (design)."""


class BrowserHistory:
    def __init__(self, homepage: str) -> None:
        # TODO: current page + back stack + forward stack
        pass

    def visit(self, url: str) -> None:
        # TODO: push current onto back stack, move to url, clear forward stack
        pass

    def back(self, steps: int) -> str:
        # TODO: pop up to `steps` pages off the back stack onto the forward stack
        pass

    def forward(self, steps: int) -> str:
        # TODO: pop up to `steps` pages off the forward stack onto the back stack
        pass


if __name__ == "__main__":
    bh = BrowserHistory("home.com")
    bh.visit("a.com")
    bh.visit("b.com")
    print(bh.back(1))     # expected: 'a.com'
    print(bh.back(1))     # expected: 'home.com'
    print(bh.forward(1))  # expected: 'a.com'
    bh.visit("c.com")     # clears forward history
    print(bh.forward(1))  # expected: 'c.com'
    print(bh.back(2))     # expected: 'home.com'
