# Solution — Find Beautiful Indices in the Given Array I

## Brute Force

Scan every start position for `a` and every start position for `b` with naive
substring comparisons, then for each `a`-index test every `b`-index.

```python
def beautifulIndices(s, a, b, k):
    n = len(s)
    A = [i for i in range(n - len(a) + 1) if s[i:i + len(a)] == a]
    B = [j for j in range(n - len(b) + 1) if s[j:j + len(b)] == b]
    res = []
    for i in A:
        if any(abs(i - j) <= k for j in B):
            res.append(i)
    return res
```

- **Time:** finding occurrences naively is `O(n · |a|)` and `O(n · |b|)`; pairing
  is `O(|A| · |B|)` which is `O(n^2)` in the worst case.
- **Space:** `O(|A| + |B|)`.

## Optimal Approach — Boyer–Moore (string search) + binary search

Two independent single-pattern searches produce the occurrence lists, and the
distance check becomes a binary search because the lists are naturally sorted.

### Step 1 — find all occurrences with Boyer–Moore

Run the all-matches Boyer–Moore matcher (Problem 4) twice:

```python
A = boyer_moore_all(s, a)   # sorted start indices of a
B = boyer_moore_all(s, b)   # sorted start indices of b
```

`boyer_moore_all` compares right-to-left, shifting by
`max(good-suffix, bad-character, 1)` on a mismatch and by `gs[0]` after a full
match so overlapping occurrences are all captured. Both `A` and `B` come out in
increasing order because the scan moves left to right.

### Step 2 — pair up under the distance constraint

For each `i` in `A`, we need *some* `j` in `B` with `i - k <= j <= i + k`. Since
`B` is sorted, binary-search the first `j >= i - k` and check whether it is
`<= i + k`:

```python
import bisect

def beautifulIndices(s, a, b, k):
    A = boyer_moore_all(s, a)
    B = boyer_moore_all(s, b)
    res = []
    for i in A:
        lo = bisect.bisect_left(B, i - k)
        if lo < len(B) and B[lo] <= i + k:
            res.append(i)
    return res
```

Because we iterate `A` in increasing order, `res` is already sorted.

### Why it is correct

- Boyer–Moore's all-occurrences variant returns **exactly** the set of start
  indices where each pattern matches (shift rules never skip a valid alignment;
  `gs[0]` preserves overlaps) — see Problems 1 and 4.
- For a fixed `i`, the closest `b`-occurrence that is `>= i - k` is `B[lo]` by
  definition of `bisect_left`. If even that one exceeds `i + k`, then no `j` lies
  in `[i - k, i + k]`; otherwise `B[lo]` witnesses beauty. This correctly decides
  the existence of a nearby `b` for every candidate `i`.

### Step-by-step on Example 1

`s = "isawsquirrelnearmysquirrelhouseohmy"`, `a = "my"`, `b = "squirrel"`,
`k = 15`.

- Boyer–Moore for `"my"` → `A = [16, 33]`.
- Boyer–Moore for `"squirrel"` → `B = [4, 18]`.
- `i = 16`: `bisect_left(B, 16 - 15 = 1) = 0`, `B[0] = 4 <= 16 + 15 = 31` ✓ →
  keep 16.
- `i = 33`: `bisect_left(B, 33 - 15 = 18) = 1`, `B[1] = 18 <= 33 + 15 = 48` ✓ →
  keep 33.
- Result `[16, 33]`.

### Complexity

- **Two Boyer–Moore scans:** `O(n · |a|)` and `O(n · |b|)` worst case, sublinear
  on average; preprocessing each pattern is `O(|a| + |Σ|)` / `O(|b| + |Σ|)`.
- **Pairing:** `O(|A| · log |B|)` with binary search.
- **Overall:** dominated by the scans, effectively `O(n)` for these tiny
  patterns (`|a|, |b| <= 10`). **Space:** `O(|A| + |B|)`.

## Key Insights & Edge Cases

- **Sorted occurrence lists + binary search** turn an `O(|A|·|B|)` pairing into
  `O(|A| log |B|)`; a two-pointer merge also works in `O(|A| + |B|)` since both
  lists are sorted.
- **`a == b`** is allowed (Example 2). Each index of `a` can pair with itself
  (`j = i`, distance 0), so every occurrence is beautiful when patterns coincide.
- **Empty `B`** (pattern `b` never occurs) → no index can be beautiful → return
  `[]`. The `lo < len(B)` guard handles this.
- **`abs(i - j) <= k`** is symmetric, so a single window `[i - k, i + k]` on the
  sorted `B` captures both `j < i` and `j > i` cases.
- The two searches are independent, so this cleanly reuses the all-occurrences
  Boyer–Moore routine from Problem 4 as a black box.
