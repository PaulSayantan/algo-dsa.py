# Solution — Number of Beautiful Integers in the Range

## Brute Force

Scan every integer in `[low, high]`; for each, count even vs. odd digits and
test divisibility by `k`.

```python
def numberOfBeautifulIntegers(low: int, high: int, k: int) -> int:
    count = 0
    for x in range(low, high + 1):
        s = str(x)
        even = sum(1 for c in s if int(c) % 2 == 0)
        odd = len(s) - even
        if even == odd and x % k == 0:
            count += 1
    return count
```

- **Time:** `O((high - low) * log high)`.
- **Space:** `O(log high)`.

With `high` up to `10^9`, the loop can be a billion iterations — too slow.

## Optimal Approach (Digit DP + prefix counting)

### Reduce the range with prefix counting

Define `f(N)` = number of beautiful integers in `[0, N]`. Then

```
answer = f(high) - f(low - 1)
```

Each `f(N)` is a single digit DP. This "subtract the prefix below `low`" trick is
the standard way to turn an arbitrary `[low, high]` query into two `[0, N]`
counts.

### The DP state

We must simultaneously enforce two accumulative conditions, so we carry two extra
state components beyond the usual `pos`/`tight`:

- `pos` — current digit index (MSB first).
- `rem` — the number built so far, modulo `k`. Divisibility by `k` at the end
  means `rem == 0`. Updated by `rem' = (rem * 10 + d) % k`.
- `balance` — `(# even digits) - (# odd digits)` placed so far. The
  even-equals-odd condition means `balance == 0` at the end. Even digit adds
  `+1`, odd digit adds `-1`.
- `tight` — prefix equals `N`'s prefix (caps the current digit at `digits[pos]`).
- `started` — whether a first nonzero digit has been placed (leading-zero flag).

### Handling leading zeros correctly

This is the crux and the most common bug. A leading zero is *not* a real digit of
the number, so while `started` is `False` and we place `d == 0`, we must **not**
count it toward `balance` (it is not an "even digit" of the number) and we keep
`started = False`. Only once a nonzero digit appears does the number "start", and
from then on every placed digit — including genuine interior/trailing `0`s —
counts toward `balance` and `rem`.

```python
from functools import lru_cache

def numberOfBeautifulIntegers(low: int, high: int, k: int) -> int:
    def count_up_to(N: int) -> int:
        if N < 0:
            return 0
        digits = list(map(int, str(N)))
        L = len(digits)

        @lru_cache(maxsize=None)
        def dp(pos: int, rem: int, balance: int, tight: bool, started: bool) -> int:
            if pos == L:
                return 1 if (started and rem == 0 and balance == 0) else 0
            hi = digits[pos] if tight else 9
            total = 0
            for d in range(hi + 1):
                nt = tight and d == hi
                if not started and d == 0:
                    # leading zero: does not affect rem or balance
                    total += dp(pos + 1, 0, 0, nt, False)
                else:
                    nb = balance + (1 if d % 2 == 0 else -1)
                    total += dp(pos + 1, (rem * 10 + d) % k, nb, nt, True)
            return total

        return dp(0, 0, 0, True, False)

    return count_up_to(high) - count_up_to(low - 1)
```

Why it is correct: `count_up_to(N)` enumerates each integer in `[0, N]` exactly
once (the `tight` flag prevents overshoot). A completed path is counted only when
the number actually started (`started`), is divisible by `k` (`rem == 0`), and
has balanced parity (`balance == 0`) — precisely the beautiful conditions. The
leading-zero rule guarantees, e.g., that `10` is scored on its real digits
`{1, 0}` (balance 0) and not on phantom leading zeros. Subtracting
`count_up_to(low - 1)` removes the numbers below `low`.

- **Time:** `O(L * k * (2L+1) * 2 * 2 * 10)` per `f(N)` call — states
  `(pos, rem, balance, tight, started)` times 10 transitions. With `L <= 10`,
  `k <= 20`, `balance in [-L, L]`, this is on the order of `10^5`–`10^6`
  operations; two calls total. Effectively instant.
- **Space:** `O(L * k * L)` for the memo per call.

## Key Insights & Edge Cases

- **Two accumulators in one DP.** The power of digit DP is stacking independent
  digit properties into the state tuple: here `rem` (divisibility) and `balance`
  (parity count) coexist without interfering.
- **`balance` can go negative.** Represent it as `even - odd` and require `0` at
  the end; Python dict/`lru_cache` keys handle negatives fine. (In array-based
  DP you would offset by `L` to keep indices non-negative.)
- **Leading zeros must not skew parity or remainder.** Failing to guard
  `not started and d == 0` is the classic mistake — it would falsely add even
  digits (`0` is even) and inflate `balance`, breaking numbers like `10`.
- **Odd total digit length can never be beautiful**: if the number has an odd
  count of real digits, even and odd counts can't be equal, so `balance != 0`.
  The DP discovers this automatically; no special-casing needed.
- **Reset/rebuild the memo per bound.** `count_up_to(high)` and
  `count_up_to(low - 1)` use different `digits` arrays, so use a fresh cache
  (a new closure) for each, as shown, to avoid cross-contamination.
- **`low - 1` handles the lower endpoint inclusively**, and `low >= 1` per the
  constraints so `low - 1 >= 0` is safe (and `count_up_to` guards `N < 0` anyway).
