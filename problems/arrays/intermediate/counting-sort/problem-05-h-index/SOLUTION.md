# H-Index — Solution

## Brute Force

Sort the citations (say, descending) and find the largest `h` where the `h`-th highest paper
still has at least `h` citations.

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

- **Time:** `O(n log n)` for the sort.
- **Space:** `O(1)` extra (in-place sort) or `O(n)`.

Correct, but the sort is the bottleneck, and we can avoid it because the h-index can never
exceed `n`.

## Optimal Approach (Counting Sort with capped buckets)

Key observation: **the h-index is at most `n`** (you cannot have more than `n` papers each
cited at least `h` times if `h > n`). So any paper with more than `n` citations contributes no
more toward the h-index than a paper with exactly `n` citations. That lets us collapse the
citation range into just `n + 1` buckets.

**Steps:**

1. Let `n = len(citations)`. Build `count[0..n]`. For each citation `c`, increment
   `count[min(c, n)]` — capping at `n` folds all "overflow" papers into the top bucket.
2. Walk `h` from `n` down to `0`, maintaining `total`, the number of papers with **at least**
   `h` citations. At each step add `count[h]` to `total` (since a paper counted at level `h`
   has at least `h` citations).
3. The first `h` (largest, because we scan downward) for which `total >= h` is the answer.

```python
def hIndex(citations):
    n = len(citations)
    count = [0] * (n + 1)
    for c in citations:
        count[min(c, n)] += 1

    total = 0
    for h in range(n, -1, -1):
        total += count[h]        # papers with >= h citations
        if total >= h:
            return h
    return 0
```

**Why it is correct:** Scanning from `h = n` downward, `total` accumulates exactly the number
of papers with at least `h` citations (a paper in bucket `b >= h` has been added at some level
`>= h`). The definition asks for the largest `h` with `total >= h`; because `total` only grows
as `h` decreases and we scan from the top, the first `h` satisfying `total >= h` is that
maximum. The loop always terminates — at `h = 0`, `total = n >= 0` holds.

- **Time:** `O(n)`. Counting is `O(n)`; the downward scan touches `n + 1` buckets.
- **Space:** `O(n)` for the count array.

## Key Insights & Edge Cases

- **Capping at `n`** is the crucial trick: it bounds the key range to `[0, n]` even though raw
  citation counts can be much larger (up to 1000 here, or unbounded in general), keeping the
  count array size `O(n)`.
- **Scan direction matters.** Going high-to-low lets `total` mean "papers with at least this
  many citations," so the first hit is the maximum `h`.
- **All zeros** (Example 3): every paper lands in bucket `0`; no positive `h` satisfies
  `total >= h`, and the loop returns `0`.
- **Papers with huge citation counts** are safely merged into bucket `n`; their exact value
  beyond `n` is irrelevant to the h-index.
- The loop is guaranteed to return inside the range because `h = 0` always satisfies the
  condition, but returning `0` after the loop makes the intent explicit.
