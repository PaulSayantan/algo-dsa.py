# Solution — Number of Digit One

## Brute Force

Loop over every integer `i` from `1` to `n` and, for each, count how many of its
decimal digits equal `1` (e.g. by repeatedly taking `i % 10`). Add these counts.

```python
def countDigitOne(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        x = i
        while x:
            total += (x % 10 == 1)
            x //= 10
    return total
```

- **Time:** `O(n * log n)` — `n` numbers, each with `O(log n)` digits.
- **Space:** `O(1)`.

With `n` up to `10^9` this is roughly `10^10` digit operations — far too slow.

## Optimal Approach (Digit DP)

We count occurrences by summing, over each digit *position*, how many *placed*
`1`s appear there among all numbers in `[0, n]`. The clean way to express this is
a memoized digit DP that returns "the number of `1`s contributed by all valid
completions of the current prefix".

State:

- `pos` — current digit index, `0` at the most significant digit.
- `count` — how many `1`s we have already placed in positions `[0, pos)`.
- `tight` — whether the prefix chosen so far exactly equals `n`'s prefix. If
  `tight` is `True`, the digit at `pos` may range only up to `digits[pos]`;
  otherwise it may range `0..9`.

Transition: at position `pos` we try each digit `d` in the allowed range. If `d`
equals `1` we increment `count`. The new `tight` is `tight and d == limit`.

Base case: when `pos == len(digits)` we have formed a complete number and return
`count` — the number of `1`s that this fully specified number contributes.

Because `dp` returns a *sum* over completions rather than a plain count, the
result at the top call is exactly the total number of `1`s over `[0, n]`.

```python
from functools import lru_cache

def countDigitOne(n: int) -> int:
    if n <= 0:
        return 0
    digits = list(map(int, str(n)))
    L = len(digits)

    @lru_cache(maxsize=None)
    def dp(pos: int, count: int, tight: bool) -> int:
        if pos == L:
            return count
        limit = digits[pos] if tight else 9
        total = 0
        for d in range(limit + 1):
            total += dp(pos + 1, count + (d == 1), tight and d == limit)
        return total

    return dp(0, 0, True)
```

Why it is correct: every integer in `[0, n]` corresponds to exactly one leaf of
this digit-choice tree (leading zeros simply form the smaller-magnitude numbers,
e.g. `013` is the number `13`), and at each leaf we return the exact number of
`1` digits in that specific number. Summing over all leaves counts every `1`
occurrence exactly once. The `tight` flag guarantees we never generate a number
greater than `n`.

- **Time:** `O(L * L * 2 * 10)` — states are `(pos, count, tight)` with
  `pos <= L`, `count <= L`, `tight in {0,1}`, and 10 transitions each. For
  `n <= 10^9`, `L <= 10`, so this is a few thousand operations.
- **Space:** `O(L * L)` for the memo plus `O(L)` recursion depth.

### Alternative: closed-form per position

The same count can be obtained without recursion by, for each place value
`10^k`, computing `high`, `cur`, `low`:

```
contribution = high * 10^k
             + (10^k               if cur > 1
                else low + 1       if cur == 1
                else 0)
```

Digit DP is preferred here because it generalizes trivially to "count digit `d`",
"count numbers containing a `1`", and much richer digit properties, whereas the
closed form must be rederived for each variant.

## Key Insights & Edge Cases

- **`n = 0`:** the answer is `0`; guard against `str(0)` producing spurious work.
- **Occurrences vs. numbers:** returning `count` at the base case (not `count > 0`)
  is what makes this count *occurrences*. If instead you wanted "how many numbers
  contain at least one `1`", return `1 if count > 0 else 0`.
- **Leading zeros are harmless here** because a leading zero contributes `0` to
  `count`, so treating `007` as `7` gives the correct digit-`1` count.
- **Memoization on `tight`:** when `tight` is `True` there is only one such path
  per `pos`, but caching it is still safe and keeps the code uniform.
