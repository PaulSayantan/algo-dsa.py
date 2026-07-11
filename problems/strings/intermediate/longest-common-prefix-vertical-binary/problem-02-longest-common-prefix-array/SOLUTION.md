# Solution — Longest Common Prefix (LeetCode 14)

Let `n = len(strs)` and `m = ` length of the *shortest* string. The answer can never be
longer than `m`.

## Brute Force

**Horizontal scan.** Start with `prefix = strs[0]`. For each subsequent string, chop
characters off the end of `prefix` until it becomes a prefix of that string:

```python
prefix = strs[0]
for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            return ""
return prefix
```

In the worst case (all strings equal) every `startswith` compares up to `m` characters
for all `n` strings.

**Time:** `O(n * m)` on average but `O(S)` where `S` is the total number of characters
scanned; each `prefix[:-1]` also rebuilds a string. **Space:** `O(m)` for the mutable
prefix.

## Optimal Approach — Vertical Scan

Read the strings **column by column**. Take `strs[0]` as the reference; at column `j`,
compare `strs[0][j]` against `strs[i][j]` for every other `i`. Stop as soon as some
string is too short (`j` past its end) or some character differs.

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        for j, ch in enumerate(first):          # column index j
            for s in strs[1:]:
                if j >= len(s) or s[j] != ch:    # short string or mismatch
                    return first[:j]
        return first                              # first string is the prefix
```

**Why it is correct.** After finishing column `j`, we have proven every string agrees on
`first[:j+1]`. We only return when a column fails, and at that point no string can share
a `(j+1)`-length prefix, so `first[:j]` is maximal. If we exhaust `first`, then `first`
itself is a prefix of every string and is the longest possible (nothing can exceed the
reference length once the reference is itself a common prefix).

**Step by step for `["flower", "flow", "flight"]`:**

| column j | chars down the column | verdict |
|----------|-----------------------|---------|
| 0        | f, f, f               | match   |
| 1        | l, l, l               | match   |
| 2        | o, o, i               | mismatch -> return `"fl"` |

**Time:** `O(S)` = `O(n * m)` worst case, but early termination makes it `O(n * L)` where
`L` is the answer length — often far less. **Space:** `O(1)` extra.

## Binary Search on Prefix Length

`isCommonPrefix(L) = all(s[:L] == strs[0][:L] for s in strs)` is **monotonic** in `L`, so
binary search the largest feasible `L` in `[0, m]`:

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(len(s) for s in strs)
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi + 1) // 2
            cand = strs[0][:mid]
            if all(s.startswith(cand) for s in strs):
                lo = mid
            else:
                hi = mid - 1
        return strs[0][:lo]
```

**Time:** `O(n * m * log m)` — `log m` length guesses, each an `O(n * m)` verification.
**Space:** `O(1)` extra. This is asymptotically heavier than the vertical scan, but it is
the right tool when prefix-equality can be answered in `O(1)` (precomputed hashes) or when
only the *length* is needed.

## Key Insights & Edge Cases

- **Single string:** return it unchanged (the outer loop finishes without a mismatch).
- **Any empty string present:** the answer is immediately `""`, because column 0 is past
  the end of the empty string.
- **No shared first character:** returns `""` at column 0.
- **All strings identical:** the vertical scan exhausts the reference and returns it.
- Pick the reference for the vertical scan as any string (commonly `strs[0]`); choosing
  the shortest string is a micro-optimization but not required for correctness.
- The vertical approach naturally stops at the first mismatch, giving best-case behavior
  when strings diverge early — a common real-world case.
