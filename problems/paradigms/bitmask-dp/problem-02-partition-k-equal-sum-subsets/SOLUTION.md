# Partition to K Equal Sum Subsets — Solution

## Brute Force

Recursively try to place each element into one of the `k` buckets and check at
the end whether all buckets equal `total / k`.

- **Time:** `O(k^n)` — every element chooses one of `k` buckets. With `n = 16`
  and `k = 16` this is astronomically large without pruning.
- **Space:** `O(n)` recursion depth plus `O(k)` bucket sums.

Standard optimizations (sort descending, skip duplicate bucket states, prune
when a bucket overflows) make it pass, but the state is re-explored across
different fill orders — that redundancy is what bitmask DP removes.

## Optimal Approach (Bitmask DP)

### Setup and feasibility check

Let `total = sum(nums)`. If `total % k != 0`, return `False` immediately.
Let `target = total / k`. If any single element exceeds `target`, return
`False`.

### Key observation

Fill buckets **one at a time**. We never actually need to know *which* bucket
we are on — only how much of the current bucket is filled. When the current
bucket reaches exactly `target`, it closes and the next element begins a new
bucket at sum `0`. If we manage to use every element this way, the number of
completed buckets is automatically `total / target = k`.

So the only state we need is the set of used elements, encoded as a bitmask.

### DP definition

Let `used[mask]` = `True` if the subset of elements in `mask` can be arranged
so that the buckets filled so far are all complete except possibly the last one
in progress. Define a companion quantity:

```
partial(mask) = (sum of nums[i] for bits i set in mask) % target
```

`partial(mask)` is exactly how full the currently-open bucket is, because every
completed bucket contributes a multiple of `target` and drops out under the
modulo.

- **Base case:** `used[0] = True` (nothing placed yet).
- **Transition:** for every reachable `mask` and every unused element `i`
  with `nums[i] + partial(mask) <= target`:

  ```
  used[mask | (1 << i)] = True
  ```

  The constraint `partial(mask) + nums[i] <= target` guarantees we never
  overflow the open bucket; when the sum lands exactly on `target`, `partial`
  wraps back to `0` and the next added element starts a fresh bucket.

- **Answer:** `used[(1 << n) - 1]`.

### Why it is correct

Because each element is worth at most `target`, the running total
`sum(mask)` only crosses multiples of `target` by *exactly landing on them*
(the `<= target` guard forbids skipping over a boundary within one bucket).
Therefore reaching the full mask means the total `k * target` was accumulated
as `k` complete buckets — a valid partition. Conversely any valid partition
corresponds to some order of adding elements that respects the guard, so it is
reachable. The bitmask collapses all fill orders that use the *same set* of
elements into a single state, eliminating the exponential redundancy of naive
recursion.

### Reference implementation

```python
class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        if max(nums) > target:
            return False

        n = len(nums)
        full = (1 << n) - 1
        used = [False] * (1 << n)
        used[0] = True

        # precompute subset sums for O(1) partial lookup
        subset_sum = [0] * (1 << n)
        for mask in range(1, 1 << n):
            low = mask & (-mask)
            i = low.bit_length() - 1
            subset_sum[mask] = subset_sum[mask ^ low] + nums[i]

        for mask in range(1 << n):
            if not used[mask]:
                continue
            rem = subset_sum[mask] % target  # fill level of open bucket
            for i in range(n):
                if mask & (1 << i):
                    continue
                if rem + nums[i] <= target:
                    used[mask | (1 << i)] = True
        return used[full]
```

- **Time:** `O(2^n * n)` — each of `2^n` masks tries `n` extensions.
- **Space:** `O(2^n)` for `used` and `subset_sum`.

## Key Insights & Edge Cases

- **Modulo trick:** storing `sum(mask) % target` instead of a bucket index is
  what lets the state be a single mask. Completed buckets vanish under the mod.
- **Early exits:** `total % k != 0` and `max(nums) > target` prune impossible
  inputs before any DP work.
- **`k = 1`** trivially returns `True` (the whole array is the one subset),
  handled because `target = total` and every element fits.
- **`k = len(nums)`** requires all elements equal; the guard naturally enforces
  it because any element below/above `target` breaks the fill.
- **Non-empty subsets:** since every `nums[i] >= 1` and buckets must each reach
  `target >= 1`, no bucket can be empty, so the "non-empty" requirement is met
  automatically.
- **Precomputing `subset_sum`** avoids recomputing popcount-weighted sums and
  keeps the inner loop `O(1)` per element.
