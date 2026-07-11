# Solution — Top K Frequent Elements

## Brute Force

Count frequencies, sort the distinct elements by count descending, take the first `k`.

```python
from collections import Counter

def topKFrequent(self, nums, k):
    counts = Counter(nums)
    return [x for x, _ in counts.most_common(k)]
```

- **Time:** `O(n + m log m)` where `m` is the number of distinct elements (the sort dominates).
- **Space:** `O(m)` for the frequency map.

A **min-heap of size k** keyed by frequency gives `O(n + m log k)` — better when
`k << m`. Both are standard and fully acceptable; Quickselect improves the selection step
to expected linear.

## Optimal Approach (Quickselect)

1. Build a frequency map `counts` with `Counter(nums)` — `O(n)`.
2. Let `unique = list(counts.keys())` be the `m` distinct elements.
3. The task becomes: **select the k elements of `unique` with the largest `counts` value.**
   That is a selection problem, solved by Quickselect keyed by frequency.

### Why it is correct

We want the k **largest** frequencies, so the target boundary is index `m - k` when the
unique list is arranged ascending by frequency. Partition around a pivot frequency so that
elements with smaller frequency go left and larger go right; the pivot lands at its final
index `p`:

- If `p == m - k`, then indices `m - k .. m - 1` hold the k highest-frequency elements —
  return `unique[m - k:]`.
- If `p < m - k`, the boundary is further right: search `[p + 1, hi]`.
- If `p > m - k`, search `[lo, p - 1]`.

Because the answer is guaranteed unique (the k-th count strictly exceeds the (k+1)-th),
there is no tie straddling the boundary, so the returned set is unambiguous.

### Reference implementation

```python
import random
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        unique = list(counts.keys())
        n = len(unique)
        target = n - k                       # boundary for the top-k largest

        def partition(lo: int, hi: int) -> int:
            rand = random.randint(lo, hi)
            unique[rand], unique[hi] = unique[hi], unique[rand]
            pivot_freq = counts[unique[hi]]
            i = lo
            for j in range(lo, hi):
                if counts[unique[j]] <= pivot_freq:
                    unique[i], unique[j] = unique[j], unique[i]
                    i += 1
            unique[i], unique[hi] = unique[hi], unique[i]
            return i

        lo, hi = 0, n - 1
        while lo <= hi:
            p = partition(lo, hi)
            if p == target:
                break
            elif p < target:
                lo = p + 1
            else:
                hi = p - 1
        return unique[target:]
```

- **Time:** `O(n)` to count + expected `O(m)` to select = expected `O(n)` overall.
- **Space:** `O(m)` for the frequency map and unique list.

## Key Insights & Edge Cases

- **Two-stage reduction:** raw array -> frequency map -> selection over *distinct* keys.
  Quickselect runs on the `m` unique elements, not the `n` raw values.
- **Compare by frequency, carry the element.** The key is `counts[element]`; the element
  itself is what you swap and ultimately return.
- **Top-k = largest -> boundary `m - k`.** Return the **suffix** `unique[target:]`. A common
  mistake is returning the prefix (which would give the least frequent).
- **k == m:** target becomes `0`, the loop returns everything — correct.
- **Uniqueness guarantee** means no boundary tie; without it you would need a tie-breaking
  rule to decide which equally frequent element makes the cut.
- **Randomize the pivot** to preserve expected-linear behavior even when frequencies arrive
  in sorted order.
