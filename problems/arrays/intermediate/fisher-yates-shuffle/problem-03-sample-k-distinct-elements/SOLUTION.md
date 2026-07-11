# Sample K Distinct Elements — Solution

## Brute Force

**Full shuffle, then take a prefix.** Run a complete Fisher–Yates shuffle over a copy
of `nums`, then return the first `k` elements.

```python
arr = nums[:]
for i in range(len(arr) - 1, 0, -1):
    j = random.randint(0, i)
    arr[i], arr[j] = arr[j], arr[i]
return arr[:k]
```

This is perfectly uniform (a uniformly random permutation's first `k` entries form a
uniformly random `k`-subset in random order), but it always does `n-1` swaps even when
`k` is tiny.

- **Time:** O(n).
- **Space:** O(n) for the copy.

An alternative brute force is rejection sampling with a `set`: draw random elements
until `k` distinct ones are collected — O(k) when `k << n` but degrades toward
coupon-collector behavior as `k` approaches `n`.

## Optimal Approach (Partial Fisher–Yates Shuffle)

You do not need to finish the whole shuffle. To fix the first `k` positions of the
permutation it suffices to run only the **first `k` iterations** of a forward
Fisher–Yates sweep:

1. Copy `nums` into `arr` (length `n`).
2. For `i` from `0` to `k-1`:
   - Pick a uniformly random index `j` in the **inclusive** range `[i, n-1]`.
   - Swap `arr[i]` and `arr[j]`.
3. Return `arr[:k]`.

After iteration `i`, position `i` holds an element chosen uniformly from all elements
not yet placed in positions `0..i-1`. That is exactly the definition of sampling
without replacement.

### Why it is correct

At step `i` there are `n - i` unplaced candidates and each is equally likely to be
swapped into slot `i`. So the first pick is uniform over `n`, the second over the
remaining `n-1`, and so on: the probability of any specific ordered `k`-tuple is

```
1/n * 1/(n-1) * ... * 1/(n-k+1) = (n-k)! / n!
```

Summing over the `k!` orderings of a given subset gives `k! (n-k)! / n! = 1 / C(n, k)`,
so every `k`-subset is equally likely. Only `k` random draws are made.

### Reference implementation

```python
import random
from typing import List


def sample_k(nums: List[int], k: int) -> List[int]:
    arr = nums[:]
    n = len(arr)
    for i in range(k):
        j = random.randint(i, n - 1)   # inclusive: pick from the unpicked suffix
        arr[i], arr[j] = arr[j], arr[i]
    return arr[:k]
```

### Complexity

- **Time:** O(k) random draws and swaps, plus O(n) once to copy the input (O(k) extra
  work if you are allowed to mutate `nums` in place).
- **Space:** O(n) for the working copy, or O(k) if you sample in place and return a
  slice.

## Key Insights & Edge Cases

- **Only `k` iterations.** The forward sweep lets you stop early; the backward sweep
  from Problem 1 would require running all the way down, so use the forward variant
  here.
- **Inclusive range `[i, n-1]`.** Including `i` itself keeps the element originally at
  `i` in the running for slot `i`, preserving uniformity.
- **`k == 0`** returns `[]` (loop never runs). **`k == n`** is a complete shuffle.
- **Distinctness of output** comes for free: swapping never duplicates an element, so
  as long as inputs are distinct the sample is too.
- **Huge `n`, small `k`.** This is where partial Fisher–Yates shines — O(k) draws
  instead of O(n). If you must not touch `nums` and `n` is enormous, use a hash map to
  record only the swapped slots (the same map-backed idea used in Problems 4 and 5).
