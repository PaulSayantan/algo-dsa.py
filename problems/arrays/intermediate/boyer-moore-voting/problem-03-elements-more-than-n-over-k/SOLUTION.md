# Elements That Appear More Than ⌊n/k⌋ Times — Solution

## Brute Force

**Hash-map counting.** Tally all frequencies, then emit keys with count `> n // k`.

```python
from collections import Counter

def elementsMoreThanNOverK(nums, k):
    n = len(nums)
    return [v for v, c in Counter(nums).items() if c > n // k]
```

- **Time:** O(n).
- **Space:** O(n) — the map can hold up to n distinct keys.

Linear time, but O(n) space. The Boyer–Moore generalization brings space down to O(k), which
matters for streaming or very large / high-cardinality inputs.

## Optimal Approach — k−1 Candidate Boyer–Moore (Misra–Gries)

**Key fact:** at most `k − 1` values can each appear more than `n/k` times. Maintain a
dictionary of **at most k − 1** `candidate -> count` slots. For each element `x`:

1. If `x` is already a candidate, increment its count.
2. Else if fewer than `k − 1` candidates are currently tracked, add `x` with count 1.
3. Else decrement **every** candidate's count by 1, and drop any candidate that hits 0.

Then **verify**: recount each surviving candidate over `nums` and keep those exceeding
`n // k`.

```python
def elementsMoreThanNOverK(nums, k):
    counts = {}                     # at most k-1 entries
    for x in nums:
        if x in counts:
            counts[x] += 1
        elif len(counts) < k - 1:
            counts[x] = 1
        else:
            for key in list(counts):
                counts[key] -= 1
                if counts[key] == 0:
                    del counts[key]

    n = len(nums)
    res = []
    for c in counts:                # candidates that survived voting
        if nums.count(c) > n // k:
            res.append(c)
    return res
```

### Why it is correct

This is exactly Boyer–Moore with `k − 1` slots. Each "decrement-all" step removes `k`
elements from consideration at once (the current `x` plus one unit from each of the `k − 1`
candidates) — think of it as discarding a group of `k` mutually distinct items. A value `v`
occurring more than `n/k` times cannot be eliminated by these group-discards: there can be at
most `⌊n/k⌋` such groups, and each removes at most one `v`, so more than `n/k` copies of `v`
guarantees at least one survives in the table. Therefore every true >n/k value is among the
survivors. The verification pass discards survivors that are not genuinely frequent (the table
can retain low-frequency junk when fewer than k−1 qualifying values exist).

### Worked trace on `[3, 1, 2, 2, 1, 2, 3, 3]`, k = 4 (so up to 3 candidates, threshold 2)

| x | rule | table (candidate:count) |
|---|------|-------------------------|
| 3 | add (0 < 3) | `{3:1}` |
| 1 | add (1 < 3) | `{3:1, 1:1}` |
| 2 | add (2 < 3) | `{3:1, 1:1, 2:1}` |
| 2 | present → +1 | `{3:1, 1:1, 2:2}` |
| 1 | present → +1 | `{3:1, 1:2, 2:2}` |
| 2 | present → +1 | `{3:1, 1:2, 2:3}` |
| 3 | present → +1 | `{3:2, 1:2, 2:3}` |
| 3 | present → +1 | `{3:3, 1:2, 2:3}` |

Survivors: `3, 1, 2`. Verify against threshold 2: `count(3)=3 > 2` ✓, `count(1)=2` ✗,
`count(2)=3 > 2` ✓. Result `[3, 2]` (order-independent, equals `[2, 3]`). ✓

- **Time:** O(n·k) — each of n elements may trigger a decrement over up to k−1 slots, plus
  the verification counts. (With a min-oriented structure this can be tightened, but O(n·k)
  is the standard bound.)
- **Space:** O(k) — at most k−1 candidate slots.

## Key Insights & Edge Cases

- **k = 2 recovers plain majority** (one candidate); **k = 3 recovers Majority Element II**
  (two candidates). This problem is the unifying generalization.
- **Verification is mandatory** — the table can hold up to k−1 survivors even when none truly
  exceed n/k (e.g. `[1, 2, 3, 4, 5], k = 2`).
- **Decrement affects *all* candidates** on a non-matching, table-full element, and you must
  delete entries that reach 0 so a new candidate can take the freed slot.
- Iterate over a snapshot of the keys (`list(counts)`) while deleting, to avoid mutating the
  dict during iteration.
- Edge cases: `k` larger than the number of distinct values, all-identical arrays, and arrays
  with no qualifying element (returns `[]`) all behave correctly.
