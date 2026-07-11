# Solution — Palindromic Substrings

## Brute Force

Enumerate all `O(n²)` substrings and test each for the palindrome property.

```python
def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                count += 1
    return count
```

- **Time:** `O(n³)` (each of `O(n²)` substrings verified in `O(n)`).
- **Space:** `O(n)` for the substring copy (or `O(1)` with index-based checks).

## Optimal Approach — Expand Around Center

**Key idea.** Every palindromic substring is symmetric about a center. There are
`2n - 1` centers (`n` odd + `n - 1` even). When we expand from a center, **each
successful step of the expansion uncovers exactly one new palindrome**: the
first match is the smallest palindrome around that center, the next match extends
it by one character on each side, and so on. So we simply count expansions.

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def count_from(left: int, right: int) -> int:
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1        # s[left..right] is a palindrome
                left -= 1
                right += 1
            return cnt

        total = 0
        for i in range(n):
            total += count_from(i, i)      # odd-length centers
            total += count_from(i, i + 1)  # even-length centers
        return total
```

**Why it is correct.** Each palindromic substring has a unique center. Expanding
maximally from every center visits each palindrome exactly once (once when the
window first reaches that width), so summing the expansion counts across all
centers counts every palindromic substring exactly once — no double counting.

**Step by step on `s = "aaa"`:**

| Center | Type | Matches while expanding | Palindromes found |
|--------|------|--------------------------|-------------------|
| i=0 | odd | `a` | 1 → `"a"` |
| 0,1 | even | `a==a` | 1 → `"aa"` |
| i=1 | odd | `a`, then `a==a` | 2 → `"a"`, `"aaa"` |
| 1,2 | even | `a==a` | 1 → `"aa"` |
| i=2 | odd | `a` | 1 → `"a"` |

Total = `1 + 1 + 2 + 1 + 1 = 6`. ✅

- **Time:** `O(n²)`  — `2n - 1` centers, each expansion `O(n)`.
- **Space:** `O(1)` extra.

## Key Insights & Edge Cases

- **Count by position, not by content.** `"aaa"` yields 6, not 3 — repeated
  identical palindromes at different positions each count. (Distinct-content
  counting is a different, harder problem; see Problem 3.)
- **The "one palindrome per expansion step" invariant** is what turns the
  longest-palindrome expansion into a counting routine. It works because widening
  a palindrome by one on each side yields a *new, longer* palindrome centered at
  the same point.
- **Even centers matter.** Dropping `count_from(i, i + 1)` would miss every
  even-length palindrome (`"aa"`, `"abba"`, ...).
- **All-identical worst case** (`"aaaa..."`) gives the maximum count
  `n(n+1)/2` and the `O(n²)` worst-case runtime.
- **Dynamic-programming alternative:** an `O(n²)` time / `O(n²)` space table also
  works, but expand-around-center matches the time bound with only `O(1)` space.
