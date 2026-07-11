# Solution — Longest Palindromic Substring

## Brute Force

Enumerate every substring `s[i:j+1]`, check whether it is a palindrome, and keep
the longest one seen.

```python
def longestPalindrome(s):
    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
    return best
```

- There are `O(n²)` substrings, and verifying each palindrome costs `O(n)`.
- **Time:** `O(n³)`  **Space:** `O(n)` for the substring copy (or `O(1)` with an
  index-based palindrome check).

This is too slow once `n` grows toward 1000.

## Optimal Approach — Expand Around Center

**Key idea.** A palindrome is symmetric around its center. Rather than checking
substrings independently, fix a center and grow outward while the mirrored
characters match. A length-`n` string has `2n - 1` centers:

- `n` **odd** centers, one on each index `i` (palindromes like `aba`).
- `n - 1` **even** centers, one between indices `i` and `i + 1` (palindromes
  like `abba`).

For each center, expand two pointers and record the widest palindrome found.

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # s[left+1 : right] is the palindrome; return inclusive bounds
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)      # odd-length center
            if r1 - l1 > end - start:
                start, end = l1, r1
            l2, r2 = expand(i, i + 1)  # even-length center
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
```

**Why it is correct.** Every palindromic substring has a unique center (a single
character for odd lengths, the gap between two characters for even lengths). By
trying all `2n - 1` centers and expanding maximally from each, we consider the
*longest* palindrome anchored at every possible center — so the global maximum is
guaranteed to be among the candidates we examine.

**Step by step on `s = "cbbd"`:**

| Center | Type | Expansion | Palindrome |
|--------|------|-----------|------------|
| i=0 (`c`) | odd | `c` only | `"c"` |
| between 0,1 | even | `c != b` | `""` |
| i=1 (`b`) | odd | `b` only | `"b"` |
| between 1,2 | even | `b == b`, then `c != d` | `"bb"` ✅ |
| i=2 (`b`) | odd | `b` only | `"b"` |
| between 2,3 | even | `b != d` | `""` |
| i=3 (`d`) | odd | `d` only | `"d"` |

The widest is `"bb"`.

- **Time:** `O(n²)` — `2n - 1` centers, each expansion is `O(n)` in the worst
  case (e.g. `"aaaa..."`).
- **Space:** `O(1)` extra (we track only index bounds; the returned slice is the
  required output).

## Key Insights & Edge Cases

- **Two center types are essential.** Forgetting the even center (`expand(i, i+1)`)
  is the classic bug — you would miss `"bb"`, `"abba"`, etc.
- **Track indices, not string copies.** Storing `(start, end)` avoids repeated
  slicing and keeps extra space at `O(1)`.
- **Comparison `r - l > end - start`** compares lengths using index spans; the
  actual length is `r - l + 1`, but the `+1` cancels on both sides.
- **Single character / empty input.** A one-character string returns itself; an
  empty string (outside the stated constraints) should return `""`.
- **All identical characters** (`"aaaa"`) is the worst case where every expansion
  runs to the ends — still `O(n²)` overall.
- **Need linear time?** Manacher's algorithm solves this in `O(n)`, but
  expand-around-center is preferred in interviews for its simplicity.
