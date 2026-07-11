# Random Flip Matrix — Solution

## Brute Force

**Store the free cells / reject-and-retry.**

- *Materialize:* keep a list of all `total = m * n` cell ids that are still `0`. On
  `flip()`, pick a random index into that list, swap the chosen id to the end, and pop
  it. This is a literal Fisher–Yates, but it costs **O(m·n) memory** — up to `10^8`
  entries for a `10^4 x 10^4` grid — which is far too much.
- *Reject-and-retry:* store flipped ids in a `set`; draw a random id in `[0, total)`
  and retry while it is already flipped. Cheap early on, but once most cells are `1`
  each `flip()` retries many times (expected retries → total as the grid fills), so it
  degrades badly.

- **Time:** materialize is O(1) per flip; reject-and-retry is O(1) early, unbounded
  late.
- **Space:** materialize O(m·n); reject-and-retry O(k) for `k` flips.

## Optimal Approach (Lazy map-backed Fisher–Yates)

Flatten the grid into a virtual array of ids `0 .. total-1`, with
`id -> (id // n, id % n)`. Run a Fisher–Yates shuffle over this virtual array but
**store only the swaps** in a hash map, so memory grows with the number of flips, not
with `total`.

State: an integer `remaining` (how many `0` cells are left) and a dict `swap` mapping a
slot to the id currently living there.

`flip()`:

1. `remaining -= 1`.
2. Draw `x = randint(0, remaining)` — inclusive, so the range has `remaining + 1`
   values, exactly the number of cells that were free before this flip.
3. The chosen id is `chosen = swap.get(x, x)` (follow the remap if slot `x` was moved
   earlier, else it is `x` itself).
4. Move the id currently sitting in the *last live slot* (`remaining`) into slot `x`:
   `swap[x] = swap.get(remaining, remaining)`. This is the Fisher–Yates swap of `x`
   with the shrinking tail.
5. Return `[chosen // n, chosen % n]`.

`reset()`: clear `swap` and restore `remaining = total`.

### Why it is correct

Before a flip there are `r + 1` free cells (where `r` is the post-decrement
`remaining`). Step 2 draws uniformly over exactly those `r + 1` slots, and the `swap`
lookups keep the mapping a bijection onto the still-free ids. So every free cell is
chosen with probability `1 / (r + 1)` — uniform. Step 4 removes the chosen cell from
the pool by pulling the last live id into the vacated slot, shrinking the effective
array by one, which is the standard partial Fisher–Yates invariant applied one draw at
a time across `flip()` calls.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.swap = {}          # slot -> id currently stored there

    def flip(self) -> List[int]:
        self.remaining -= 1
        x = random.randint(0, self.remaining)          # inclusive [0, remaining]
        chosen = self.swap.get(x, x)                    # follow remap if any
        # move the last live id into slot x
        self.swap[x] = self.swap.get(self.remaining, self.remaining)
        return [chosen // self.n, chosen % self.n]

    def reset(self) -> None:
        self.remaining = self.total
        self.swap.clear()
```

### Complexity

- **Time:** O(1) per `flip()` (one random draw and a couple of dict operations); O(1)
  per `reset()` amortized (`dict.clear`).
- **Space:** O(k) where `k` is the number of flips since the last reset — the map holds
  at most one entry per flip, never O(m·n).

## Key Insights & Edge Cases

- **Decrement before drawing.** `remaining -= 1` then `randint(0, remaining)` gives an
  inclusive range whose size equals the number of currently-free cells. Off-by-one here
  is the classic bug — an exclusive `randrange(remaining)` would never pick the last
  slot.
- **`swap.get(x, x)` twice, for two different purposes.** Once to resolve the *chosen*
  id, once to find the *last live* id being pulled into slot `x`. Both must go through
  the map.
- **Never materialize the grid.** `total` can be `10^8`+, so the map-backed shuffle is
  what makes the problem feasible — the same idea as Random Pick with Blacklist
  (Problem 4), applied incrementally per flip.
- **`reset()` is cheap.** Just clear the map and reset the counter; do not rebuild any
  array.
- **id ↔ (row, col):** `row = id // n`, `col = id % n`. Using `m` instead of `n` as the
  divisor is a common mistake — divide by the number of **columns** `n`.
