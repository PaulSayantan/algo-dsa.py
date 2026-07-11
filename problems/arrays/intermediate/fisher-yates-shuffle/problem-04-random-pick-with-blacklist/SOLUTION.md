# Random Pick with Blacklist — Solution

## Brute Force

**Reject-and-retry.** Store the blacklist in a `set`. On `pick()`, draw a random value
in `[0, n-1]` and retry while it is blacklisted.

```python
def pick(self):
    x = random.randrange(self.n)
    while x in self.black:
        x = random.randrange(self.n)
    return x
```

- **Time:** O(1) expected only when the blacklist is sparse. If the blacklist covers a
  large fraction of `[0, n-1]`, the expected number of retries blows up (unbounded as
  the allowed fraction → 0).
- **Space:** O(B) for the blacklist set, where `B = len(blacklist)`.

A second brute force materializes the full list of allowed values and indexes into it —
that is O(1) per pick but needs **O(n) memory**, which is impossible for `n` up to
`10^9`.

## Optimal Approach (Map-backed Fisher–Yates remap)

Let `m = n - B` be the count of allowed values. Key idea: **force every pick to come
from the compact prefix `[0, m)`**. Some of those prefix indices are themselves
blacklisted; redirect each of those to a distinct *allowed* value living in the tail
`[m, n)`. This is precisely the "swap into a smaller region, remember only the swaps in
a hash map" flavor of Fisher–Yates.

Construction:

1. Put every blacklisted value into a set. Compute `m = n - B`.
2. Collect the allowed values in the tail `[m, n)` (there are exactly as many free
   tail slots as there are blacklisted values sitting in `[0, m)`).
3. For each blacklisted value `b < m`, pop an allowed tail value `w` from step 2 and
   record `remap[b] = w`.

Query:

- `pick()` draws `x = randrange(m)`. If `x` is a remapped (blacklisted) prefix index,
  return `remap[x]`; otherwise return `x` itself.

### Why it is correct

Every draw is uniform over the `m` indices in `[0, m)`. Each index maps to exactly one
distinct allowed value: prefix indices that are allowed map to themselves, and prefix
indices that are blacklisted map bijectively to the allowed tail values. Because the
mapping is a bijection from `[0, m)` onto the `m` allowed values, and `x` is uniform
over `[0, m)`, each allowed value is returned with probability exactly `1/m`.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.m = n - len(blacklist)
        black = set(blacklist)
        # Allowed values in the tail [m, n).
        tail = (x for x in range(self.m, n) if x not in black)
        self.remap = {}
        for b in blacklist:
            if b < self.m:               # only prefix blacklisted values need a target
                self.remap[b] = next(tail)

    def pick(self) -> int:
        x = random.randrange(self.m)
        return self.remap.get(x, x)
```

### Complexity

- **Time:** O(B) to build the map; **O(1)** per `pick()`.
- **Space:** O(B) for the remap (at most one entry per blacklisted value), independent
  of `n`.

## Key Insights & Edge Cases

- **Only remap blacklisted values below `m`.** Blacklisted values in `[m, n)` are never
  drawn (picks are from `[0, m)`), so they need no entry — and they are correctly
  excluded when generating tail targets via `x not in black`.
- **The tail has exactly enough allowed slots.** The number of blacklisted values in
  `[0, m)` equals the number of allowed values in `[m, n)`, so `next(tail)` never runs
  dry.
- **Empty blacklist:** `m == n`, the map is empty, and `pick()` is a plain uniform
  draw.
- **`n` up to 10^9:** never build the full range; the map holds at most `B <= 10^5`
  entries. This memory bound is the whole point of the Fisher–Yates remap over the
  materialize-everything approach.
- **Relation to Fisher–Yates:** conceptually you "swap" each blacklisted prefix slot
  with an allowed tail slot and store only that swap — the exact map-backed shuffle
  trick, applied once at construction instead of repeatedly.
