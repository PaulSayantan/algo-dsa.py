# Solution — Rotated Digits

## Brute Force

For each `x` from `1` to `n`, look at every digit. Reject `x` if any digit is in
`{3, 4, 7}`. Otherwise it is *valid*; it is *good* if at least one digit is in
`{2, 5, 6, 9}` (a digit that actually changes on rotation).

```python
def rotatedDigits(n: int) -> int:
    good = 0
    for x in range(1, n + 1):
        s = str(x)
        if any(c in "347" for c in s):
            continue
        if any(c in "2569" for c in s):
            good += 1
    return good
```

- **Time:** `O(n * log n)`.
- **Space:** `O(1)` (or `O(log n)` for the string).

For `n <= 10^4` this is fine, but it does not scale if the bound were `10^18`,
which is exactly the setting Digit DP is built for. We present the Digit DP so
the pattern transfers to larger-bound variants.

## Optimal Approach (Digit DP)

The goodness of a number depends only on which digits it uses:

- It must **never** use a digit in `INVALID = {3, 4, 7}`.
- It must use **at least one** digit in `CHANGES = {2, 5, 6, 9}`.

We count numbers in `[0, n]` meeting both conditions with a digit DP.

State:

- `pos` — current digit index from the most significant end.
- `changed` — boolean, `True` if some digit in `CHANGES` has been placed in
  `[0, pos)`. This is the "contains a rotation-changing digit" flag.
- `tight` — whether the prefix equals `n`'s prefix (caps the current digit).

Transition at `pos`: iterate `d` from `0` to `limit` (`limit = digits[pos]` if
`tight` else `9`). Skip `d` if `d in INVALID` (that branch can never be valid).
Otherwise recurse with `changed or (d in CHANGES)` and `tight and d == limit`.

Base case: at `pos == len(digits)`, return `1` if `changed` else `0`.

```python
from functools import lru_cache

def rotatedDigits(n: int) -> int:
    INVALID = {3, 4, 7}
    CHANGES = {2, 5, 6, 9}
    digits = list(map(int, str(n)))
    L = len(digits)

    @lru_cache(maxsize=None)
    def dp(pos: int, changed: bool, tight: bool) -> int:
        if pos == L:
            return 1 if changed else 0
        limit = digits[pos] if tight else 9
        total = 0
        for d in range(limit + 1):
            if d in INVALID:
                continue
            total += dp(pos + 1, changed or d in CHANGES, tight and d == limit)
        return total

    return dp(0, False, True)
```

Why it is correct: the DP enumerates exactly the integers in `[0, n]` (the
`tight` flag prevents overshoot). A branch survives only if it never places an
invalid digit, and it is counted only if `changed` is true at the end, matching
the definition of *good*. The number `0` maps to the all-zero path, which never
sets `changed`, so it contributes `0` — hence counting over `[0, n]` equals
counting over `[1, n]`.

- **Time:** `O(L * 2 * 2 * 10)` — states `(pos, changed, tight)` times 10 digit
  choices. `L = len(str(n)) <= 5` for `n <= 10^4`.
- **Space:** `O(L)` for the memo and recursion.

## Key Insights & Edge Cases

- **Two independent digit predicates**: one is a *hard filter* (never use
  `3,4,7`) implemented by pruning the branch; the other is an *accumulating
  flag* (`changed`) that must be true by the end. Recognizing which predicates
  are filters vs. accumulators is the core modeling step in digit DP.
- **`0` is excluded automatically** because it can never set `changed`; no
  special leading-zero handling is required for this particular problem.
- **`changed` must be part of the memo key** — two prefixes reaching the same
  `pos` can have different `changed` values and therefore different completions.
- If the problem instead asked to *include* numbers equal to their rotation
  (i.e. count all *valid* numbers), you would simply return `1` unconditionally
  at the base case and drop the `changed` state.
