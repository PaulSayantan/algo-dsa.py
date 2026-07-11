# Generate a Random Permutation — Solution

## Brute Force

**Rejection / "pick unused" sampling.** Repeatedly draw a random value in `[0, n-1]`,
keep it if it has not been used yet (track a `set`), and stop once `n` distinct values
have been collected.

```python
seen, out = set(), []
while len(out) < n:
    x = random.randint(0, n - 1)
    if x not in seen:
        seen.add(x)
        out.append(x)
return out
```

- **Time:** O(n) expected, but the last few picks collide often — the classic
  coupon-collector effect makes it degrade badly as the set fills up, and it is O(n^2)
  in the worst case.
- **Space:** O(n) for the `seen` set.

Another brute force is "assign each element a random key, then sort by key" — that is
O(n log n) and needs care to break ties so it stays unbiased.

## Optimal Approach (Fisher–Yates Shuffle)

Build the identity array `arr = [0, 1, ..., n - 1]`, then sweep from the last index
down to index `1`:

1. At index `i`, pick a uniformly random index `j` in the **inclusive** range
   `[0, i]`.
2. Swap `arr[i]` and `arr[j]`.
3. Decrement `i`. Everything from `i+1` onward is now finalized and never touched
   again.

The region `arr[i+1 .. n-1]` is the "already placed" suffix; `arr[0 .. i]` is the pool
of candidates still to be placed. Choosing `j` in `[0, i]` (including `i` itself)
means an element can legitimately "stay put," which is essential for uniformity.

### Why it is correct (unbiased)

Consider the probability that a specific element lands in the last slot `n-1`. On the
first iteration `j` is uniform over `n` choices, so any element goes there with
probability `1/n`. Given that, on the next iteration the chosen element for slot `n-2`
is uniform over the remaining `n-1`, giving `1/(n-1)`, and so on. Multiplying, any
fixed permutation is produced with probability

```
1/n * 1/(n-1) * ... * 1/2 * 1/1 = 1/n!
```

which is uniform over all `n!` orderings. The naive version that draws `j` from the
full range `[0, n-1]` every time instead yields `n^n` equally likely swap sequences;
since `n^n` is not divisible by `n!` for `n >= 3`, that scheme is provably biased.

### Reference implementation

```python
import random
from typing import List


def random_permutation(n: int) -> List[int]:
    arr = list(range(n))
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)   # inclusive on both ends
        arr[i], arr[j] = arr[j], arr[i]
    return arr
```

### Complexity

- **Time:** O(n) — one random draw and one swap per element.
- **Space:** O(1) auxiliary (the array itself is shuffled in place; O(n) only because
  we must return the array).

## Key Insights & Edge Cases

- **Inclusive `[0, i]` is the whole trick.** Using `[0, i-1]` or `[0, n-1]` breaks
  uniformity. `random.randint(0, i)` is inclusive of `i`; `random.randrange(i + 1)`
  is the equivalent.
- **Direction is flexible.** Iterating upward from `0` to `n-1` and picking `j` in
  `[i, n-1]` is the mirror image and equally unbiased.
- **`n == 1` (and `n == 0`)**: the loop body never runs; the single-element (or empty)
  array is already a valid uniform permutation.
- **Do not reseed inside the loop.** One RNG, `n-1` draws — reseeding per iteration
  destroys independence.
- **Quality of randomness matters.** A weak or short-period PRNG cannot reach all `n!`
  states once `n!` exceeds the RNG's state space; use a well-seeded generator for large
  `n`.
