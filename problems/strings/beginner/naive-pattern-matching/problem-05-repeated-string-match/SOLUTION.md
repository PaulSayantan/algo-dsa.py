# Solution — Repeated String Match

## Brute Force

Keep appending copies of `a` and, after each append, test whether `b` is now a
substring. Stop once the repeated string is comfortably longer than `b`.

```python
def repeatedStringMatch(a, b):
    repeated = a
    count = 1
    # keep going until repeated is at least len(b) + len(a) long
    while len(repeated) < len(b) + len(a):
        if b in repeated:          # substring test
            return count
        repeated += a
        count += 1
    return count if b in repeated else -1
```

This works but is easy to get subtly wrong on the stopping condition, and it relies on
the built-in `in`. The insight below pins down *exactly* how many copies to try.

- **Time:** `O((n + m) · m)` where `n = len(a)`, `m = len(b)`.
- **Space:** `O(n + m)` for the repeated string.

## Optimal Approach (Naive Pattern Matching)

**How many copies could ever be needed?** To contain `b` at all, the repeated string
must be at least as long as `b`, so we need at least `k = ceil(len(b) / len(a))` copies.
Those `k` copies might not line up with where `b` starts inside the periodic string — a
match may begin partway through the first copy — so we may need **one extra** copy to
cover the tail. Crucially, `k + 1` copies are always sufficient if a solution exists:
any occurrence of `b` in the infinite repetition of `a` spans at most `k + 1` blocks.
Therefore the answer is `k` if `b` fits in `k` copies, else `k + 1` if it fits there,
else `-1`.

```python
import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        k = math.ceil(len(b) / len(a))          # minimum copies by length
        for copies in (k, k + 1):               # only these can be minimal
            text = a * copies
            if self._contains(text, b):
                return copies
        return -1

    @staticmethod
    def _contains(text: str, pattern: str) -> bool:
        """Naive substring search: True iff pattern occurs in text."""
        n, m = len(text), len(pattern)
        for start in range(n - m + 1):
            j = 0
            while j < m and text[start + j] == pattern[j]:
                j += 1
            if j == m:
                return True
        return False
```

**Why it is correct.**
- Fewer than `k` copies are shorter than `b`, so `b` cannot fit — no need to test them.
- If `b` occurs in the infinite string `aaaa...`, its occurrence starts at some offset
  `0 <= off < len(a)` (any larger offset is equivalent modulo one block). From that
  offset, `b` spans `off + len(b)` characters, and
  `off + len(b) <= len(a) + len(b) <= (k + 1) · len(a)`, so `k + 1` copies always
  contain it. Hence if neither `k` nor `k + 1` copies contain `b`, no amount ever will.
- We test `k` first and return immediately, guaranteeing the **minimum**.

**Step-by-step** on `a = "abcd"`, `b = "cdabcdab"` (`len(a) = 4`, `len(b) = 8`):
`k = ceil(8 / 4) = 2`. Test `copies = 2`: `text = "abcdabcd"` (length 8); naive search
finds no `"cdabcdab"` -> fail. Test `copies = 3`: `text = "abcdabcdabcd"`; naive search
matches at index 2 -> return `3`.

- **Time:** `O((n + m) · m)` worst case — the repeated string has length
  `O(n + m)` and the naive search is `O(length · m)`. `O(n + m)` on typical inputs.
- **Space:** `O(n + m)` to build the repeated string.

## Key Insights & Edge Cases

- **Only two candidate counts.** `k` and `k + 1`. Testing more is wasted work; testing
  fewer misses the length requirement. This bound is the crux of the problem.
- **The "+1" is for alignment**, not length: even when `k` copies are long enough, `b`
  might straddle a copy boundary such that it needs part of one more copy.
- **Impossible characters.** If `b` contains a character absent from `a` (Example 3),
  neither search matches and we return `-1` — the naive scan handles this without a
  separate character-set check.
- **`b` shorter than `a`.** Then `k = 1`; we test 1 copy, then 2, covering cases like
  `a = "abcd"`, `b = "cda"` where the match wraps the boundary.
- Swapping `_contains` for KMP or Rabin-Karp yields `O(n + m)` overall while keeping the
  exact same `k` / `k + 1` reasoning.
