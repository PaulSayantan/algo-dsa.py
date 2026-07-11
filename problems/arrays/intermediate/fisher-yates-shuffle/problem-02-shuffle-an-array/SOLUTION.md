# Shuffle an Array — Solution

## Brute Force

**Draw-and-remove.** Keep the original array. For `shuffle()`, copy the elements into
a pool `list`, then repeatedly pop a random index out of the pool and append it to the
result until the pool is empty.

```python
def shuffle(self):
    pool = list(self.original)
    out = []
    while pool:
        idx = random.randrange(len(pool))
        out.append(pool.pop(idx))   # pop from the middle is O(len(pool))
    return out
```

- **Time:** O(n^2) per shuffle, because `list.pop(idx)` shifts all later elements. It
  *is* uniform (it is Fisher–Yates in disguise), just slow.
- **Space:** O(n) for the pool plus the output.

## Optimal Approach (Fisher–Yates Shuffle)

Store two things at construction time:

- `self.original` — an immutable snapshot so `reset()` can always rebuild the exact
  starting order.
- `self.arr` — a working copy that `shuffle()` rearranges in place.

`reset()` copies `self.original` back into `self.arr` and returns it. `shuffle()`
applies the in-place Fisher–Yates sweep to `self.arr`:

1. For `i` from `n-1` down to `1`, pick a uniformly random `j` in the inclusive range
   `[0, i]`.
2. Swap `arr[i]` and `arr[j]`.
3. Return the shuffled `arr`.

### Why it is correct

Fisher–Yates yields each of the `n!` permutations with probability `1/n!` (see
Problem 1's proof). The only additional requirement here is **isolation**: `shuffle()`
must never corrupt the original. Keeping a separate `self.original` snapshot — and
returning a *copy* from `reset()` if the caller might mutate it — guarantees repeated
`shuffle()`/`reset()` calls stay independent and correct.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]   # immutable snapshot
        self.arr = nums[:]        # working copy

    def reset(self) -> List[int]:
        self.arr = self.original[:]
        return self.arr

    def shuffle(self) -> List[int]:
        for i in range(len(self.arr) - 1, 0, -1):
            j = random.randint(0, i)      # inclusive
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr
```

### Complexity

- **Time:** O(n) per `shuffle()`, O(n) per `reset()`.
- **Space:** O(n) total to hold the original snapshot and the working copy.

## Key Insights & Edge Cases

- **Snapshot with a copy, not a reference.** `self.original = nums` (no slice) would
  alias the same list, so shuffling `self.arr` could corrupt the "original." Always
  copy with `nums[:]` (or `list(nums)`).
- **Inclusive bound `[0, i]`.** As in the base algorithm, this is what keeps the
  distribution uniform.
- **Repeated calls.** Because we shuffle a copy and reset from the snapshot, any
  interleaving of `reset()` and `shuffle()` behaves correctly.
- **Single element / already shuffled state.** With `n == 1` the loop is empty and both
  operations return the same one-element array.
- **Returning a copy from `reset()`.** If test harnesses mutate returned arrays, return
  `self.arr[:]` to avoid outside code altering internal state.
