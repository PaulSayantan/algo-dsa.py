# Solution — Palindrome Partitioning IV

## Brute Force

Try every pair of cut points `(i, j)` and check whether each of the three pieces
is a palindrome by reversing it.

```python
def checkPartitioning(s):
    n = len(s)
    def is_pal(a, b):          # inclusive [a, b]
        sub = s[a:b + 1]
        return sub == sub[::-1]
    for i in range(1, n - 1):
        for j in range(i, n - 1):
            if is_pal(0, i - 1) and is_pal(i, j) and is_pal(j + 1, n - 1):
                return True
    return False
```

- There are `O(n²)` cut-point pairs, each palindrome check costs `O(n)`.
- **Time:** `O(n³)`  **Space:** `O(n)` for the reversed slices.

With `n` up to 2000, `O(n³)` (8 billion operations) is too slow.

## Optimal Approach — Expand-Around-Center Palindrome Table + Two Cuts

**Key idea.** The bottleneck is repeatedly re-checking whether a substring is a
palindrome. Precompute a boolean table `pal[i][j]` = "is `s[i..j]` a palindrome"
once, then each of the `O(n²)` cut-pair tests becomes `O(1)`.

We fill that table with expand-around-center: from each of the `2n - 1` centers,
every successful expansion marks one window `pal[left][right] = True`.

```python
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table by expanding around every center.
        def mark(left: int, right: int) -> None:
            while left >= 0 and right < n and s[left] == s[right]:
                pal[left][right] = True
                left -= 1
                right += 1

        for c in range(n):
            mark(c, c)      # odd-length centers
            mark(c, c + 1)  # even-length centers

        # Try every pair of cut points: [0..i-1] [i..j] [j+1..n-1]
        for i in range(1, n - 1):
            if not pal[0][i - 1]:
                continue
            for j in range(i, n - 1):
                if pal[i][j] and pal[j + 1][n - 1]:
                    return True
        return False
```

**Why it is correct.** Expand-around-center marks `pal[i][j]` for *exactly* the
palindromic windows (each palindrome is reached once from its unique center), so
the table is complete and accurate. The double loop then enumerates every legal
way to place two cuts (guaranteeing three non-empty pieces via the index ranges
`1 <= i` and `j < n - 1`), and returns `True` as soon as all three pieces are
flagged palindromes. If no pair works, no valid partition exists.

**Step by step on `s = "abcbdd"` (n = 6):**

1. Expansion marks palindromes including `pal[0][0]` (`"a"`), `pal[1][3]`
   (`"bcb"`), `pal[4][5]` (`"dd"`), plus all single characters.
2. Cut search: with `i = 1`, `pal[0][0]` is `True`. With `j = 3`, `pal[1][3]`
   (`"bcb"`) is `True` and `pal[4][5]` (`"dd"`) is `True`.
3. All three pieces are palindromes → return `True`. ✅

For `"bcbddxy"`, the last two characters `"xy"` force the third piece to end in a
non-palindromic tail no matter where the cuts go, so every pair fails → `False`.

- **Time:** `O(n²)` — building the table is `O(n²)`, and the cut search is
  `O(n²)` with `O(1)` lookups.
- **Space:** `O(n²)` for the palindrome table.

## Key Insights & Edge Cases

- **Table build is the star.** Expand-around-center produces the full `pal[i][j]`
  table in `O(n²)` with a very tight inner loop — cleaner than the DP recurrence
  `pal[i][j] = (s[i]==s[j]) and pal[i+1][j-1]`, though both are `O(n²)`.
- **Cut-point ranges enforce non-emptiness.** `i` ranges over `[1, n-2]` and `j`
  over `[i, n-2]`, so the first piece (`0..i-1`), middle (`i..j`), and last
  (`j+1..n-1`) are all guaranteed length ≥ 1.
- **Early `continue`** when the first piece isn't a palindrome prunes a whole row
  of the inner loop.
- **Minimum length.** With `n = 3`, the only candidate is `i = 1, j = 1`, i.e.
  three single characters — always three palindromes, so any 3-char string
  returns `True`.
- **Memory note.** For very large `n`, an `O(n)`-space variant is possible by
  precomputing, for each start index, the set of palindrome end indices as
  bitsets — but the `O(n²)` table is simplest and fits the constraints.
