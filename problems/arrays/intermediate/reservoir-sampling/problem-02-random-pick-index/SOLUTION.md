# Solution — Random Pick Index

## Brute Force

In the constructor, build a hash map from each value to the list of indices where it
appears. Then `pick(target)` just picks a random index from `map[target]`.

```python
class Solution:
    def __init__(self, nums):
        self.idx = collections.defaultdict(list)
        for i, v in enumerate(nums):
            self.idx[v].append(i)

    def pick(self, target):
        return random.choice(self.idx[target])
```

- **Time:** `O(n)` to build the map; `O(1)` per `pick`.
- **Space:** `O(n)` extra for the map.

Fast per query, but it uses `O(n)` extra memory — it fails the `O(1)`-extra-space
follow-up. It is the right choice when `pick` is called very frequently and memory is
plentiful.

## Optimal Approach (Reservoir Sampling, k = 1)

Treat the positions where `nums[i] == target` as a stream. Walk the whole array once per
`pick`; each time you hit a match, increment a `count` and adopt the current index as the
answer with probability `1/count`.

### Why it is correct

Suppose `target` occurs at positions `p_1 < p_2 < ... < p_m`. When we encounter the
`t`-th match we keep it with probability `1/t`. Position `p_t` is the final answer iff we
adopt it at its match **and** never adopt a later match:

```
P(return p_t) = (1/t) · (1 - 1/(t+1)) · (1 - 1/(t+2)) · ... · (1 - 1/m)
              = (1/t) · (t/(t+1)) · ((t+1)/(t+2)) · ... · ((m-1)/m)
              = (1/t) · (t/m)                # telescoping
              = 1/m
```

So each of the `m` matching indices is returned with probability `1/m` — uniform.

### Step-by-step

1. Initialize `count = 0` and `result = -1`.
2. Iterate `i` over `nums`. Skip if `nums[i] != target`.
3. On a match: `count += 1`; with probability `1/count` set `result = i`
   (e.g. `if random.randint(1, count) == 1`).
4. After the pass, return `result`.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums            # no per-value index map -> O(1) extra space

    def pick(self, target: int) -> int:
        count = 0
        result = -1
        for i, v in enumerate(self.nums):
            if v != target:
                continue
            count += 1
            if random.randint(1, count) == 1:   # keep this match with prob 1/count
                result = i
        return result
```

- **Time:** `O(n)` per `pick` (single scan of the array).
- **Space:** `O(1)` extra beyond storing `nums`.

## Key Insights & Edge Cases

- **Reservoir over a filtered stream.** The reservoir logic runs only over matching
  positions; non-matches are ignored, so `count` tracks *matches seen*, not array index.
- **Probability `1/count`, not `1/i`.** Using the array index instead of the match count
  would bias the result — always divide by the number of matches encountered so far.
- **Single occurrence:** the first (and only) match sets `result` at `count = 1` with
  probability `1`, so a unique target always returns its lone index.
- **All elements equal to target:** degenerates to the classic `k = 1` reservoir over the
  whole array, returning any index with probability `1/n`.
- **Space/time trade-off:** this is the mirror image of the brute force — `O(1)` extra
  space but `O(n)` per query. Choose based on how many `pick` calls you expect versus how
  much memory you can spend.
