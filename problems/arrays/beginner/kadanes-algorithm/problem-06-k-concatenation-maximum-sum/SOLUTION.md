# Solution — K-Concatenation Maximum Sum

## Brute Force

Build the full array of length `n * k` and run Kadane on it (empty subarray
allowed, so clamp at `0`).

```python
def kConcatenationMaxSum(arr, k):
    big = arr * k
    cur = best = 0
    for x in big:
        cur = max(0, cur + x)
        best = max(best, cur)
    return best % (10**9 + 7)
```

- **Time:** O(n * k) — infeasible when `n` and `k` are both up to `10^5`
  (up to `10^10` elements).
- **Space:** O(n * k) to materialize the array.

## Optimal Approach — Kadane on at most two copies

**Key observation.** An optimal subarray of the repeated array touches at most
two "boundary" copies — a suffix of one copy and a prefix of another — with zero
or more *full* copies sandwiched in between. Two facts follow:

1. Running Kadane over **two** concatenated copies (`arr + arr`) already captures
   any subarray that crosses a single seam, including the best suffix + best
   prefix combination.
2. Full interior copies help only if one copy's total `s = sum(arr)` is
   **positive**; then each of the `k - 2` interior copies adds `s`. If `s <= 0`,
   extra copies never help, so two copies suffice.

So, letting `kadane(a)` be the max subarray sum of `a` with the empty subarray
allowed (result `>= 0`):

```
if k == 1:            answer = kadane(arr)
elif s > 0:           answer = kadane(arr + arr) + (k - 2) * s
else:                 answer = kadane(arr + arr)
```

Take everything modulo `10^9 + 7` at the end.

### Reference implementation

```python
def kConcatenationMaxSum(arr, k):
    MOD = 10**9 + 7

    def kadane(a):
        cur = best = 0          # empty subarray allowed -> never negative
        for x in a:
            cur = max(0, cur + x)
            best = max(best, cur)
        return best

    s = sum(arr)
    one = kadane(arr)
    if k == 1:
        return one % MOD
    two = kadane(arr + arr)
    if s > 0:
        return (two + (k - 2) * s) % MOD
    return two % MOD
```

### Why it is correct

- **Crossing one seam:** two copies contain every possible (suffix of copy A) +
  (prefix of copy B) pair, so `kadane(arr + arr)` is the best sum using at most
  two boundary copies and no interior copies.
- **Interior copies:** if the optimal subarray spans `>= 3` copies, its interior
  full copies each contribute exactly `s`. When `s > 0`, greedily include all
  `k - 2` of them, added to the two-copy boundary result. When `s <= 0`, an
  interior copy can only reduce the sum, so the optimum uses at most two copies
  and equals `two`.
- **Empty subarray:** seeding Kadane at `0` guarantees a non-negative result,
  matching the "length-0 subarray sum 0" rule (Example 3).

### Step-by-step on `arr = [1, -2, 1], k = 5`

- `s = sum([1, -2, 1]) = 0`.
- `kadane([1, -2, 1]) = 1` (best single copy).
- `kadane([1, -2, 1, 1, -2, 1]) = 2` — the seam pair `... 1 | 1 ...` sums to `2`.
- Since `s = 0` (not `> 0`), interior copies add nothing, so answer `= two = 2`.

Answer: **2**.

- **Time:** O(n) — Kadane over one or two copies (each O(n)).
- **Space:** O(n) to hold `arr + arr` (or O(1) by looping the index modulo `n`).

## Key Insights & Edge Cases

- **`k == 1`:** there is no seam, so only `kadane(arr)` applies; do not use
  `arr + arr`.
- **`s <= 0`:** never add interior copies; the `(k - 2) * s` term would only hurt.
- **All negative** (Example 3): `kadane` returns `0` (empty subarray) and `s < 0`,
  so the answer is `0`.
- **Overflow / modulo:** in Python integers are unbounded, but still apply
  `% (10^9 + 7)` at the very end; in fixed-width languages compute the modulo
  carefully since `(k - 2) * s` can be large.
- **Two copies, not three:** a common bug is repeating three times "to be safe."
  Two copies plus the `(k - 2) * s` term is provably sufficient and cheaper.
