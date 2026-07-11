# Top K Frequent Elements — Solution

## Brute Force

**Count then sort by frequency.** Build a frequency map, sort the distinct keys by
frequency descending, and take the first `k`.

```python
from collections import Counter
freq = Counter(nums)
return [v for v, _ in freq.most_common(k)]
```

- **Time:** O(n) to count + O(m log m) to sort the `m` distinct values.
- **Space:** O(m).

A min-heap of size `k` gives O(m log k). The follow-up asks to beat O(n log n), and
Quickselect delivers O(m) average.

## Optimal Approach (Quickselect on frequency)

1. **Count** frequencies in O(n) with a hash map: `freq[value] -> count`.
2. Put the **distinct values** into an array `unique`. Let `m = len(unique)`.
3. Run **Quickselect** on `unique` using `freq[value]` as the key so that the array is
   partitioned into a low-frequency part and a high-frequency part. We want the `k`
   **most** frequent at the right end, so target the boundary index `n - k` (ascending
   by frequency): after selection, `unique[m-k .. m-1]` are the `k` most frequent.
4. Return `unique[m - k:]`.

### Why it is correct

Counting is exact. Quickselect places one element (the pivot) at its final rank-by-
frequency position on each partition and moves less-frequent values left. When the
partition boundary reaches index `m - k`, everything at indices `[m-k, m-1]` has
frequency `>=` everything to its left, so those are exactly the `k` most frequent
distinct values. Their internal order is irrelevant since any order is accepted.

### Reference implementation

```python
import random
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        unique = list(freq.keys())
        n = len(unique)
        target = n - k  # we want indices [target, n-1] = k most frequent

        def partition(lo: int, hi: int) -> int:
            r = random.randint(lo, hi)
            unique[r], unique[hi] = unique[hi], unique[r]
            pivot_freq = freq[unique[hi]]
            i = lo
            for j in range(lo, hi):
                if freq[unique[j]] < pivot_freq:
                    unique[i], unique[j] = unique[j], unique[i]
                    i += 1
            unique[i], unique[hi] = unique[hi], unique[i]
            return i

        lo, hi = 0, n - 1
        while lo < hi:
            p = partition(lo, hi)
            if p == target:
                break
            elif p < target:
                lo = p + 1
            else:
                hi = p - 1
        return unique[target:]
```

### Complexity

- **Time:** O(n) to count + O(m) expected for Quickselect = **O(n)** average
  (`m <= n`). Worst case O(m^2), mitigated by the random pivot.
- **Space:** O(m) for the frequency map and the distinct-value array.

## Key Insights & Edge Cases

- **The key is the frequency, not the value.** We partition `unique` but compare
  `freq[unique[j]]`. Do not accidentally partition on the raw value.
- **Boundary index `n - k`** collects the top `k` at the *right* end. Equivalently you
  could negate frequencies and select the smallest `k` at the left end.
- **`k == m`** (all distinct values) returns everything; the loop exits immediately and
  `unique[target:]` is the whole array.
- **Single element** (`nums = [1], k = 1`) yields one distinct value returned directly.
- The answer is guaranteed unique, so we never have to break frequency ties in a
  specific way.
