# H-Index — Solution

## Brute Force

Sort the citations in descending order. Then scan: the largest `h` such that the
`h`-th paper (1-indexed) has at least `h` citations is the answer.

```python
def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h
```

- **Time:** `O(n log n)` dominated by the sort.
- **Space:** `O(1)` extra (or `O(n)` if the sort is not in place).

This is clean, but the sort is unnecessary: citation counts above `n` are
indistinguishable for h-index purposes, so we can bucket instead.

## Optimal Approach (Bucket Sort)

**Key observation:** the h-index is at most `n` (you cannot have more than `n`
papers each cited `n` times when you only have `n` papers). Therefore any
citation count larger than `n` is "capped" at `n` — it contributes no more than
a paper with exactly `n` citations. That makes the count space a bounded integer
range `[0, n]`, perfect for bucketing.

### Steps

1. Create `n + 1` buckets. `buckets[i]` = number of papers with exactly `i`
   citations, **except** `buckets[n]` also absorbs every paper with `> n`
   citations (cap at `n`).
2. Fill the buckets in one pass: for each `c`, increment `buckets[min(c, n)]`.
3. Sweep from `i = n` down to `0`, keeping a running total of papers seen so far
   (papers with `>= i` citations). The first `i` where
   `running_total >= i` is the h-index.

```python
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations:
            buckets[min(c, n)] += 1

        total = 0  # number of papers with >= i citations
        for i in range(n, -1, -1):
            total += buckets[i]
            if total >= i:
                return i
        return 0
```

### Why It Is Correct

Sweeping from the top, `total` after processing index `i` equals the number of
papers with at least `i` citations (capping at `n` is safe because a paper with
`>= n` citations certainly has `>= i` citations for any `i <= n`). By definition
the h-index is the largest `i` for which at least `i` papers have `>= i`
citations, i.e. `total >= i`. Because we scan `i` from high to low, the first
index satisfying `total >= i` is the maximum such `i` — exactly the h-index. The
loop always terminates because at `i = 0`, `total = n >= 0`.

### Complexity

- **Time:** `O(n)`. One pass to fill buckets, one pass to sweep.
- **Space:** `O(n)` for the `n + 1` buckets.

## Key Insights & Edge Cases

- **Capping at `n`** is the crux — it bounds the key space so bucketing is legal
  and turns `O(n log n)` into `O(n)`.
- **All zeros** (`[0, 0]`): every paper lands in `buckets[0]`; the sweep reaches
  `i = 0` with `total = 2 >= 0`, returning `0`.
- **All papers highly cited** (`[100, 100, 100]` with `n = 3`): all three cap to
  `buckets[3]`; at `i = 3`, `total = 3 >= 3`, so h = 3.
- **Single paper** (`[5]`, `n = 1`): caps to `buckets[1]`; at `i = 1`,
  `total = 1 >= 1`, h = 1.
- Be sure to allocate `n + 1` buckets (indices `0..n`), and remember to add the
  current bucket to `total` *before* the comparison inside the loop.
