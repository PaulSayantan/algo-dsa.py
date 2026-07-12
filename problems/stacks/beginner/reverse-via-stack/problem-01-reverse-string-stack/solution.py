"""Reverse a string using an explicit stack."""


class Solution:
    def reverse(self, s: str) -> str:
        # TODO: push chars onto a stack, then pop them off
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse("hello"))  # expected: 'olleh'
    print(sol.reverse("a"))  # expected: 'a'
    print(sol.reverse(""))  # expected: ''
