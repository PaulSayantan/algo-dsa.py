# Number of Ways to Wear Different Hats — Solution

## Brute Force

Try to give each **person** one of their liked hats, backtracking and marking
hats as used so no type repeats.

- **Time:** `O(40^n)` in the worst case — each of `n` people picks among up to
  `40` hats. With `n = 10` that is `40^10 ≈ 10^16`, far too slow.
- **Space:** `O(n)` recursion plus a used-hat set.

Why the mask should be over **people, not hats:** a mask over hats would need
`2^40` states, which is hopeless. A mask over people needs only `2^10 = 1024`
states. Always put the bitmask on the smaller universe.

## Optimal Approach (Bitmask DP over people)

### Reframe: assign people to hats

Instead of "each person picks a hat," process **hats one at a time** and decide
which (if any) still-unassigned person wears the current hat. Since hats are
processed once each, no hat type can be reused — the ordering guarantees the
distinctness constraint for free.

Build `hat_to_people[h]` = the list/bitmask of people who like hat `h`.

### DP definition

Let `dp[h][mask]` = the number of ways, considering only hats `1..h`, to have
covered exactly the set of people in `mask` (each with a distinct hat among the
first `h` types).

- **Base case:** `dp[0][0] = 1` (no hats considered, nobody covered).
- **Transition** for hat `h` (from `dp[h-1][*]` to `dp[h][*]`):
  - **Skip hat `h`:** `dp[h][mask] += dp[h-1][mask]`.
  - **Give hat `h` to some person `p`** who likes it and is *not* in `mask`:
    `dp[h][mask | (1 << p)] += dp[h-1][mask]`.
  All additions are taken modulo `1e9 + 7`.
- **Answer:** `dp[40][(1 << n) - 1]` — all people covered after all hats.

The `h` dimension can be collapsed with a rolling 1-D array of size `2^n`,
iterating hats in the outer loop.

### Why it is correct

Each hat is offered exactly once and to at most one person, so distinct hat
types are guaranteed. Every valid full assignment corresponds to a unique
sequence of "hat `h` -> person `p` or skip" choices as `h` runs `1..40`, and
the DP sums over exactly those sequences that end with all `n` people covered.
Counting is exact because each assignment is generated once (hats are visited in
fixed increasing order).

### Reference implementation

```python
class Solution:
    def numberWays(self, hats):
        MOD = 10 ** 9 + 7
        n = len(hats)
        full = (1 << n) - 1

        # For each hat type, which people like it (as a list of person indices).
        hat_to_people = [[] for _ in range(41)]
        for person, liked in enumerate(hats):
            for h in liked:
                hat_to_people[h].append(person)

        dp = [0] * (1 << n)
        dp[0] = 1
        for h in range(1, 41):
            # iterate masks high-to-low is unnecessary here because we read the
            # previous hat's values; use a fresh next-layer array for clarity.
            ndp = dp[:]  # "skip hat h" copies the previous counts forward
            for mask in range(1 << n):
                if dp[mask] == 0:
                    continue
                for p in hat_to_people[h]:
                    if mask & (1 << p):
                        continue
                    nm = mask | (1 << p)
                    ndp[nm] = (ndp[nm] + dp[mask]) % MOD
            dp = ndp
        return dp[full] % MOD
```

- **Time:** `O(40 * 2^n * n)` — 40 hats, `2^n` masks, up to `n` people per hat.
  For `n = 10`: `40 * 1024 * 10 ≈ 4.1 * 10^5`. Very fast.
- **Space:** `O(2^n)` with the rolling array.

## Key Insights & Edge Cases

- **Mask the smaller set.** People (`<= 10`) not hats (`<= 40`). This choice is
  the whole problem.
- **Process hats as the "resource" being handed out;** the fixed processing
  order is what enforces "no hat used twice" without extra bookkeeping.
- **Rolling array + copy-forward** implements the skip transition cleanly. If
  you instead update `dp` in place with a single array, add each person's
  contribution carefully so a hat is not implicitly reused within the same `h`.
- **Modulo every addition** to avoid overflow and match the required output.
- **Unreachable states** (`dp[mask] == 0`) can be skipped for speed.
- **Answer is `dp[full]`;** partial coverage (some person hatless) never counts.
