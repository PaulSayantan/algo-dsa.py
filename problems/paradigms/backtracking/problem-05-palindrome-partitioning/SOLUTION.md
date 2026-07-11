# Palindrome Partitioning — Solution

## Brute Force

A string of length `n` has `n - 1` possible cut positions between adjacent
characters, and each can independently be "cut" or "not cut", giving `2^(n-1)`
candidate partitions. The brute-force approach enumerates all `2^(n-1)` subsets
of cut positions, splits the string accordingly, and keeps a partition only if
**every** resulting piece is a palindrome.

```python
def partition(s):
    n = len(s)
    result = []
    for mask in range(1 << (n - 1)):          # each bit = cut after position i
        pieces, prev = [], 0
        for i in range(n - 1):
            if mask & (1 << i):
                pieces.append(s[prev:i + 1]); prev = i + 1
        pieces.append(s[prev:])
        if all(p == p[::-1] for p in pieces):
            result.append(pieces)
    return result
```

- **Time:** `O(2^(n-1) · n^2)` — `2^(n-1)` partitions, each split and palindrome-
  checked in `O(n^2)` total.
- **Space:** `O(n)` per candidate partition.

It is correct but validates each partition only *after* fully building it, so it
wastes effort on partitions doomed by an early non-palindromic piece.

## Optimal Approach (Backtracking)

Instead of choosing all cuts up front, grow the partition left to right. From
position `start`, try every prefix `s[start:end]`; **only recurse when that
prefix is already a palindrome**. This prunes entire subtrees the moment a piece
is invalid.

```python
def partition(s):
    n = len(s)
    result = []
    path = []

    def is_pal(lo, hi):                      # s[lo:hi+1] palindrome?
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1; hi -= 1
        return True

    def backtrack(start):
        if start == n:                       # consumed the whole string
            result.append(path[:])
            return
        for end in range(start, n):          # prefix s[start:end+1]
            if is_pal(start, end):           # prune: skip non-palindromic prefix
                path.append(s[start:end + 1])   # choose
                backtrack(end + 1)              # recurse on the suffix
                path.pop()                      # undo
    backtrack(0)
    return result
```

**Why it is correct.**

- The base case `start == n` records a partition only after the string is fully
  consumed by contiguous pieces, so the pieces always concatenate back to `s`.
- Every piece appended passes `is_pal`, so recorded partitions are all-palindrome.
- Trying every `end >= start` covers every possible first-cut length, and
  recursion handles the rest, so no valid partition is missed and — because cuts
  advance strictly (`end + 1`) — none is produced twice.

**Step by step for `s = "aab"`:**

- `start=0`: prefix `"a"` (pal) → `start=1`: prefix `"a"` (pal) → `start=2`:
  prefix `"b"` (pal) → `start=3` == n → record `["a","a","b"]`. Undo.
  Back at `start=1`, prefix `"ab"` not a palindrome → prune. Undo.
- Back at `start=0`, prefix `"aa"` (pal) → `start=2`: `"b"` (pal) → record
  `["aa","b"]`. Undo. Prefix `"aab"` not a palindrome → prune.

Result: `[["a","a","b"], ["aa","b"]]`.

- **Time:** `O(n · 2^n)` in the worst case (e.g., `s = "aaaa..."` where every cut
  is legal): up to `2^(n-1)` partitions, each costing `O(n)` to copy, plus the
  `O(n)` palindrome checks along each path.
- **Space:** `O(n)` recursion depth + current path.

## Key Insights & Edge Cases

- **Prune before recursing.** Checking `is_pal` *before* the recursive call is
  what makes this beat brute force in practice — a bad prefix kills its subtree
  immediately instead of after the full partition is assembled.
- **Precompute palindromes (DP).** For repeated queries you can precompute a
  boolean table `pal[i][j]` in `O(n^2)` so each `is_pal` check is `O(1)`; this
  lowers per-node cost but not the exponential number of partitions.
- **Copy on record** (`path[:]`) — same aliasing trap as the other problems.
- **Every single character is a palindrome**, so a fully-split partition always
  exists; the result is therefore never empty (for `n >= 1`).
- **Whole-string palindromes** (like `"aba"`) yield the uncut string as one valid
  partition, produced by the final `end = n - 1` branch.
