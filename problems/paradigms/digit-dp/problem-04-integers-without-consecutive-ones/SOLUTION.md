# Solution — Non-negative Integers Without Consecutive Ones

## Brute Force

Check every integer from `0` to `n`; for each, test whether its binary form has
two adjacent `1`s. A neat bit trick: `x` has consecutive ones iff `x & (x >> 1)`
is non-zero.

```python
def findIntegers(n: int) -> int:
    count = 0
    for x in range(n + 1):
        if (x & (x >> 1)) == 0:
            count += 1
    return count
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

With `n` up to `10^9` this is ~`10^9` iterations — too slow within typical limits.

## Optimal Approach (Digit DP in base 2)

Because the forbidden pattern is *adjacent bits*, we run the digit DP over the
**binary** digits of `n`. Represent `n` as its bit string `bits` from the most
significant bit to the least.

State:

- `pos` — current bit index (0 = MSB).
- `prev` — the bit we placed at `pos - 1` (0 or 1). This is the only history we
  need, since "no two adjacent 1s" is a purely local, first-order constraint.
- `tight` — whether the prefix of chosen bits equals `n`'s prefix (caps the
  current bit at `bits[pos]`).

Transition at `pos`: let `hi = bits[pos] if tight else 1`. Try each bit
`b` in `range(hi + 1)`; skip the choice `b == 1 and prev == 1` (that would create
adjacent ones). Recurse with `prev = b` and `tight = tight and b == hi`.

Base case: `pos == len(bits)` returns `1` (any completed path that never violated
the rule is a valid number, and includes `0` via the all-zeros path).

```python
from functools import lru_cache

def findIntegers(n: int) -> int:
    bits = bin(n)[2:]          # binary string, MSB first
    L = len(bits)

    @lru_cache(maxsize=None)
    def dp(pos: int, prev: int, tight: bool) -> int:
        if pos == L:
            return 1
        hi = int(bits[pos]) if tight else 1
        total = 0
        for b in range(hi + 1):
            if b == 1 and prev == 1:
                continue
            total += dp(pos + 1, b, tight and b == hi)
        return total

    return dp(0, 0, True)
```

Why it is correct: the DP enumerates every integer in `[0, n]` exactly once
(the tight flag prevents exceeding `n`; leading zeros just represent smaller
numbers). A path is counted iff it never places a `1` immediately after another
`1`, which is exactly the "no consecutive ones" property. Starting `prev = 0` is
safe because a leading `1` has no predecessor `1`.

- **Time:** `O(L * 2 * 2 * 2)` — states `(pos, prev, tight)` with 2 bit choices.
  `L = 30` for `n <= 10^9`, so this is a few hundred operations.
- **Space:** `O(L)`.

### Fibonacci insight (why the loose counts are Fibonacci numbers)

The number of length-`m` bit strings with no two adjacent ones (leading zeros
allowed) is `Fib(m + 2)`. The classic closed-form solution to this problem walks
the bits of `n` from MSB to LSB, and whenever it sees a set bit at position `i`
it adds `Fib(i + 1)` (counting all valid numbers with a `0` fixed at that
position), stopping early if it ever encounters two consecutive set bits in `n`
itself. The digit DP above computes the same quantity but generalizes to other
bit constraints without re-deriving the recurrence.

## Key Insights & Edge Cases

- **Base matters:** the constraint is on binary adjacency, so the "digits" are
  bits and the alphabet is `{0, 1}`. Running a base-10 digit DP here would be a
  modeling error.
- **`prev` is enough history:** first-order adjacency constraints need only the
  immediately previous symbol in the state — no full mask required.
- **`0` is included:** the range is `[0, n]`, and the all-zeros path yields `0`,
  which is valid. That is why Example 2 returns `2`, not `1`.
- **`n` may itself contain adjacent ones** (e.g. `n = 3 = 0b11`); the tight path
  simply gets pruned at the offending bit, and looser paths still contribute.
- **Leading zeros don't create false adjacency** because a leading `0` followed
  by `1` is fine; only `1` then `1` is forbidden.
