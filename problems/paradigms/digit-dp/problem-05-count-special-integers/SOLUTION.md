# Solution — Count Special Integers

## Brute Force

Iterate `x` from `1` to `n` and check `len(set(str(x))) == len(str(x))`.

```python
def countSpecialNumbers(n: int) -> int:
    count = 0
    for x in range(1, n + 1):
        s = str(x)
        if len(set(s)) == len(s):
            count += 1
    return count
```

- **Time:** `O(n * log n)`.
- **Space:** `O(log n)`.

`n` can be `2 * 10^9`, so this is billions of iterations — infeasible. We need to
count without enumerating.

## Optimal Approach (Digit DP with a used-digit bitmask)

Building the number left to right, "all digits distinct" requires knowing which
digits are already used. A 10-bit mask (`bit d = 1` means digit `d` is taken)
captures that in the DP state. The subtlety is **leading zeros**: a number like
`57` has an implicit leading zero (`057`) when compared against a 3-digit bound,
but that leading zero must **not** be recorded as "digit `0` is used", or we
would wrongly reject numbers that legitimately contain a `0` later.

State:

- `pos` — current digit index (0 = MSB of the bound).
- `mask` — 10-bit set of digits already placed in *real* positions.
- `tight` — prefix equals bound's prefix (caps the current digit).
- `started` — whether we have placed a first nonzero digit yet (i.e. the number
  has actually begun). While `started` is `False`, chosen `0`s are leading zeros.

Transition at `pos`, with `hi = digits[pos] if tight else 9`, for each `d` in
`0..hi`:

- If `not started and d == 0`: still a leading zero — recurse with the mask
  unchanged, `started = False`, `tight = tight and d == hi`. **Do not** set a
  mask bit.
- Else (this is a real digit): if bit `d` is already in `mask`, skip (would
  repeat a digit). Otherwise recurse with `mask | (1 << d)`, `started = True`,
  `tight = tight and d == hi`.

Base case: `pos == len(digits)` returns `1 if started else 0` (the all-leading-
zeros path represents `0`, which is outside `[1, n]`).

```python
from functools import lru_cache

def countSpecialNumbers(n: int) -> int:
    digits = list(map(int, str(n)))
    L = len(digits)

    @lru_cache(maxsize=None)
    def dp(pos: int, mask: int, tight: bool, started: bool) -> int:
        if pos == L:
            return 1 if started else 0
        hi = digits[pos] if tight else 9
        total = 0
        for d in range(hi + 1):
            new_tight = tight and d == hi
            if not started and d == 0:
                # leading zero: number hasn't started, digit not "used"
                total += dp(pos + 1, mask, new_tight, False)
            else:
                if mask & (1 << d):
                    continue  # digit already used -> not distinct
                total += dp(pos + 1, mask | (1 << d), new_tight, True)
        return total

    return dp(0, 0, True, False)
```

Why it is correct: the DP enumerates each integer in `[0, n]` once. The
`started` flag ensures leading zeros neither count as a used digit nor make the
final number equal to `0` be counted (base case excludes `started == False`).
Skipping digits already in `mask` enforces distinctness, and `tight` keeps every
generated number `<= n`.

- **Time:** `O(L * 2^10 * 2 * 2 * 10)` — states `(pos, mask, tight, started)`
  times 10 digit transitions. `L <= 10`, so ~2 * 10^5 operations, trivially fast.
- **Space:** `O(L * 2^10)` for the memo.

### Combinatorial cross-check

For lengths strictly less than `L`, the count of length-`m` distinct-digit
numbers is `9 * 9 * 8 * ... ` (first digit `1..9`, then permute the rest from the
remaining digits). Summing those plus the tight same-length count reproduces the
DP answer; the DP is preferred because it handles the tight boundary uniformly.

## Key Insights & Edge Cases

- **Leading-zero flag is essential.** Without `started`, a leading `0` would set
  `mask` bit 0 and incorrectly forbid a real `0` appearing later (e.g. `1024`).
- **`mask` must be part of the memo key**; two prefixes at the same `pos` with
  different used-digit sets have different valid completions.
- **`started` is also part of the key** because the transition rules differ
  before vs. after the number has begun.
- **Single-digit numbers** (`n <= 9`) are all special, matching Example 2.
- **Upper bound `2 * 10^9`** has 10 digits; `10` distinct decimal digits max out
  at length 10, so no number longer than 10 digits can be special anyway — but
  the DP handles this automatically via `mask` exhaustion.
