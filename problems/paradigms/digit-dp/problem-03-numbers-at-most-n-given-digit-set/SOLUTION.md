# Solution — Numbers At Most N Given Digit Set

## Brute Force

Generate every number writable from the allowed digits, in increasing length,
and count those `<= n`. Even bounding the length by `len(str(n))`, the number of
strings is `sum_{len} k^len`, which for `k = 9` and 10-digit `n` is on the order
of `9 + 9^2 + ... + 9^10 ~ 4 * 10^9` — too many to enumerate.

```python
def atMostNGivenDigitSet(digits, n):
    from itertools import product
    count = 0
    L = len(str(n))
    for length in range(1, L + 1):
        for combo in product(digits, repeat=length):
            if int("".join(combo)) <= n:
                count += 1
    return count
```

- **Time:** `O(k^L * L)`.
- **Space:** `O(L)`.

## Optimal Approach (Digit DP)

Let `s = str(n)`, `L = len(s)`, and `k = len(digits)`. A writable positive
integer is `<= n` in exactly one of two disjoint ways.

### Part A — strictly fewer digits than `n`

Any number with `length < L` is automatically `< n`. Since the digit set never
contains `'0'`, **every** length-`length` string over the alphabet is a valid
positive number with no leading-zero concern. There are `k^length` of them:

```
partA = k^1 + k^2 + ... + k^(L-1)
```

### Part B — exactly `L` digits and `<= n`

Walk the positions of `s` from most significant to least while *tight* (prefix
equals `n`'s prefix so far). At position `pos` with current bound digit
`c = s[pos]`, consider each allowed digit `d`:

- **`d < c`:** the prefix is now strictly below `n`, so all `L - pos - 1`
  remaining positions can be filled freely — add `k^(L - pos - 1)`.
- **`d == c`:** we remain tight; move to `pos + 1`.
- **`d > c`:** this and larger choices exceed `n`; stop scanning this position.

If we manage to stay tight through all `L` positions, then `n` itself is
writable, so add `1`.

```python
from functools import lru_cache

def atMostNGivenDigitSet(digits, n):
    s = str(n)
    L = len(s)
    k = len(digits)

    # Part A: fewer digits
    total = 0
    for length in range(1, L):
        total += k ** length

    # Part B: exactly L digits, tight walk
    for pos in range(L):
        c = s[pos]
        matched = False
        for d in digits:
            if d < c:
                total += k ** (L - pos - 1)
            elif d == c:
                matched = True  # stay tight, handled by continuing the loop
        if not matched:
            break
    else:
        total += 1  # n itself is writable

    return total
```

Equivalent memoized formulation (closer to canonical digit DP), returning the
count of completions:

```python
@lru_cache(maxsize=None)
def dp(pos, tight):
    if pos == L:
        return 1  # a complete same-length number that stayed <= n
    total = 0
    limit = s[pos]
    for d in digits:
        if tight:
            if d < limit:
                total += k ** (L - pos - 1)   # free tail
            elif d == limit:
                total += dp(pos + 1, True)
            # d > limit: skip
        # tight == False handled by the k**rest shortcut above
    return total
# answer = partA + dp(0, True)
```

Why it is correct: Part A and Part B are disjoint (different lengths vs.
same length) and together cover all writable positives `<= n`. The tight walk
counts precisely the length-`L` writable numbers not exceeding `n`, because
once a digit `< c` is chosen the remaining suffix is unconstrained, and larger
digits are pruned.

- **Time:** `O(L * k)` — each of the `L` positions scans the `k` allowed digits.
  (Computing `k^rest` is `O(1)` with precomputed powers.) `L <= 10`, `k <= 9`.
- **Space:** `O(L)`.

## Key Insights & Edge Cases

- **No `'0'` in the alphabet** is a gift: every string is a valid number with no
  leading-zero ambiguity, so `k^length` counts cleanly. If `'0'` were allowed,
  you would need a separate leading-zero/started flag to avoid counting `007`.
- **The `for/else` construct** neatly adds `1` for `n` itself only if the loop
  never `break`s (i.e. we stayed tight the whole way — `n` is fully writable).
- **`n` itself might not be writable** (e.g. it contains a digit not in the set);
  in that case `d == c` never matches at some position, the loop breaks, and we
  correctly do not add `1`.
- **Watch the exponent:** the free tail after choosing `d < c` at position `pos`
  has `L - pos - 1` positions, not `L - pos`.
