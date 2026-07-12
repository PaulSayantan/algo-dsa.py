"""First non-repeating character in a stream — return the per-step answers."""
from collections import deque  # noqa: F401


class Solution:
    def firstUniqStream(self, stream: str) -> str:
        # TODO: maintain counts + a deque of candidates; front is the first unique
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqStream("aabc"))  # expected: 'a#bb'
    print(sol.firstUniqStream("abcabc"))  # expected: 'aaabc#'
    print(sol.firstUniqStream("abadc"))  # expected: 'aabbb'
    print(sol.firstUniqStream("z"))  # expected: 'z'
